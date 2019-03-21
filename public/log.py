#!/usr/bin/python3.6
################################################################
#                                                              #
#                   Log Python Script                          #
#          Fastkylin 2018年 12月 10日 星期一 00:02:49 CST      #
#                                Linux Ubuntu 18.04            #
#                                                              #
################################################################
#log script
import file
logPath="./log/log"
def logOutput(content):
    try:
        f=open(logPath,'r')
    finally:
        if f:
            f.close()
    if(not(f)):
        f.write(content)
        f.close




