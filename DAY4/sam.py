'''s=7
p=11
a=3
b=15
create list '''

apples=[6,5,-4]
oranges=[9,8,-4]
s=7
t=11
a=3
b=15
a1=0
b1=0
for i in apples:
    if a+i>=s and a+i<=t:
        a1+=1
print(a1)
for i in oranges:
    if b+i>=s and b+i<=t:
        b1+=1
print(b1)
print(a1+b1)
    



