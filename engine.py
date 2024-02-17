import os
import hashlib
import time
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

class Engine:
    def __init__(self, typeH):
        if typeH.lower() == "sha256":
            self.hash_file_path = "DataBase/HashDataBase/Sha256/virusHash.unibit"
        elif typeH.lower() == "md5":
            self.hash_file_path = "DataBase/HashDataBase/Md5/md5HashOfVirus.unibit"
        else:
            raise ValueError("Invalid hash type. Supported types are 'sha256' and 'md5'.")

        with open(self.hash_file_path, "r") as hash_file:
            self.hashList = hash_file.readlines()

    def hash_to_full_num(self, hash):
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        alpha_num = {char: str(i + 1) for i, char in enumerate(alpha)}
        result = ''.join(alpha_num.get(char, char) for char in hash.lower())
        return int(result)

    def binary_tree_search(self, h_list, value_to_find):
        initial_value, length_of_list = 0, len(h_list) - 1
        point_found = False

        while initial_value < length_of_list and not point_found:
            middle = (initial_value + length_of_list) // 2

            if h_list[middle] == value_to_find:
                point_found = True
                position_of_point = middle

            if h_list[middle] > value_to_find:
                length_of_list = middle

            if h_list[middle] < value_to_find:
                initial_value = middle + 1

        return position_of_point if point_found else None

    def calculate_hashes(self, path):
        file_hashes = {}

        for file_path in Path(path).rglob("*"):
            if file_path.is_file():
                try:
                    with open(file_path, "rb") as f:
                        file_hash = hashlib.md5()
                        while chunk := f.read(4096):
                            file_hash.update(chunk)
                        md5_hash = file_hash.hexdigest()
                        sha256_hash = hashlib.sha256(chunk).hexdigest()
                        file_hashes[file_path] = {'md5': md5_hash, 'sha256': sha256_hash}
                except Exception as e:
                    logging.error(f"Error calculating hash for file {file_path}: {e}")

        return file_hashes

    def virus_scanner(self, path_list, hash_function, scan_type):
        virus_path = []
        virus_hash_cy_py = []

        io_list = [self.hash_to_full_num(hash_val) for hash_val in self.hashList]
        io_list.sort()

        logging.info(f"\nStarted {scan_type} scan...")
        for file_path in path_list:
            try:
                directory_name = file_path.parent
                file_name = file_path.name
                logging.info(f"Scanning directory: {directory_name}, File: {file_name}...")

                logging.info(f"Calculating hash for file: {file_path}...")
                hash_value = hash_function(file_path)
                v_i_hash = self.binary_tree_search(io_list, self.hash_to_full_num(hash_value))

                if v_i_hash:
                    logging.info(f"File {file_path} is infected.")
                    virus_hash_cy_py.append(v_i_hash)
                    virus_path.append(file_path)
                else:
                    logging.info(f"File {file_path} is clean.")

            except Exception as e:
                logging.error(f"Error scanning file {file_path}: {e}")

        logging.info(f"{scan_type} scan completed.")

        if virus_path:
            logging.info("Virus found.")
        else:
            logging.info("No Virus Found.")

        return virus_hash_cy_py, virus_path

    def md5_hash(self, file_path):
        try:
            with open(file_path, "rb") as f:
                file_hash = hashlib.md5()
                while chunk := f.read(4096):
                    file_hash.update(chunk)
                md5_hash = file_hash.hexdigest()
            return md5_hash
        except Exception as e:
            logging.error(f"Error calculating MD5 hash for file {file_path}: {e}")
            return ''

    def quick_scan(self, path, extensions):
        files_to_scan = [file_path for file_path in Path(path).rglob("*") if file_path.is_file() and file_path.suffix.lower() in extensions]
        result = self.virus_scanner(files_to_scan, self.md5_hash, "Quick")
        self.update_report(result, path, "Quick")
        return result

    def full_scan(self, path):
        all_files = [file_path for file_path in Path(path).rglob("*") if file_path.is_file()]
        result = self.virus_scanner(all_files, self.md5_hash, "Full")
        self.update_report(result, path, "Full")
        return result

    def deep_scan(self, root_path):
        all_files = [file_path for file_path in Path(root_path).rglob("*") if file_path.is_file()]
        result = self.virus_scanner(all_files, self.md5_hash, "Deep")
        self.update_report(result, root_path, "Deep")
        return result

    def custom_scan(self, path):
        file_details = []
        scanned_files = []

        for file_path in Path(path).rglob("*"):
            if file_path.is_file():
                try:
                    file_stats = file_path.stat()
                    file_details.append({
                        "File Name": file_path.name,
                        "Size (bytes)": file_stats.st_size,
                        "Creation Time": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(file_stats.st_ctime)),
                        "Last Modified Time": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(file_stats.st_mtime))
                    })
                    scanned_files.append(str(file_path))  # Store path of scanned file
                except Exception as e:
                    logging.error(f"Error getting details for file {file_path}: {e}")

        result = file_details, scanned_files
        self.update_report(result, path, "Custom")
        return result

    def update_report(self, result, folder_path, scan_type):
        start = time.strftime("%Y-%m-%d %H:%M:%S")
        end = time.strftime("%Y-%m-%d %H:%M:%S")

        if result:
            if scan_type == "custom":
                file_details, scanned_files = result
                logging.info(f"Scanned Files: {scanned_files}")
                logging.info("File Details:")
                for detail in file_details:
                    logging.info(detail)
            else:
                if isinstance(result, tuple):
                    virus_hash_cy_py, virus_path = result
                    report_data = [f"Scanned Files: {virus_path[i]}, Virus Hash: {virus_hash_cy_py[i]}" for i in range(len(virus_path))]
                else:
                    report_data = ["File Details:"] + [f"{detail}" for detail in result]
                report_data.extend([
                    f"Scanned Folder: {folder_path}",
                    f"Scan Type: {scan_type}",
                    f"Start Time: {start}",
                    f"End Time: {end}",
                    f"Scan Results: Virus Found" if virus_path else "Scan Results: No Virus Found"
                ])
                save_report(report_data, "scan_report.txt")
        else:
            save_report(["No Virus Found."], "scan_report.txt")

def run_scan(scan_function, *args):
    start_time = time.time()
    result = scan_function(*args)
    end_time = time.time()
    print("\n")
    print("\n")
    logging.info(f"Total time taken for scanning: {end_time - start_time:.2f} seconds.")
    return result

def save_report(report_data, report_path):
    try:
        with open(report_path, "a",encoding="utf-8") as report_file: 
            if report_file.tell() != 0:  
                report_file.write("\n")  
            report_file.write("\n".join(report_data) + "\n") 
        logging.info(f"Report updated successfully at: {report_path}")
    except Exception as e:
        logging.error(f"Error updating report: {e}")

if __name__ == "__main__":
    try:
        hash_type = input("Choose the hash type (MD5/SHA256): ").strip().lower()
        if hash_type not in ['md5', 'sha256']:
            raise ValueError("Invalid hash type. Supported types are 'md5' and 'sha256'.")

        folder_path = input("Enter the full path of the directory to scan: ").strip()
        if not Path(folder_path).is_dir():
            raise ValueError("Invalid directory path. Please provide a valid path.")

        scan_choice = input("Choose the scan type (quick/full/deep/custom): ").strip().lower()

        engine = Engine(hash_type)

        if scan_choice == "quick":
            extensions = [".jpg", ".png", ".pdf", ".ppt"]
            result = run_scan(engine.quick_scan, folder_path, extensions)
        elif scan_choice == "full":
            result = run_scan(engine.full_scan, folder_path)
        elif scan_choice == "deep":
            result = run_scan(engine.deep_scan, folder_path)
        elif scan_choice == "custom":
            result = run_scan(engine.custom_scan, folder_path)

        logging.info(f"\nScanning completed.")
    except Exception as e:
        logging.error(f"Error: {e}")
