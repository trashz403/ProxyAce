# ProxyAce

## Overview

ProxyAce is a Python tool designed to validate and manage proxy lists efficiently. It reads a list of proxies from a file, checks their validity, and saves the valid proxies to a specified output file.

## Features

- **Proxy Validation:** Verify the functionality of proxies sourced from a file.
- **Interactive Mode:** Input proxy list and output file paths interactively.
- **Flexible Usage:** Command-line arguments for easy integration into scripts.
- **Simple Integration:** Intuitive and straightforward to use.

## Installation

```bash
git clone https://github.com/trashz403/ProxyAce
```

```bash
cd ProxyAce
```

```bash
bash setup.sh
```

```bash
proxyace --main
```

or 

```bash
proxyace --proxy-list proxy-list.txt --valid-proxy proxy-list.txt
```

### Command-Line Arguments

- `--proxy-list` : Path to the file containing the list of proxies.
- `--valid-proxy` : Path to save valid proxies (defaults to `valid_proxies.txt` if not specified).
- `--main` : Interactive mode to prompt for file paths.

### Thanks and Responsibility

- Thank you for using ProxyAce! This tool was developed with the aim of simplifying proxy management and enhancing your workflow. As a user, you are responsible for ensuring the lawful and ethical use of proxies as per your local regulations and policies. Use ProxyAce responsibly and respect the terms of service of proxy providers and internet services you interact with.

Your support and feedback are greatly appreciated and help improve ProxyAce for everyone. Happy proxy managing!
