s=input()
count=0
for i in range(0,len(s)):
    vowel='aeiouAEIOU'
    if s[i] in vowel:
        count+=1
print(count)