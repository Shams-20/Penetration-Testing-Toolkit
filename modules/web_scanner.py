import requests
from bs4 import BeautifulSoup

def scan_website(target_url):
    print(f"\n[+] Scanning {target_url} for vulnerabilities...\n")

    try:
        response = requests.get(target_url, timeout=3)
    except Exception as e:
        print(f"[-] Failed to connect: {e}")
        return

    if response.status_code != 200:
        print(f"[-] Got status code {response.status_code}, might not be accessible")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    forms = soup.find_all("form")

    if not forms:
        print("[-] No forms found on this page.")
        return

    print(f"[+] Found {len(forms)} form(s). Checking for common vulnerabilities...\n")

    for i, form in enumerate(forms, start=1):
        action = form.get("action")
        method = form.get("method", "get").upper()
        print(f"Form #{i} | Method: {method} | Action: {action}")

        # Quick and dirty test payloads
        test_payloads = {
            "xss": "<script>alert(1)</script>",
            "sqli": "' OR '1'='1"
        }

        for vuln, payload in test_payloads.items():
            if method == "GET":
                target = target_url + "?" + f"test={payload}"
                r = requests.get(target)
            else:
                r = requests.post(target_url, data={"test": payload})

            if payload in r.text:
                print(f"[!!] Possible {vuln.upper()} vulnerability detected with payload: {payload}")

    print("\n[+] Scan complete!")