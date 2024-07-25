n1=2885
n2=5945
carry=0
count=0
sum=0
while n1>0 and n2>0:
  res1=n1%10
  res2=n2%10
  sum=res1+res2+carry
  if sum>9:
    carry=1
    count+=1
  else:
    carry=0
  n1=n1//10
  n2=n2//10
  print("carry is:",carry)
print("number of carries are:",count)
