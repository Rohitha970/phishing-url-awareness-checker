

##  Test Results ##

Python version used: Python 3.12.4   |   Operating system: Windows   |   Date: 28/10/2026

| # | Input | Expected result | Actual result | Pass/Fail |
|---|-------|-----------------|---------------|-----------|
| 1 | https://www.example.com/login | No listed warning signs |  No listed warning signs found. This does NOT prove safety.|Pass|

| 2 | http://192.0.2.10/account | IP address + HTTP |  Uses an IP address instead of a familiar domain, Uses HTTP. HTTPS alone does not prove trust. | Pass|
| 3 | http://example.com@sample.invalid/login | @ symbol + HTTP | Contains an @ symbol; inspect carefully,Uses HTTP. HTTPS alone does not prove trust.| Pass|
| 4 | https://a.b.c.d.e.example.invalid/path | Many hostname segments | Contains many hostname segments/subdomains.| Pass |
| 5 | https://xn--example.invalid/ | Punycode-style hostname | Contains a punycode-style hostname.| Pass |

## Notes ## 
All five test cases produced the expected warning messages, so they passed the tests. I learned how Python can check URL text for potential phishing warning signs, including suspicious symbols, IP addresses, multiple hostname segments, punycode markers, and HTTP usage. However, these checks cannot guarantee whether a website is safe or malicious.

## Conclusion ##

The testing demonstrates that the Phishing URL Awareness Checker identifies the selected warning signs in the sample URLs as expected. It is an educational tool for cybersecurity awareness and does not replace a complete security analysis.