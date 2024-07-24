#Good numbers

'''arr=[35,9,1]
res=low cube+high cube
low=1
high=3
whil low<high
res=1+27
if res<=arr[i]
low+=1
elif res==arr[i]
count+=1'''

import math
arr=[35,9,1,65,126,133,]
res=0
count=0
for i in arr:
    low=1
    high=math.ceil(i**0.3)
    while low<high:
        res=low**3+high**3          #low cube + high cube
        if res==i:
            print("The Good numbers is:",i)
            count+=1
        if res<i:
            low+=1
        else:
            high-=1 
print("the number of good numbers are:",count)

