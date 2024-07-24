'''4
****
*  *
*  *'''


'''n=int(input())
for i in range(1,n+1):
    if i==1 or i==n:
        
        print("*"*n)
    else:
        print("*"+" "*(n-2)+"*")'''
        
        
#s="1C0C1C1A0B1"
s=input()
temp=int(s[0])
for i in range(1,len(s),2):
    if s[i]=='A':
        temp=temp & int(s[i+1])
        #print(temp)
    elif s[i]=='B':
        temp=temp | int(s[i+1])
        #print(temp)
    elif s[i]=='C':
        temp=temp ^ int(s[i+1])
print(temp)

