import os
import argparse
import hashlib
from time import sleep
from pathlib import Path
import requests
from pprint import pprint

API_KEY = "ad5d58b0ce9b93a7646c3fe87053cb2e7f9d5fa8963060107bb9aef41ab8c354"
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
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            scan_file(file_path)

    print("Scan completed.")

def scan_file(file_path):
    file = Path(file_path)

    if not file.exists():
        print(f"File not found: {file_path}")
        return

    print(f"Scanning file: {file_path}")
    f_hash = hash_it(file, "sha256")
    response = vt_get_data(f_hash)

    if response is not None:
        pprint(response, width=2)
        print()
        if response.get("last_analysis_stats").get("malicious") > 0:
            print("Result: Malicious")
        else:
            print("Result: Clean")
    else:
        print("No information available for the file.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scan files in a directory with VirusTotal")
    parser.add_argument("directory", action="store", nargs=1, help="directory to scan")

    parsed_args = parser.parse_args()
    directory = parsed_args.directory[0]

    scan_directory(directory)
