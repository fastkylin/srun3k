#!/usr/bin/python3.6
################################################################
#                                                              #
#                fileExist Python Script                       #
#          Fastkylin 2018年 12月 03日 星期一 00:02:04 CST      #
#                                Linux Ubuntu 18.04            #
#                                                              #
################################################################
import os
import public

def config():
    #_user="123456789"
    #_password="123456789"
    print("Inuput user: ")
    _user=input("in< ")
    print("Input password: ")
    _password=input("in< ")
    f=open("config/config.data","w")
    u=public.encryptData.encryptuser(_user)
    p=public.encryptData.encryptpassword(_password)
    print(u)
    f.write(u+"\n"+p)
    f.close()

