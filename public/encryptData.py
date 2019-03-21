#!/usr/bin/python3.6
################################################################
#                                                              #
#                fileExist Python Script                       #
#          Fastkylin 2018年 11月 27日 星期二 12:35:04 CST      #
#                                Linux Ubuntu 18.04            #
#                                                              #
################################################################

#  encrypt the username and password

def debug(a):
	return a
def encryptuser(user):

    # encrypt user
   
    #u=list(input()) # string to list.because of string can not be changed
    u=list(user)
    for i in range(len(u)):
         u[i]=chr(ord(u[i])+4)  #get the ascii code and plus ascii 4
    outuser=''.join(u) # list to string
    #print(outuser)  

    return outuser
def encryptpassword(password):
      # encrypt password
    outpassword=""

    #p=list(input())
    p=list(password)
    key="1234567890"
    keyl=list(key)
    for i in range(len(p)):
        ki=ord(keyl[ len(key) - ( i % len(key) )-1 ]) ^ord(p[i] )
        #ki=ord(p[i])^(ord(keyl[len(key) - i%len(key) -1]))
        l=chr((ki&15)+54)
        h=chr(((ki>>4)&15)+99)

        if i%2==0:
            outpassword=outpassword+l+h
        else:
            outpassword=outpassword+h+l
    return outpassword
    #print(outpassword)





