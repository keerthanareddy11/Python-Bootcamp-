#print(5^7)
#n=input()
#c=0
#for i in n+1:
 #   if not(i.isdigit()):
  #      c+=1
#print(c)
    


#data=[1,8,"apple","carrot","mango"]
#vegies=["brinjal","carrot"]
#fruits=["apple","mango","orange","grapes","carrot"]
#for i in data:
   # if i in vegies not in fruits:
      # print(i)


#identity op
#s='hi hello how are you hello how how'
#s=s.split()
#print(len(s))
#print(s.count('hello'))
#print(s.count('how'))



#functions
'''def greetings(branch):
    return 'hello hai',branch
print(greetings('cse'))
print(greetings('ece'))'''

'''def greetings(branch):
    print('hello hai',branch)
greetings('cse')
greetings('ece')'''
#check even or odd

'''def check(n):
    if n%2==0:
        return "even"
    else:
        return "odd"
print(check(18))'''
#another one for func

'''def check(n):
    if n%2==0:
        print("even")
    else:
        print("odd")
check(17)'''



'''def div(arr):
    count=0
    for i in arr:
        if i%4==0 and i%6==0:
            print(i)
            count+=1
    return count
arr=list(map(int,input().split()))
print(div(arr))'''

#reverse of words and sentence
'''def reverse(arr):
    rev=''
    for i in arr:
        rev=i+rev  
    return rev
arr=str(input())
print(reverse(arr))'''
#fibonacci series
'''def fib(n):
    t1=0
    t2=1
    c=2
    print(t1,t2,end=' ')
    while c<n:
        t3=t1+t2
        print(t3,end=' ')
        t1=t2
        t2=t3
        c+=1
fib(5)'''

#do until single digit is obtained
n=1895
s=0
c=0
for i in range(n):
    s=s+i
    c+=1
print(s)
    
    




#homework
'''n=678432
f=678
s=432
output:234678'''



#function call in function
'''def check(ele):
    return ele%2==0
def increment(arr):
    count=0
    for i in arr:
        if check(i):
            print(i)
            count+=1
    return count
arr=[5,9,12,6,17,3]
print(increment(arr))'''

#print only prime numbers  homework       #for palindrome  ele=str(ele)
                                            #  return ele==str(ele[::-1])
'''def check(ele):
    return ele%2==0
def increment(arr):
    count=0
    for i in arr:
        if check(i):
            print(i)
            count+=1
    return count
arr=[5,9,12,6,17,3]
print(increment(arr))'''
#check palindrome from 1 to 50
'''def check(n):
    n=str(n)
    return len(n)>1 and n==n[::-1]
def increment(N):
    c=0
    for i in range(1,N+1):
        if check(i):
            print(i)
            c+=1
    return c
N=50
print(increment(N))'''