# WEB-APPLICATION
"NAME"        :  CHEBROLU LUCKKY SOWRAB
"CODE ID"     :  CT08DN1640
"COMPANY"     : CODTECT IT SOLUTIONS
"DURATION"    : 8WEEKS
"MENTOR"      : NEELA SANTOSH
#OUT PUT
[*] Detected 3 forms on http://testphp.vulnweb.com

[!] Possible SQL Injection detected on form #1 with payload: ' OR '1'='1
[!] Possible SQL Injection detected on form #1 with payload: '; DROP TABLE users; --
[!] Possible XSS vulnerability detected on form #2 with payload: <script>alert('XSS')</script>
[!] Possible XSS vulnerability detected on form #2 with payload: <img src=x onerror=alert('XSS')>
#
[*] Detected 2 forms on http://secure.example.com
(No alerts printed; site is likely secure against basic SQLi/XSS payloads)
