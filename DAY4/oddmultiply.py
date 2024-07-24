n=str(input())
m=int(input())
res=0
mul=0
add=0
for i in n:
    if int(i)%2==0:
        add=int(i)+m
        #print(add,end='')
    else:
        mul=int(i)*m
        #print(mul,end='')



