import os
import argparse
import hashlib
from time import sleep, time
from pathlib import Path
import requests

API_KEY = "Your_API_KEY"
HEADERS = {"x-apikey": API_KEY}

def hash_it(file, algorithm):
    hasher = hashlib.new(algorithm)
    with open(file, 'rb') as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

def vt_get_data(f_hash):
    url = f"https://www.virustotal.com/api/v3/files/{f_hash}"
    while True:
        response = requests.get(url, headers=HEADERS)
        if response.status_code == 200:
            return response.json().get("data").get("attributes")
        elif response.status_code == 404:
            return None
        elif error_handle(response):
            break
    return None

def vt_post_files(file, url="https://www.virustotal.com/api/v3/files"):
    with open(file, "rb") as f:
        file_bin = f.read()
    upload_package = {"file": (file.name, file_bin)}
    while True:
        response = requests.post(url, headers=HEADERS, files=upload_package)
        if error_handle(response):
            break
    return response

def vt_get_analyses(response):
    _id = response.json().get("data").get("id")
    url = f"https://www.virustotal.com/api/v3/analyses/{_id}"
    while True:
        response = requests.get(url, headers=HEADERS)
        if error_handle(response):
            break
    return response

def error_handle(response):
    if response.status_code == 429:
        print("WAITING")
        sleep(60)
    elif response.status_code == 401:
        raise Exception("Invalid API key")
    elif response.status_code not in (200, 404, 429):
        raise Exception(response.status_code)
    else:
        return True
    return False

def scan_directory(directory):
    print(f"Scanning directory: {directory}")
    start_time = time()
    infected_files = []
    clean_files = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            result = scan_file(file_path)
            if result == "Malicious":
                infected_files.append(file_path)
            elif result == "Clean":
                clean_files.append(file_path)

    end_time = time()
    total_time = end_time - start_time

    print("\nScan completed.")
    print("\nInfected Files:")
    print("\n".join(infected_files))
    print("\nClean Files:")
    print("\n".join(clean_files))
    print(f"\nTotal time taken: {total_time:.2f} seconds")

def scan_file(file_path):
    file = Path(file_path)

    if not file.exists():
        print(f"File not found: {file_path}")
        return "Not Found"

    print(f"Scanning file: {file_path}")
    f_hash = hash_it(file, "sha256")
    response = vt_get_data(f_hash)

    if response is not None:
        if response.get("last_analysis_stats").get("malicious") > 0:
            print("Result: Malicious")
            return "Malicious"
        else:
            print("Result: Clean")
            return "Clean"
    else:
        print("No information available for the file.")
        return "Unknown"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scan files in a directory with VirusTotal")
    parser.add_argument("directory", action="store", nargs=1, help="directory to scan")

    parsed_args = parser.parse_args()
    directory = parsed_args.directory[0]

    scan_directory(directory)
