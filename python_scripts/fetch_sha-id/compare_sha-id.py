import csv
import sys
import os
from datetime import datetime
from tabulate import tabulate

def read_sha_csv(file_path):
    sha_map = {}
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            app_name = row['App-Name'].strip().lower()
            sha = row['SHA-ID'].strip()
            sha_map[app_name] = sha
    return sha_map

def compare_sha(reference_file, target_file):
    ref_sha_map = read_sha_csv(reference_file)
    tgt_sha_map = read_sha_csv(target_file)

    results = []

    for app, sha_b in tgt_sha_map.items():
        sha_a = ref_sha_map.get(app, None)
        if sha_a is None:
            status = "Missing_in_Reference"
            sha_a = "N/A"
        elif sha_a == sha_b:
            status = "Matched"
        else:
            status = "Mismatch"
        results.append([app, sha_b, sha_a, status])

    # 📁 Create output folder
    output_dir = "compare_output"
    os.makedirs(output_dir, exist_ok=True)

    # 🕒 Create timestamped file name
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    output_file = os.path.join(output_dir, f"sha_comparison_{timestamp}.csv")

    # 💾 Write to CSV
    with open(output_file, 'w', newline='') as out:
        writer = csv.writer(out)
        writer.writerow(["App-Name", "SHA_in_target", "SHA_in_refrence", "Status"])
        writer.writerows(results)

    # 🖥️ Print to console
    print("\n📋 SHA Comparison Result:\n")
    print(tabulate(results, headers=["App-Name", "SHA_in_target", "SHA_in_refrence", "Status"], tablefmt="grid"))
    print(f"\n✅ Comparison complete. Output saved to '{output_file}'")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 compare_sha_outputs.py <input_for_target.csv> <input_for_refrence.csv>")
        sys.exit(1)

    reference = sys.argv[1]
    target = sys.argv[2]
    compare_sha(reference, target)
