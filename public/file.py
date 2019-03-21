#!/usr/bin/python3.6
################################################################
#                                                              #
#                   file Python Script                         #
#          Fastkylin 2018年 12月 10日 星期一 00:13:29 CST      #
#                                Linux Ubuntu 18.04            #
#                                                              #
################################################################
import os
def isFileExist(path):
    if(os.access(path , os.F_OK)):
        return True
    else:
        return False

def isFileRead(path):
    if(os.access(path,os.R_OK)):
        return True 
    else:
        return False

def isFileWrite(path):
    if(os.access(path,os.W_OK)):
        return True
    else:
        return False
def getFileContent(path):
    if(isFileExist(path) and isFileRead(path)):
        try:
            f=open(str(path),'r')
            return f.read()
        finally:
            if f:
                f.close()
    else:
        print("out> File "+str(path)+"Not Found"+"or No Permission")
       # log.write()



