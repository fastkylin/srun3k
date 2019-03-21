#!/usr/bin/python3.6
################################################################################
#                                                                              #
#                         Haut Login Python Script                             #
#                         Fastkylin   Mon Set 26 2018                          #
#                         Ubuntu linux 18.04                                   #
#                                                                              #
################################################################################

from urllib import parse,request
import public
import os
from urllib.request import urlopen
data=""
_user=""
_ac_id=2 #  1 or 2
_mac="00-01-6C-06-A6-29" #a mac address you like
_type=2
_password=""
_action=""  #include logout  login
hosturl="http://172.16.154.130:69/cgi-bin/srun_portal" #you can define url here


def defdata(user,password,action,acid):
    global data
    if ( action == "login" ):
        print ("action = login")
        data={
                "action":action,
                "username":"{SRUN3}\r\n"+user,
                "password":password,
                "ac_id":acid,
                "drop":"0",
                "pop":"1",
                "type":10,
                "n":"117",
                "mbytes":"0",
                "minutes":"0"}
    elif ( action=="logout" ):
        print("action = logout")
        data={'username':user,
                'action':"logout",
                'type':"2",
                'mac':_mac,
                }
    else:
        print("log> defdata action error!")
        data="error"
    #print(data)      
    return data

def postaction(data):
    data = parse.urlencode(data).encode('utf-8')
    req = request.Request(hosturl,data)
    re  = urlopen(req)
    a=re.read().decode()
    print(a)
    return a


def config():
    class userdata:
        u=""
        p=""
    configpath="config/config.data"
    if(public.file.isFileExist(configpath)):
        out=public.file.getFileContent(configpath)
        o=list(out)
        a=""
        for i in range(0,len(out)):
            if(o[i] != "\n" ):
                a=a+o[i]
            else:
                break
        userdata.u=a
        userdata.p=out[len(a)+1:]
        return userdata
    else:
        public.setup.config()
        config()
def resinfo(u,p,action):
    acid=2
    response=postaction(defdata(u,p,action,acid))
    if ('ip_already_online_error' == response):
        print("out> online")
    elif (response.find("login_ok")>=0):
        print("out> login ok!!")
    elif ('logout_ok' == response):
        print("out> logout ok!!")
    elif('login_error#You are not online.' == response):
        print("ou> offline")
    elif('login_error#INFO failed, BAS respond timeout.' == response):
        print("out> try to change acid")
        if(acid==1):
            acid=2
        else:
            acid=1
        response=postaction(defdata(u,p,action,acid))
        resinfo(u,p,action)
    else:
        print("log> response error!!")


def main():
    d=config()
    print("out> choose a action\nlogin: 1\nlogout: 2")
    action=input("In< ")
    if('1'==action):
        action="login"
    elif('2'==action):
        action="logout"
    else:
        print("out> error! try again please")
        main()
    resinfo(d.u,d.p,action)
    
    



main()



