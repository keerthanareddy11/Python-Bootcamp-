alice=[10,3,6]
bob=[12,3,4]

a=0
b=0
for i in range(len(alice)):
    if alice[i]>bob[i]:
        a+=1
    else:
        b+=1
if a>b:
    print("alice won")   
elif b>a:
    print("bob won") 
else:
    print("Both have equal points")



#swap without third var
'''a=int(input())
b=int(input())
a=a+b
b=a-b
a=a-b
print(a)
print(b)'''