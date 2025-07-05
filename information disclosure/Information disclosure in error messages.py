import requests
import re


# Disable certificate warning
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

url = "https://0a2c00870337b13082b2abee0049004d.web-security-academy.net/"  #change to lab URL

def findversion(url):
    final_url = url + "product?productId=test"
    r = requests.get(final_url,verify=False)
    match = re.search(r'Apache Struts (.+)',r.text)
    name = match.group(1)
    return name

def submitsolution(url,version):
    final_url = url + "submitSolution"
    data = {"answer":version}
    r = requests.post(final_url, data=data,verify=False)
    print(r.text)

version = findversion(url)
print(version)
submitsolution(url,version)