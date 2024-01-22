<<<<<<< HEAD
from hashlib import sha256, md5
import time
import os

start = time.time()

class Engine:
    def __init__(self, typeH):
        base_path = "DataBase/HashDataBase"
        if typeH.lower() == "sha256":
            with open(os.path.join(base_path, "Sha256/virusHash.unibit"), "r") as i:
                self.hashList = i.readlines()

        if typeH.lower() == "md5":
            with open(os.path.join(base_path, "Md5/md5HashOfVirus.unibit"), "r") as i:
                self.hashList = i.readlines()

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

    def virusScannerSha256(self, path):
        import os

        self.virusPath = []
        self.virusHashCyPy = []

        ioList = []

        for i in self.hashList:
            ioList.append(self.hashToFullNum(i))

        ioList.sort()

        dir_list = list()
        for (dirpath, dirnames, filenames) in os.walk(path):
            dir_list += [os.path.join(dirpath, file) for file in filenames]

        for i in dir_list:
            try:
                vIHash = self.binaryTreeSearch(
                    ioList, self.hashToFullNum(self.sha256_hash(i)))
                print(i)
                if vIHash:
                    self.virusHashCyPy.append(vIHash)
                    self.virusPath.append(i)

            except:
                pass

        return self.virusHashCyPy, self.virusPath

    def virusScannerMd5(self, path):
        import os

        self.virusPath = []
        self.virusHashCyPy = []

        ioList = []

        for i in self.hashList:
            ioList.append(self.hashToFullNum(i))

        ioList.sort()

        dir_list = list()
        for (dirpath, dirnames, filenames) in os.walk(path):
            dir_list += [os.path.join(dirpath, file) for file in filenames]

        for i in dir_list:
            try:
                vIHash = self.binaryTreeSearch(
                    ioList, self.hashToFullNum(self.Md5_hash(i)))
                print(i)
                if vIHash:
                    self.virusHashCyPy.append(vIHash)
                    self.virusPath.append(i)

            except:
                pass

        return self.virusHashCyPy, self.virusPath

    def CacheFileRemover(self):
        temp_list = list()

        username = os.environ.get('USERNAME').upper().split(" ")

        for (dirpath, dirnames, filenames) in os.walk("/tmp"):
            temp_list += [os.path.join(dirpath, file) for file in filenames]
            temp_list += [os.path.join(dirpath, file) for file in dirnames]

        for (dirpath, dirnames, filenames) in os.walk("/var/tmp"):
            temp_list += [os.path.join(dirpath, file) for file in filenames]
            temp_list += [os.path.join(dirpath, file) for file in dirnames]

        for (dirpath, dirnames, filenames) in os.walk("/var/cache"):
            temp_list += [os.path.join(dirpath, file) for file in filenames]
            temp_list += [os.path.join(dirpath, file) for file in dirnames]

        if temp_list:
            for i in temp_list:
                print(i)

                try:
                    os.remove(i)
                except:
                    pass

                try:
                    os.rmdir(i)
                except:
                    pass
        else:
            return 0

    def ramBooster(self):
        pass

    def FlowDetectorIo(self, path, bit_size):
        with open("DataBase/Flow Detection/flow_exe.unibit", "r") as rFile:
            io = rFile.readlines()
            rFile.close()

        with open(path, "rb") as rFile:
            nj = list(rFile.read())
            rFile.close()

        njStr = ''

        for i in nj:
            njStr += str(i)

        bX = 0

        for f in io:
            for i in range(0, len(f), bit_size):
                if njStr.find(f[i:i+bit_size]) != -1:
                    bX += 1

            if flen := len(f)/bit_size:
                prLen = (bX/flen)*100

        return prLen


io = Engine("md5")

end = time.time()
print(end - start)
=======
import os
import hashlib
import time

class Engine:
    def __init__(self, typeH):
        base_path = "DataBase/HashDataBase"
        
        if typeH.lower() == "md5":
            with open(os.path.join(base_path, "Md5/md5HashOfVirus.unibit"), "r") as i:
                self.hashList = i.readlines()

    def hashToFullNum(self, hash):
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        alphaNum = {char: str(index + 1) for index, char in enumerate(alpha)}

        j = ''.join(alphaNum.get(char, char) for char in hash.lower())
        return int(j)

    def binaryTreeSearch(self, hList, valueToFind):
        initialValue = 0
        lengthOfList = len(hList) - 1
        pointFound = 0

        while initialValue < lengthOfList and pointFound == 0:
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

    def md5_hash(self, filename):
        try:
            with open(filename, "rb") as f:
                bytes_content = f.read()
                md5_hash = hashlib.md5(bytes_content).hexdigest()
            return md5_hash
        except:
            return 0

    def virusScannerMd5(self, path):
        self.virusPath = []
        self.virusHashCyPy = []

        ioList = [self.hashToFullNum(i) for i in self.hashList]
        ioList.sort()

        dir_list = [os.path.join(dirpath, file) for (dirpath, _, filenames) in os.walk(path) for file in filenames]

        print("Scanned Files:")
        for i in dir_list:
            try:
                vIHash = self.binaryTreeSearch(ioList, self.hashToFullNum(self.md5_hash(i)))
                print(i)
                if vIHash:
                    self.virusHashCyPy.append(vIHash)
                    self.virusPath.append(i)
            except:
                pass

        print("Generated Hashes:")
        print(self.virusHashCyPy)

        if not self.virusPath:
            print("Scan Completed. No virus found.")

        return self.virusHashCyPy, self.virusPath

    def cacheFileRemover(self):
        temp_list = list()

        username = os.environ.get('USER').upper().split(" ")

        for directory in ["/tmp", "/var/tmp", "/var/cache"]:
            for (dirpath, dirnames, filenames) in os.walk(directory):
                temp_list += [os.path.join(dirpath, file) for file in filenames]
                temp_list += [os.path.join(dirpath, file) for file in dirnames]

        if temp_list:
            print("\nRemoved Files:")
            for i in temp_list:
                print(i)

                try:
                    os.remove(i)
                except:
                    pass

                try:
                    os.rmdir(i)
                except:
                    pass
        else:
            print("\nNo temporary files to remove.")

    def ramBooster(self):
        pass

    def flowDetectorIo(self, path, bit_size):
        with open("DataBase/Flow Detection/flow_exe.unibit", "r") as rFile:
            io = rFile.readlines()

        with open(path, "rb") as rFile:
            nj = list(rFile.read())

        njStr = ''.join(str(i) for i in nj)

        bX = 0

        for f in io:
            for i in range(0, len(f), bit_size):
                if njStr.find(f[i:i+bit_size]) != -1:
                    bX += 1

            if flen := len(f) / bit_size:
                prLen = (bX / flen) * 100

        return prLen


def main():
    start = time.time()

    io = Engine("md5")

    # Perform your operations here
    print("\nCache File Remover:")
    io.cacheFileRemover()

    # For example, run the virus scanner on a specific path
    path_to_scan = "/home/ashraf/Ashraf/Bit-Link-Python-Antivirus/"
    print("\nVirus Scanner (MD5):")
    io.virusScannerMd5(path_to_scan)

    end = time.time()
    print("\nTotal Time Taken:", end - start, "seconds")


if __name__ == "__main__":
    main()
>>>>>>> 22a2ff38f7097ebcbe36476aee53845a22e6fc52
