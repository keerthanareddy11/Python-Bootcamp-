n=101011
c=0
sum=0
while(n>0):
    rem=n%10   #1
    pro=rem*pow(2,c)  #1*2**0
    sum+=pro
    c+=1
    n=n//10
print(sum)


