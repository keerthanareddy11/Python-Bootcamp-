#Exception handling
'''try:
    a=10
    b=0
    c=a/b
    print(c)
    #n1=100
    #n2=200
    #print(n1+n2)###exception arised so not executing
except Exception:
    print("divide by zero is not possible")
    n1=100
    n2=200
    print(n1+n2)
    a1=1000
    a2=2000
    print(a1+a2)'''

'''try:
    a=5
    print(b)
except NameError:
    print("variable b is not declared")'''

try:
    arr=[1,2,3,4,5]
    print(arr[3])
except IndexError:
    print("can't access index value")
else:
    print("no exception occured")
finally:
    print("finally wednesday is last day of training")