# autoreconx.py

import os
import sys
import argparse

def run_subfinder(domain):
    print("[+] Running Subfinder...")
    os.system(f"subfinder -d {domain} -o subs.txt")

def run_httpx():
    print("[+] Checking Alive Domains...")
    os.system("httpx -l subs.txt -o alive.txt")

def run_nmap():
    print("[+] Running Nmap on Alive Hosts...")
    os.system("nmap -iL alive.txt -oN ports.txt")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--domain", help="Target domain", required=True)
    args = parser.parse_args()

    run_subfinder(args.domain)
    run_httpx()
    run_nmap()

    print("[✔] Scan complete! Results in subs.txt, alive.txt, and ports.txt")

if __name__ == "__main__":
    main()
