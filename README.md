# 💀 AutoReconX

A powerful automated recon tool built by **XploitCoreX** for subdomain enumeration, alive host checking, and port scanning.

---

## 🚀 Features

- 🔍 Subdomain Enumeration (via [Subfinder](https://github.com/projectdiscovery/subfinder))
- 🌐 Alive Host Checking (via [httpx](https://github.com/projectdiscovery/httpx))
- 🔎 Port Scanning (via Nmap)
- 📂 Clean and simple output files
- 🧠 Beginner-friendly CLI usage

---

## 🧰 Installation (Tested on Kali/Ubuntu)

### 🔹 Step 1: Install Required Packages

```bash
sudo apt update
sudo apt install git python3 python3-pip nmap golang -y
```
---

 ### 🧰 Step 2: Install required packages


```
sudo apt install git python3 python3-pip nmap golang -y
```
---

### 🧾 Step 3: Set Go PATH

```
echo 'export PATH=$PATH:$(go env GOPATH)/bin' >> ~/.bashrc
source ~/.bashrc
```
---

### 🔍 Step 4: Install Subfinder

```
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
```
---

### 🌐 Step 5: Install httpx

```
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
```
---

### 📦 Step 6: Clone the tool

```
git clone https://github.com/XploitCoreX/AutoReconX.git
```
```
cd AutoReconX
```
---
### 🚀 Step 7: Run the tool

```
python3 autoreconx.py -d example.com
```
---

### 🧪 Example:

```
python3 autoreconx.py -d google.com
```


---

## 🧠 Why Use AutoReconX?

✔️ Beginner friendly & terminal based  
✔️ Fast recon with Subfinder, httpx, Nmap  
✔️ Perfect for CTFs, Pentesters, and Bug Bounty hunters  
✔️ Clean output files and simple usage  

---

## 🔧 Upcoming Features

- [ ] OSINT integration (Shodan, whois)
- [ ] Subdomain takeover checks
- [ ] Report generation (PDF)
- [ ] More automation modules

---

## 🙏 Like this tool?

📌 Star this repo  
📌 Follow [XploitCoreX](https://github.com/XploitCoreX)  
📌 Share it with your hacker squad 💀

---

## 📜 License

MIT License — Free to use, modify, and distribute.

