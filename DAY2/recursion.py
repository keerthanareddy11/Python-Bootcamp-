#Factorial of a number

'''def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
n=int(input())
print(fact(n))'''
#sum of natural numbers
'''def sum_natural(n):
    if n==1:
        return 1
    else:
        return n+sum_natural(n-1)

n=int(input())
print(sum_natural(n))'''
#without using recursion
'''n=int(input())
sum=0
for i in range(0,n+1):
    sum+=i
print(sum)'''

#fibonacci recursion
'''def fib(n):
    if n==0 or n==1:
        return n
    else:
        return fib(n-1)+fib(n-2)
n=int(input())
print(fib(n))'''


# finding n fibonacci series
def fib(n):

