'''mob=['iphone','samsung','oppo']
mob.insert(2,'vivo') #inserts in particular pos
print(mob)
frnd=['keerthi','ajay','srikanth','rishith','laddu']
frnd.append('divya') #adds last
print(frnd)
frnd.remove('keerthi') #removes perticular ele
print(frnd)
frnd.pop()#pops last ele
print(frnd)
            #print empty list but not list
mob.clear()
print(mob)
             #update
frnd[2]='chikky'
print(frnd)
print(frnd[True]) #prints 1st index value
print(frnd[False]) #prints 0th index val

#frnd=[]
c=1
for i in frnd:
    print(c,i)
    c+=1'''
    #print indexes with even and reverse of only those even indexed values and keep odd indexes same
'''li=['cat','dog','donkey','rabbit','tiger','lion']
for i in range(0,len(li)):
    if i%2==0:
        rev=li[i]
        print(rev[::-1])
    else:
        print(li[i])'''
    

#k=3
#o/p:34512
arr=[1,2,3,4,5]
k=int(input())
#frst=arr[k-1:]
#second=arr[:k-1]
#print(frst+second)
#frst.extend(second)
#print(frst)

'''i/p:k=3
o/p:[5,4,3,1,2]  reverse last 3 and print 1st two same
frst=arr[k+1:k-(k-1):-1]
#print(frst)
second=arr[:k-1]
print(frst+second)'''

#print last 2 ele in reverse and remaining same
'''frst=arr[k+2:k:-1]
#print(frst)
second=arr[:k+1]
print(frst+second)'''


        