#yeah
""" 
Mr Shobadeh gar
"""

__author__ = "@Creator_Ryson"
__license__ = "GPLv3"
__version__ = "0.2"
__status__ = "being developed"

from time import time, sleep
from random import choice
from multiprocessing import Process

from utils import CheckPublicIP, IsProxyWorking
from utils import PrintStatus, PrintSuccess, PrintError
from utils import PrintBanner, GetInput, PrintFatalError
from utils import LoadUsers, LoadProxies, PrintChoices

from instaclient import InstaClient

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


if __name__ == "__main__":
    PrintBanner()
    PrintStatus("Loading users!")
    USERS = LoadUsers("./users.txt")
    PrintStatus("Loading Proxes!")
    PROXIES = LoadProxies("./proxy.txt")
    print("")

    username = GetInput("enter account username you want to complain :")
    userid = GetInput("number of report you want to complain :")
    useproxy = GetInput("Do you want to use proxy? [yes no]:")
    if (useproxy == "yes"):
        useproxy = True
    elif (useproxy == "no"):
        useproxy = False
    else:
        PrintFatalError("Please just enter 'yes' or 'no'!")
        exit(0)
    usemultithread = GetInput("Do you want to use multithreading? [Yes / No] (Do not use this feature if you have too many users or if your computer is slow!):")
    
    if (usemultithread == "yes"):
        usemultithread = True
    elif (usemultithread == "no"):
        usemultithread = False
    else:
        PrintFatalError("Please just enter 'Yes' or 'No'!")
        exit(0)
    
    PrintChoices()
    reasonid = GetInput("Please select one of the reasons for the above complaint (ex: 1 for spam):")

    
    
    
    print("")
    PrintStatus("Starting!")
    print("")

    if (usemultithread == False):
        NoMultiThread()
    else:
        for user in USERS:
            p = Process(target=MultiThread,
                args=(username,
                    userid,
                    user["user"],
                    user["password"],
                    None if useproxy == False else choice(PROXIES),
                    reasonid
                )
            )
            p.start() 
   

