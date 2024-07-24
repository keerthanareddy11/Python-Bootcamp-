#Arranging using sorted function

'''s='apple'
res=sorted(s)
print(res)'''

#without inbuilt function finding number of alphabet in order
s='apple'
for i in s:
    print(i,'->',ord(i)-96)

#printing characters in alphabetical order for given numeber
s=str(11616125)
for i in s:
    print(i,'->',chr(i)-'96')
