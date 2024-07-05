#!/usr/bin/python3
import os
import sys
import subprocess
import shutil
import time

def banner():
    print("+--------------------------------------------------------------------+")
    print("| ██████╗ ██████╗  ██████╗ ██╗  ██╗██╗   ██╗ █████╗  ██████╗███████╗ |")
    print("| ██╔══██╗██╔══██╗██╔═══██╗╚██╗██╔╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔════╝ |")
    print("| ██████╔╝██████╔╝██║   ██║ ╚███╔╝  ╚████╔╝ ███████║██║     █████╗   |")
    print("| ██╔═══╝ ██╔══██╗██║   ██║ ██╔██╗   ╚██╔╝  ██╔══██║██║     ██╔══╝   |")
    print("| ██║     ██║  ██║╚██████╔╝██╔╝ ██╗   ██║   ██║  ██║╚██████╗███████╗ |")
    print("| ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚══════╝ |")
    print("+--------------------------------------------------------------------+")

def install_python_package():
    print("[*] Installing Python package 'validproxy'...")
    result = subprocess.run(['pip', 'install', 'validproxy'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        print("[+] Python package 'validproxy' installed successfully.")
    else:
        print("[-] Failed to install Python package 'validproxy'.")
        sys.exit(1)
    time.sleep(3)
    os.system('cls')

def main():
    banner()
    time.sleep(1)

    if os.name == 'nt':
        install_python_package()
    else:
        print("This script is designed to run on Windows.")
        sys.exit()

if __name__ == "__main__":
    main()
    
