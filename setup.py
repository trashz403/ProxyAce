#!/usr/bin/python3
import os
import sys
import subprocess
import shutil
import time

GREEN = '\033[1;32m'
RED = '\033[1;31m'
WHITE = '\033[1;37m'
CYAN = '\033[0;36m'
RESET = '\033[0m'

def banner():
    print(f"{WHITE}+--------------------------------------------------------------------+")
    print(f"{WHITE}| {GREEN}██████╗ ██████╗  ██████╗ ██╗  ██╗██╗   ██╗ █████╗  ██████╗███████╗ {WHITE}|")
    print(f"{WHITE}|{GREEN} ██╔══██╗██╔══██╗██╔═══██╗╚██╗██╔╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔════╝ {WHITE}|")
    print(f"{WHITE}|{GREEN} ██████╔╝██████╔╝██║   ██║ ╚███╔╝  ╚████╔╝ ███████║██║     █████╗   {WHITE}|")
    print(f"{WHITE}|{GREEN} ██╔═══╝ ██╔══██╗██║   ██║ ██╔██╗   ╚██╔╝  ██╔══██║██║     ██╔══╝   {WHITE}|")
    print(f"{WHITE}|{GREEN} ██║     ██║  ██║╚██████╔╝██╔╝ ██╗   ██║   ██║  ██║╚██████╗███████╗ {WHITE}|")
    print(f"{WHITE}|{GREEN} ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚══════╝ {WHITE}|")
    print(f"{WHITE}+--------------------------------------------------------------------+{RESET}")

def require_root():
    if os.geteuid() != 0:
        print(f"{RED}This script must be run as root. Please use sudo or log in as root.{RESET}")
        sys.exit(1)

def install_python_package():
    print(f"{WHITE}[{CYAN}*{WHITE}] {CYAN}Installing Python package 'validproxy'...{RESET}")
    result = subprocess.run(['pip', 'install', 'validproxy'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        print(f"{WHITE}[{GREEN}+{WHITE}] {GREEN}Python package 'validproxy' installed successfully.{RESET}")
    else:
        print(f"{WHITE}[{RED}-{WHITE}] {RED}Failed to install Python package 'validproxy'.{RESET}")
        sys.exit(1)
    time.sleep(3)
    os.system('clear')

def termux_setup():
    install_python_package()
    shutil.copytree('proxyace', '/data/data/com.termux/files/usr/bin/', dirs_exist_ok=True)
    os.chmod('/data/data/com.termux/files/usr/bin/proxyace', 0o755)
    if shutil.which('proxyace'):
        print(f"{WHITE}[{GREEN}+{WHITE}] {GREEN}Proxyace installed successfully in Termux.{RESET}")
    else:
        print(f"{WHITE}[{RED}-{WHITE}] {RED}Proxyace installation failed in Termux.{RESET}")

def linux_setup():
    install_python_package()
    shutil.copytree('proxyace', '/usr/bin/', dirs_exist_ok=True)
    os.chmod('/usr/bin/proxyace', 0o755)
    if shutil.which('proxyace'):
        print(f"{WHITE}[{GREEN}+{WHITE}] {GREEN}Proxyace installed successfully on Linux.{RESET}")
    else:
        print(f"{WHITE}[{RED}-{WHITE}] {RED}Proxyace installation failed on Linux.{RESET}")

def main():
    banner()
    time.sleep(1)
    require_root()

    if os.path.isdir('/usr/bin'):
        linux_setup()
    elif os.path.isdir('/data/data/com.termux/files/home'):
        termux_setup()
    else:
        install_python_package()
        sys.exit()

    if shutil.which('proxyace'):
        print(f"{WHITE}[{GREEN}+{WHITE}] {GREEN}Installation successful.{RESET}")
    else:
        print(f"{WHITE}[{RED}-{WHITE}] {RED}Installation not completed.{RESET}")

if __name__ == "__main__":
    main()
    
