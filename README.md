# 🛠️ Penetration Testing Toolkit

A modular Python-based penetration testing toolkit with multiple attack surfaces.  
Currently includes:

- **Port Scanner** → Scans top ports on a target system  
- **Brute-Forcer** → SSH brute force with wordlist support  
- **Web Scanner** → Crawls pages & tests forms for common vulnerabilities (SQLi/XSS)



## 📂 Project Structure

Penetration-Testing-Toolkit/
├─ main.py                # Menu to run modules
├─ modules/
│   ├─ port_scanner.py    # Port scanning logic
│   ├─ brute_forcer.py    # SSH brute-forcing logic
│   └─ web_scanner.py     # Web vulnerability scanning logic
├─ utils/
│   ├─ __init__.py
│   └─ helper_funcs.py    # Shared functions (e.g., IP validation)
├─ wordlist.txt           # Password wordlist for brute-forcer
└─ README.md              # This file




## 🚀 Usage

### 1. Run Toolkit
python3 main.py

### 2. Main Menu
=== PENETRATION TESTING TOOLKIT ===
1. Port Scanner
2. Brute-Forcer
3. Web Scanner
4. Exit



## 🔍 Modules

### Port Scanner
- Scans top ports on a given IP  
- Example:
Enter target IP: 8.8.8.8
[+] Port 53 is OPEN
[+] Port 443 is OPEN



### Brute-Forcer
- SSH brute force using **paramiko**  
- Supports custom wordlists  
- Example:
Enter target IP: 192.168.195.128
Enter target port: 22
Enter path to wordlist: wordlist.txt
Enter username to brute-force: kali
[-] Tried kali:1234 ❌
[-] Tried kali:toor ❌
[+] Found credentials: kali:kali

💡 *Wordlist should be a text file with one password per line. Example:*
1234
password
toor
kali



### Web Scanner
- Crawls forms on target web pages  
- Tests inputs for **SQL Injection** and **XSS**  
- Example target: local vulnerable page
python3 -m http.server 8000






## ⚠️ Disclaimer
This toolkit is for **educational purposes only**.  
Do **NOT** use against systems you don’t own or have explicit permission to test.  
The author is not responsible for misuse.  



## 🧩 Next Steps
- Add logging system  
- Add more brute-force services (FTP, HTTP auth)  
- Expand web scanner with more payloads
