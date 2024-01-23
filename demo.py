import os
import json
import urllib.parse
import urllib.request
from urllib.error import HTTPError

def submit_file_for_scan(api_key, file_path):
    url_scan = 'https://www.virustotal.com/vtapi/v2/file/scan'
    api_key_param = {'apikey': api_key}

    with open(file_path, 'rb') as file:
        files_param = {'file': (os.path.basename(file_path), file.read())}

    encoded_params_scan = urllib.parse.urlencode(api_key_param).encode('utf-8')

    try:
        url_scan_with_params = f"{url_scan}?{encoded_params_scan.decode('utf-8')}"
        print(f"Submitting file {file_path} to: {url_scan_with_params}")  # Debug print
        request_scan = urllib.request.Request(url_scan_with_params, data=files_param['file'][1], headers={'User-Agent': 'Mozilla/5.0'})
        response_scan = urllib.request.urlopen(request_scan)

        # Follow redirects if necessary
        if response_scan.geturl() != request_scan.get_full_url():
            url_scan = response_scan.geturl()
            print(f"Following redirect to: {url_scan}")  # Debug print

    except HTTPError as e:
        print(f"Error submitting file {file_path} for scanning. HTTP status code: {e.code}")
        return None

    return url_scan

def get_scan_report(api_key, resource_id):
    url_report = 'https://www.virustotal.com/vtapi/v2/file/report'
    params_report = {'apikey': api_key, 'resource': resource_id}
    encoded_params_report = urllib.parse.urlencode(params_report).encode('utf-8')

    try:
        url_report_with_params = f"{url_report}?{encoded_params_report.decode('utf-8')}"
        print(f"Requesting report for resource {resource_id} from: {url_report_with_params}")  # Debug print
        response_report = urllib.request.urlopen(urllib.request.Request(url_report_with_params, headers={'User-Agent': 'Mozilla/5.0'}))
    except HTTPError as e:
        print(f"Error getting report for resource {resource_id}. HTTP status code: {e.code}")
        return None

    return response_report

def scan_folder(api_key, folder_path):
    clean_files = []
    infected_files = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            scan_url = submit_file_for_scan(api_key, file_path)

            if scan_url:
                response_report = get_scan_report(api_key, scan_url)
                
                if response_report:
                    json_response_report = json.loads(response_report.read().decode('utf-8'))

                    if json_response_report['response_code'] == 1:
                        if json_response_report['positives'] == 0:
                            clean_files.append(file)
                            print(f"File {file} is clean.")  # Debug print
                        else:
                            infected_files.append({
                                'file': file,
                                'positives': json_response_report['positives'],
                                'total': json_response_report['total'],
                                'scan_date': json_response_report['scan_date']
                            })
                            print(f"File {file} is infected.")  # Debug print
                    else:
                        print(f"Failed to get report for file {file}. Response: {json_response_report['verbose_msg']}")
    
    print("\nScan Results:")
    if infected_files:
        print("Infected Files:")
        for file_info in infected_files:
            print(f"{file_info['file']} - {file_info['positives']} out of {file_info['total']} scanners detected the file on {file_info['scan_date']}")
    else:
        print("All files are clean. No viruses found.")

# Replace 'YOUR_API_KEY' with your actual VirusTotal API key
api_key = 'your_api_key'
# Replace 'YOUR_FOLDER_PATH' with the path to the folder you want to scan
folder_path = 'D:\\Tools'

scan_folder(api_key, folder_path)
