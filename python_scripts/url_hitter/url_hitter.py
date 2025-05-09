import requests
import time
import json

# Load config
with open("config.json", "r") as f:
    config = json.load(f)

urls = config.get("urls", [])
interval_seconds = config.get("interval_seconds", 10)

if not urls:
    print("No URLs found in config.")
    exit(1)

print(f"Starting URL hitter with interval = {interval_seconds}s. Press Ctrl+C to stop.")

try:
    while True:
        for url in urls:
            try:
                response = requests.get(url)
                print(f"[{time.strftime('%H:%M:%S')}] Hit {url} | Status: {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"[{time.strftime('%H:%M:%S')}] Error hitting {url}: {e}")
        print(f"Sleeping for {interval_seconds} seconds...\n")
        time.sleep(interval_seconds)
except KeyboardInterrupt:
    print("\nStopped by user.")
