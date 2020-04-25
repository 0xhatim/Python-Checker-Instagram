import requests
import random
import secrets
import time
import threading
from queue import Queue
from termcolor import colored
from colorama import init
import os
init()
clear = lambda: os.system('cls')  # on Windows System
clear()

print("Checker Test v2")
proxies = []
USER_AGENTS = [
    ('Mozilla/5.0 (X11; Linux x86_64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/57.0.2987.110 '
     'Safari/537.36'),  # chrome
    ('Mozilla/5.0 (X11; Linux x86_64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/61.0.3163.79 '
     'Safari/537.36'),  # chrome
    ('Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) '
     'Gecko/20100101 '
     'Firefox/55.0'),  # firefox
    ('Mozilla/5.0 (X11; Linux x86_64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/61.0.3163.91 '
     'Safari/537.36'),  # chrome
    ('Mozilla/5.0 (X11; Linux x86_64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/62.0.3202.89 '
     'Safari/537.36'),  # chrome
    ('Mozilla/5.0 (X11; Linux x86_64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/63.0.3239.108 '
     'Safari/537.36'),  # chrome
]

global numberofthreads
counter = 0 
try:

    passw = str(input("password:"))
    youremail = str(input("email:"))
    youremail = youremail.split("@")
    newemail = youremail[0]+f"+{random.randint(0,100)}"+"@"+youremail[1]
    print("email will be like this ",newemail)
except Exception as e:
    print(e)
    input("")

url = "https://www.instagram.com/accounts/web_create_ajax/attempt/"
prx = open("proxy.txt","r").read().splitlines()
for i in prx:
    proxies.append(i)
urlreg =  "https://www.instagram.com/accounts/web_create_ajax/"

numberofthreads = int(input("threads:"))

timeout = int(input("Timeout 1-10:"))
def Checker():
    global counter 
    global q
    global email
    global urlreg
    global passw
    global newemail
    global url
    global timeout

    while True:
            
        try:
            
            

            r = requests.session()
            proxy = str(random.choice(proxies))
            NewProxies = {
                'http': 'http://{}'.format(proxy),
                'https': 'http://{}'.format(proxy)}
            r.proxies = NewProxies
            cookie = secrets.token_hex(8)*2
            usr = str(random.choice(usernameList))
            counter+=1

            head = {"method": "POST", "X-CSRFToken":"missing",
                    "Referer": "https://www.instagram.com/accounts/web_create_ajax/",
                    "X-Requested-With":"XMLHttpRequest",## Here
                    "path":"/accounts/web_create_ajax/",
                    "accept": "*/*", "ContentType": "application/x-www-form-urlencoded",
                    "mid":cookie,"csrftoken":"missing","rur":"FTW","user-agent":str(random.choice(USER_AGENTS))}
            data = {

                'email': newemail,
                'password': passw,
                "username": usr,
                "first_name": "Mexaw",
                "opt_into_one_tap": "false"
            }
            r.headers.update(head)
            s = r.post(urlreg, data=data ,timeout=timeout)

            text = str(s.text)
            if text.find("checkpoint") >=0:
                named_tuple = time.localtime()
                time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
                print(colored("Found Registry mexaw Reg @31421","white"))
                print(colored("Details","green"))
                print(f"""
username:{usr}
password:{passw}
email:{newemail}
cookies:{r.cookies.get_dict()}
time:{time_string}
                """)
                details = f"""\n
username:{usr}
password:{passw}
email:{youremail}
cookies:{r.cookies.get_dict()}
time:{time_string}\n
                """
                with open("found.txt",'a') as wr:
                    wr.write(details)
                    newemail = youremail[0]+f"+{random.randint(0,100)}"+"@"+youremail[1]
    
            if text.find("true") >=0:
                named_tuple = time.localtime()
                time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
# get struct_time

                print(colored("Found Registry mexaw Reg @31421","white"))
                print(colored("Details","green"))
                print(f"""
username:{usr}
password:{passw}
email:{youremail}
cookies:{r.cookies.get_dict()}
time:{time_string}
                """)
                details = f"""\n
username:{usr}
password:{passw}
email:{youremail}
cookies:{r.cookies.get_dict()}
time:{time_string}\n
                """
                with open("found.txt",'a') as wr:
                    wr.write(details)
                    newemail = youremail[0]+f"+{random.randint(0,100)}"+"@"+youremail[1]

            print(colored("[+]attempt:{}[+]".format(counter) ,"red"),end="\r")
   
        except Exception as e:
            print(e)
            
            
            
usernameList = []

s = open("username.txt", "r").read().splitlines()
for i in s:
    if i =="":
        continue
    usernameList.append(i)
    
    







threads = [] 
for i in range(numberofthreads):
    t = threading.Thread(target=Checker)
    t.start()
    threads.append(t)


for i in threads:
    i.join()

