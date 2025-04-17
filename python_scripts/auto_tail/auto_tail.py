import subprocess
import time
import getpass
import sys
import os

def launch_tail(ip, filepath, grep_cmd, username, password):
    # Set tab title
    title_set = f'echo -ne "\\033]0;{ip}\\007"; '

    # Remote log tail command
    remote_command = f'tail -F {filepath} | {grep_cmd}'

    # SSH command with 3 retries inside the terminal
    ssh_cmd = f"""
    for i in {{1..3}}; do
        echo "Attempt $i to connect {ip}...";
        sshpass -p '{password}' ssh -o StrictHostKeyChecking=no {username}@{ip} "{remote_command}" && break;
        echo "SSH attempt $i failed for {ip}, retrying...";
        sleep 2;
    done
    """

    # Full shell command
    bash_cmd = f'{title_set} {ssh_cmd}; exec bash'

    # Launch new Terminator tab with command
    terminator_cmd = [
        "terminator",
        "--new-tab",
        "-e",
        f"bash -c '{bash_cmd}'"
    ]

    try:
        subprocess.Popen(terminator_cmd)
        print(f"[+] Launched terminator tab for {ip}")
    except Exception as e:
        print(f"[!] Error launching for {ip}: {e}")

def main():
    # Handle optional file input
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        if not os.path.exists(input_file):
            print(f"[!] Provided input file '{input_file}' does not exist.")
            return
    else:
        input_file = "servers.txt"
        if not os.path.exists(input_file):
            print("[!] Default 'servers.txt' not found.")
            return

    print(f"== Using Input File: {input_file} ==")
    username = input("Enter SSH username: ")
    password = getpass.getpass("Enter SSH password: ")

    with open(input_file, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue  # Skip empty lines and comments
            try:
                ip, file_path, grep_cmd = map(str.strip, line.split(","))
                launch_tail(ip, file_path, grep_cmd, username, password)
                time.sleep(0.3)
            except ValueError:
                print(f"[!] Invalid line: {line}")

if __name__ == "__main__":
    main()