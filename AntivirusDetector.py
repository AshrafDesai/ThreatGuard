import sys
import subprocess
def check_antivirus():
    try:
        
        if 'win' in sys.platform:
            command = 'wmic /namespace:\\\\root\\SecurityCenter2 path AntiVirusProduct get displayName'
            output = subprocess.check_output(command, shell=True, text=True)
            antivirus_list = output.split('\n')[1:-1] 
            if antivirus_list:
                print("Installed antivirus software:")
                for antivirus in antivirus_list:
                    print(antivirus.strip())
            else:
                print("No antivirus software found.")
    except Exception as e:
        print("Error:", e)  
check_antivirus()  
