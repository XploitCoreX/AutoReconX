# AutoReconX
Automated subdomain , alive host , and port scanner tool
# 💀 AutoReconX

A simple recon automation tool built by **XploitCoreX**

## 🚀 Features:
- 🔍 Subdomain Enumeration (via subfinder)
- 🌐 Alive Host Checking (via httpx)
- 🔎 Port Scanning (via nmap)

## 📦 Installation (Linux/Kali/Ubuntu)

Follow these steps to install all dependencies:

```bash
# Install required packages
sudo apt update
sudo apt install git python3 python3-pip nmap golang -y

# Set Go path (if not already)
echo 'export PATH=$PATH:$(go env GOPATH)/bin' >> ~/.bashrc
source ~/.bashrc

# Install subfinder
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest

# Install httpx
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
git clone https://github.com/XploitCoreX/AutoReconX.git
cd AutoReconX
python3 autoreconx.py -d example.com
python3 autoreconx.py -d google.com
