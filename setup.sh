#!/usr/bin/bash

banner() 
{
  echo -e '{white}+--------------------------------------------------------------------+'
  echo -e '{white}| {green}██████╗ ██████╗  ██████╗ ██╗  ██╗██╗   ██╗ █████╗  ██████╗███████╗ {white}|'
  echo -e '{white}|{green} ██╔══██╗██╔══██╗██╔═══██╗╚██╗██╔╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔════╝ {white}|'
  echo -e '{white}|{green} ██████╔╝██████╔╝██║   ██║ ╚███╔╝  ╚████╔╝ ███████║██║     █████╗   {white}|'
  echo -e '{white}|{green} ██╔═══╝ ██╔══██╗██║   ██║ ██╔██╗   ╚██╔╝  ██╔══██║██║     ██╔══╝   {white}|'
  echo -e '{white}|{green} ██║     ██║  ██║╚██████╔╝██╔╝ ██╗   ██║   ██║  ██║╚██████╗███████╗ {white}|'
  echo -e '{white}|{green} ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚══════╝ {white}|'
  echo -e '{white}+--------------------------------------------------------------------+{reset}'
}

if [[ -d /usr/bin ]]; then
  if [ $(id -u) -ne 0 ]; then
    echo "This script must be ran as root"
  fi
fi

termux_app()
{
  cp -r proxyace /data/data/com.termux/files/usr/bin/
  chmod +x /data/data/com.termux/files/usr/bin/proxyace
  if [[ $(command -v proxyace) ]]; then
    echo ''
  else
    echo ''
  fi
}

linux_setup()
{
  cp -r proxyace /usr/bin/
  chmod +x /usr/bin/proxyace
  if [[ $(command -v proxyace) ]]; then
    echo ''
  else
    echo ''
  fi
}

main()
{
  banner
  sleep 3
  if [[ -d /usr/bin ]]; then
    linux_setup
  else
    termux_app
  fi
}
