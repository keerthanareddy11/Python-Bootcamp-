'''s=['aba','sasdad','aaaccc','tatdog']
s1=''
for i in range(len(s)-1,-1,-1):
    s1+=s[i]
if s1==s:
    print("palindrome")
else:
    print("not")'''


'''strings = ["aba", "sasdad", "aaaccc", "tatdog"]
count = 0

for i in strings:
    n = len(i)
    if n % 2 == 0:
        first_half = i[:n//2]
        second_half = i[n//2:]
    else:
        first_half = i[:n//2]
        second_half = i[n//2 + 1:]
    res=i[::-1]
    halindrome=first_half == second_half[::-1]

    half_length = n // 2
    if n % 2 == 0:
        half_string = i[:half_length]
    else:
        half_string = i[:half_length + 1]
    
    is_half_palindrome = half_string == half_string[::-1]

    if halindrome or is_half_palindrome:
        count += 1
        print(f"'{i}' is a halindrome and at least half of it is a palindrome")
    else:
        print(f"'{i}' is not a halindrome or at least half of it is not a palindrome")

print(f"Number of halindromes with at least half palindrome: {count}")'''



strings = ["aba", "sasdad", "aaaccc", "tapdog","emepe"]
count = 0

for i in strings:
    if i==i[::-1]:
        count+=1
        print(i)
    
    else:
        m=len(i)//2
        if len(i)%2==0:
          
            first=i[:m]
            second=i[m:]
            if first==first[::-1] or second==second[::-1]:
                count+=1
                print(i)

        else:
            first=i[:m+1]
            second=i[m+1:]
            if first==first[::-1] or second==second[::-1]:
                count+=1
                print(i)
    
print(count)

