# !/usr/bin/python
# the reporter
# ------ json payload , mian file compiled ------
'''Mr Shobadeh Gar'''

__author__ = "@Creator_Ryson"
__license__ = "mr"
__version__ = "0.2"
__status__ = "mr shobadehgar"
from colorama import Fore
import time
from random import choice
from multiprocessing import Process

from utils import CheckPublicIP, IsProxyWorking
from utils import PrintStatus, PrintSuccess, PrintError
from utils import PrintBanner, GetInput, PrintFatalError
from utils import LoadUsers, LoadProxies, PrintChoices

from instaclient import InstaClient
import time
import sys , os , pyuseragents , requests
USERS = []
PROXIES = []

def MultiThread(username, userid, loginuser, loginpass, proxy, reasonid):
    client = None
    if (proxy != None):
        PrintStatus("[" + loginuser + "]", "Logging into the Account!")
        client = InstaClient(
            loginuser,
            loginpass,
            proxy["ip"],
            proxy["port"]
        )
    else:
        PrintStatus("[" + loginuser + "]", "Logging into the Account!")
        client = InstaClient(
            loginuser,
            loginpass,
            None,
            None
        )
        
    client.Connect()
    client.Login()
    client.Spam(userid, username, reasonid)
    print("")

def NoMultiThread():
    for user in USERS:
        client = None
        if (useproxy):
            proxy = choice(PROXIES)
            PrintStatus("[" + user["user"] + "]", "Logging into the Account!")
            client = InstaClient(
                user["user"],
                user["password"],
                proxy["ip"],
                proxy["port"]
            )
        else:
            proxy = choice(PROXIES)
            PrintStatus("[" + user["user"] + "]", "Logging into the Account!")
            client = InstaClient(
                user["user"],
                user["password"],
                None,
                None
            )
        
        client.Connect()
        client.Login()
        client.Spam(userid, username, reasonid)
        print("")

mr = """\033[93m


                 .xUHWH!! !!?RYSONN:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRMMDM!
              ~?WuxiW*   "#$$$$8!!!!??!!!     
             :X- M$$$$       "T#$T~!8$WUXU~
             :%  ~#$$$m:        ~!~ ?$$$$$$
          :!.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:< !    ~?T#$$@@W@*?$$      /
W$@@M!!! .!~~ !!     .:XUW$W!~ "~:    :
#"~~.:x%!!  !H:   !WM$$$$Ti.: .!WUn+!
:::~:!!:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$!          
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!          
$R@i.~~ !     :   ~$$$$$B$$en:`            
?MXT@Wx.~    :     ~"##*$$$$M~
\033[92m

[ reporter rubika version 1.0 ]
\033[36m

<https://rubika.ir/caetorr>
"""
if __name__ == "__main__":
    print(mr)
    time.sleep(1)
    PrintStatus("\n\033[31m\nLoading users!\n")
    USERS = LoadUsers("./users.txt")
    time.sleep(1)
    PrintStatus("\n\033[35mLoading Proxes!\n")
    PROXIES = LoadProxies("./proxy.txt")
    print("")
    time.sleep(2)
    username = GetInput("\n\033[32menter account username you want to complain >>> \033[20;37m")
    time.sleep(1)
    userid = GetInput("\n\033[35mnumber of report you want to complain >>> \033[20;37m")
    time.sleep(1)
    useproxy = GetInput("\ndo you want to use proxy? [yes no] >>> \033[20;37m")
    if (useproxy == "yes".lower()):
        useproxy = True
    elif (useproxy == "no".lower()):
        useproxy = False
    else:
        PrintFatalError("\nPlease just enter 'yes' or 'no'!")
        exit(0)
    time.sleep(1)
    usemultithread = GetInput("\033[31m\ndo you want to use multithreading? [Yes / No] (do not use this feature if you have too many users or if your computer is slow! >>> ")
    
    if (usemultithread == "yes".lower()):
        usemultithread = True
    elif (usemultithread == "no".lower()):
        usemultithread = False
    else:
        time.sleep(1)
        PrintFatalError("Please just enter 'Yes' or 'No'!")
        exit(0)
    
    PrintChoices()
    time.sleep(1)
    reasonid = GetInput("\nPlease select one of the reasons for the above complaint (ex: 1 for spam) >>> ")

    print (f'\n\033[20;37mstarting [reporter] | target: @{username}\n')
    userid1 = 0
    while userid != userid1:
        time.sleep(1)
        print ()
        data = ('`\M3gt6HHdtuTe\REPORT\`')
        json = {"api_version":"5","method":"messenger","data":{"id":f"{username}","send_type":"REPORT"}}
        headers = {'Host': 'https://messenger817.iranlms.ir/','content-length': '96','accept': 'application/json, text/plain, */*','user-agent': pyuseragents.random(),'content-type': 'text/plain','origin': 'https://web.rubika.ir/','sec-fetch-site':'cross-site','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://web.rubika.ir/','accept-encoding': 'gzip, deflate, br','accept-language': 'fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6','content-length':'143'}
        try:
            requests.post('https://messenger817.iranlms.ir/',headers=headers,json=json,data=data)
            time.sleep(6.5)
            print (f'\n\033[92m[SENDED] ~> \033[93m|SPAM| TARGET ~> \033[20;37m@{username}\033[00;00m\033[00m\n')
        except:
            time.sleep(1)
            print ('\n\033[20;37m[N0T SPAM] :(')
            pass
        try:
            time.sleep(6.5)
            PrintStatus(f"\n\033[92m[SENDED] ~> \033[93m|SPAM| TARGET ~> \033[20;37m @{username}\033[00;00m\033[00m\n")
        except:
            time.sleep(1)
            print ('\n\033[20;37m[NOT SPAM] :(')

        if (usemultithread == False):
            time.sleep(1)
            print ()
            print (Fore.BLUE+'')
            NoMultiThread()
        else:
            for user in USERS:
                time.sleep(1)
                print ()
                p = Process(target=MultiThread,
                    args=(username,
                        userid,
                        user["user"],
                        user["password"],
                        None if useproxy == False else choice(PROXIES),
                       reasonid
                    )
                )
                time.sleep(1)
                print (Fore.BLUE+'')
                p.start()
        userid1 = (userid1-1)
   

lab = input("yeah okey or no bad |y/n| ")
if lab == "y":
    time.sleep(1)
    print (" oh thanks -mmd")
if lab == "n":
    me = input(""" sorry you error proxy or other (VPN)
restart ok-? (y/n)""")
if me == "y":
    print ("OK")
    os.syatem("python report.py")
if me == "n":
    print ("OK")
    sys.exit

os.system("exit")
