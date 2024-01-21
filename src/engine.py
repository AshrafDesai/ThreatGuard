from hashlib import md5
import os
import time


class Engine:

    def __init__(self, typeH):
        if typeH.lower() == "sha256":
            with open("DataBase\\HashDataBase\\Sha256\\virusHash.unibit", "r") as i:
                self.hashList = i.readlines()
                i.close()

        if typeH.lower() == "md5":
            with open("DataBase\\HashDataBase\\Md5\\md5HashOfVirus.unibit", "r") as i:
                self.hashList = i.readlines()
                i.close()

    def hashToFullNum(self, hash):
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        alphaNum = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8,
                    'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17,
                    'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

        j = ''

        sampleHash = hash.lower()

        for i in sampleHash:
            if i in alpha:
                i = alphaNum[i]

            j = j + str(i)

        return int(j)

    def binaryTreeSearch(self, hList, valueToFind):
        initialValue = 0
        lengthOfList = len(hList) - 1
        pointFound = 0

        while (initialValue < lengthOfList and pointFound == 0):
            middle = (initialValue + lengthOfList) // 2

            if hList[middle] == valueToFind:
                pointFound = 1
                positionOfPoint = middle

            if hList[middle] > valueToFind:
                lengthOfList = middle

            if hList[middle] < valueToFind:
                initialValue = middle + 1

        if pointFound == 1:
            return positionOfPoint

        else:
            return None

    def sha256_hash(self, filename):
        import hashlib
        try:
            with open(filename, "rb") as f:
                bytes = f.read()
                sha256hash = hashlib.sha256(bytes).hexdigest()
                f.close()
            return sha256hash
        except:
            return 0

    def Md5_hash(self, filename):
        import hashlib
        try:
            with open(filename, "rb") as f:
                bytes = f.read()
                md5Hash = hashlib.md5(bytes).hexdigest()
                f.close()
            return md5Hash
        except:
            return 0

    def calculate_hashes(self, path):
        file_hashes = {}

        # Get the list of all files in directory tree at given path
        dir_list = list()
        for (dirpath, dirnames, filenames) in os.walk(path):
            dir_list += [os.path.join(dirpath, file) for file in filenames]

        print(f"\nCalculating hashes of files in directory: {path}")
        for i, file_path in enumerate(dir_list):
            try:
                print(f"Calculating hash for file {i + 1}/{len(dir_list)}: {file_path}...")
                md5_hash = self.Md5_hash(file_path)
                sha256_hash = self.sha256_hash(file_path)
                file_hashes[file_path] = {'md5': md5_hash, 'sha256': sha256_hash}
            except Exception as e:
                print(f"Error calculating hash for file {file_path}: {e}")

        return file_hashes

    def virusScannerSha256(self, path):
        self.virusPath = []
        self.virusHashCyPy = []

        ioList = []

        for i in self.hashList:
            ioList.append(self.hashToFullNum(i))

        ioList.sort()

        # Get the list of all files in directory tree at given path
        dir_list = list()
        for (dirpath, dirnames, filenames) in os.walk(path):
            dir_list += [os.path.join(dirpath, file) for file in filenames]

        print(f"\nScanning directory: {path}")
        for i, file_path in enumerate(dir_list):
            try:
                print(f"Scanning file {i + 1}/{len(dir_list)}: {file_path}...")
                vIHash = self.binaryTreeSearch(
                    ioList, self.hashToFullNum(self.sha256_hash(file_path)))

                if vIHash:
                    print(f"File {file_path} is infected.")
                    self.virusHashCyPy.append(vIHash)
                    self.virusPath.append(file_path)
                else:
                    print(f"File {file_path} is clean.")

            except Exception as e:
                print(f"Error scanning file {file_path}: {e}")

        return self.virusHashCyPy, self.virusPath

    def virusScannerMd5(self, path):
        self.virusPath = []
        self.virusHashCyPy = []

        ioList = []

        for i in self.hashList:
            ioList.append(self.hashToFullNum(i))

        ioList.sort()

        # Get the list of all files in directory tree at given path
        dir_list = list()
        for (dirpath, dirnames, filenames) in os.walk(path):
            dir_list += [os.path.join(dirpath, file) for file in filenames]

        print(f"\nScanning directory: {path}")
        for i, file_path in enumerate(dir_list):
            try:
                print(f"Scanning file {i + 1}/{len(dir_list)}: {file_path}...")
                vIHash = self.binaryTreeSearch(
                    ioList, self.hashToFullNum(self.Md5_hash(file_path)))

                if vIHash:
                    print(f"File {file_path} is infected.")
                    self.virusHashCyPy.append(vIHash)
                    self.virusPath.append(file_path)
                else:
                    print(f"File {file_path} is clean.")

            except Exception as e:
                print(f"Error scanning file {file_path}: {e}")

        return self.virusHashCyPy, self.virusPath


def scan_folder(folder_path):
    # Initialize the Engine with the desired hash type
    engine = Engine("md5")

    # Calculate hashes of all files in the directory
    file_hashes = engine.calculate_hashes(folder_path)
    print("\nHashes of Files:")
    for file_path, hashes in file_hashes.items():
        print(f"{file_path} => MD5: {hashes['md5']}, SHA256: {hashes['sha256']}")
    print("Started Comparing the hashes generated with the created database")
    # Perform scanning using the Engine
    virus_hashes, infected_files = engine.virusScannerMd5(folder_path)

    print("\nScan Results:")
    if infected_files:
        print(f"Infected Files in directory {folder_path}:")
        for file_info in infected_files:
            print(f"{file_info} is infected.")
    else:
        print(f"All files in directory {folder_path} are clean. No viruses found.")


if __name__ == "__main__":
    try:
        folder_path = input("Enter the full path of the directory to scan: ").strip()
        if not os.path.exists(folder_path):
            raise ValueError("Invalid directory path. Please provide a valid path.")
        
        start = time.time()

        scan_folder(folder_path)

        end = time.time()
        print(f"\nScanning completed in {end - start} seconds.")
    except Exception as e:
        print(f"Error: {e}")
