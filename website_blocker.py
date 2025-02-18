import datetime
import time

# Define the end time for blocking
end_time = datetime.datetime(2025, 12, 4, 23, 59, 59)

# Take multiple website URLs from user
site_block = input("Enter website URLs to block (separate with commas): ").split(",")

# Trim spaces from URLs
site_block = [site.strip() for site in site_block]

# Define file path correctly for Windows
host_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

while True:
    if datetime.datetime.now() < end_time:
        print("Start Blocking Websites...")
        with open(host_path, "r+") as host_file:
            content = host_file.read()
            for website in site_block:
                if website not in content:
                    host_file.write(f"{redirect} {website}\n")

    else:
        print("Unblocking Websites...")
        with open(host_path, "r+") as host_file:
            content = host_file.readlines()
            host_file.seek(0)
            for line in content:
                if not any(website in line for website in site_block):
                    host_file.write(line)
            host_file.truncate()

        print("Blocking Ended. Websites are now accessible.")
        break

    time.sleep(5)  # Sleep to avoid excessive CPU usage
