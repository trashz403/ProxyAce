#!/usr/bin/bash

green='\033[1;32m'
red='\033[1;31m'
white='\033[1;37m'
cyan='\033[0;36m'
reset='\033[0m'

banner() {
  echo -e "${white}+--------------------------------------------------------------------+"
  echo -e "${white}| ${green}██████╗ ██████╗  ██████╗ ██╗  ██╗██╗   ██╗ █████╗  ██████╗███████╗ ${white}|"
  echo -e "${white}|${green} ██╔══██╗██╔══██╗██╔═══██╗╚██╗██╔╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔════╝ ${white}|"
  echo -e "${white}|${green} ██████╔╝██████╔╝██║   ██║ ╚███╔╝  ╚████╔╝ ███████║██║     █████╗   ${white}|"
  echo -e "${white}|${green} ██╔═══╝ ██╔══██╗██║   ██║ ██╔██╗   ╚██╔╝  ██╔══██║██║     ██╔══╝   ${white}|"
  echo -e "${white}|${green} ██║     ██║  ██║╚██████╔╝██╔╝ ██╗   ██║   ██║  ██║╚██████╗███████╗ ${white}|"
  echo -e "${white}|${green} ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚══════╝ ${white}|"
  echo -e "${white}+--------------------------------------------------------------------+${reset}"
}

require_root() {
  if [[ -d /usr/bin ]]; then
    if [[ $EUID -ne 0 ]]; then
      echo -e "${red}This script must be run as root. Please use sudo or log in as root.${reset}"
      exit 1
    fi
  fi
}

termux_setup() {
  cp -r proxyace /data/data/com.termux/files/usr/bin/
  chmod +x /data/data/com.termux/files/usr/bin/proxyace
  if command -v proxyace > /dev/null; then
    echo -e "${white}[${green}+${white}] ${green}Proxyace installed successfully in Termux.${reset}"
  else
    echo -e "${white}[${red}-${white}] ${red}Proxyace installation failed in Termux.${reset}"
  fi
}

linux_setup() {
  cp -r proxyace /usr/bin/
  chmod +x /usr/bin/proxyace
  if command -v proxyace > /dev/null; then
    echo -e "${white}[${green}+${white}] ${green}Proxyace installed successfully on Linux.${reset}"
  else
    echo -e "${white}[${red}-${white}] ${red}Proxyace installation failed on Linux.${reset}"
  fi
}

main() {
  banner
  sleep 1
  require_root

  if [[ -d /usr/bin ]]; then
    linux_setup
  else
    termux_setup
  fi

  if command -v proxyace > /dev/null; then
    echo -e "${white}[${green}+${white}] ${green}Installation successful.${reset}"
  else
    echo -e "${white}[${red}-${white}] ${red}Installation not completed.${reset}"
  fi
}

main
