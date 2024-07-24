'''s=input()
ucount,lcount,dcount,scount=0,0,0,0
for c in s:
    if c.isupper():
        ucount+=1
    elif c.islower():
        lcount+=1
    elif c.isdigit():
        dcount+=1
    else:
        scount+=1
if len(s)>8 and ucount>0 and lcount>0 and dcount>0 and scount>0:
    print("valid password")
else:
    print("invalid password")'''

#    2nd method
pwd=input()
caps="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower="abcdefghijklmnopqrstuvwxyz"
dig=1234567890
spcl_char="!@#$%^&*()_?"
all=caps+lower+str(dig)+str(spcl_char)
for i in pwd:
    if len(pwd)>8 and all:
        print("valid")
        break
    else:
        print("invalid")