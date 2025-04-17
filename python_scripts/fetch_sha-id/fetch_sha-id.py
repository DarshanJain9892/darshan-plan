import paramiko
import getpass
import csv
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
import sys
import os

def read_servers(file_path):
    servers = []
    with open(file_path, 'r') as file:
        for idx, line in enumerate(file):
            if line.strip() and not line.strip().startswith("#"):
                parts = line.strip().split(',')
                if len(parts) == 3:
                    servers.append((idx, parts[0], parts[1], parts[2]))
    return servers

def fetch_sha(index, ip, tomcat_name, app_name, username, password, max_attempts=3):
    attempt = 0
    while attempt < max_attempts:
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(ip, username=username, password=password, timeout=10)

            path = f"/opt/{tomcat_name}/webapps/{app_name}/WEB-INF/classes/git-revision"
            command = f"cat {path}"
            stdin, stdout, stderr = ssh.exec_command(command)

            output = stdout.read().decode().strip()
            error = stderr.read().decode().strip()
            ssh.close()

            if output:
                return (index, ip, tomcat_name, app_name, output)
            else:
                msg = error if error else "git-revision file not found or empty"
                return (index, ip, tomcat_name, app_name, f"Error: {msg}")

        except Exception as e:
            attempt += 1
            if attempt < max_attempts:
                print(f"[{ip}] Attempt {attempt} failed, retrying...")
                time.sleep(2)
            else:
                return (index, ip, tomcat_name, app_name, f"SSH Failed after {max_attempts} attempts: {str(e)}")

if __name__ == "__main__":
    # Use file passed via command-line or default to servers.txt
    input_file = sys.argv[1] if len(sys.argv) > 1 else "servers.txt"

    if not os.path.isfile(input_file):
        print(f"❌ Input file '{input_file}' not found!")
        sys.exit(1)

    # Generate timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")

    # Create output folder if not exists
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    # Derive output filename inside output/
    if len(sys.argv) > 1:
        base_name = os.path.splitext(os.path.basename(input_file))[0]
        output_file = os.path.join(output_dir, f"{base_name}_{timestamp}.csv")
    else:
        output_file = os.path.join(output_dir, f"sha_output_{timestamp}.csv")

    servers = read_servers(input_file)

    print("Enter SSH credentials to connect to servers:")
    username = input("Username: ")
    password = getpass.getpass("Password: ")

    results = []
    print(f"\n🔄 Fetching SHA IDs with retries (max 3 attempts) from '{input_file}'...\n")

    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_server = {
            executor.submit(fetch_sha, idx, ip, tomcat, app, username, password): idx
            for idx, ip, tomcat, app in servers
        }

        for future in as_completed(future_to_server):
            result = future.result()
            results.append(result)
            print(f"[{result[1]}] => {result[4]}")

    # Sort results by original input order
    results.sort(key=lambda x: x[0])

    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["IP", "Tomcat-Name", "App-Name", "SHA-ID"])
        for _, ip, tomcat, app, sha in results:
            writer.writerow([ip, tomcat, app, sha])

    print(f"\n✅ Ordered output saved to '{output_file}'")
