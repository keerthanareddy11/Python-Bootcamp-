#RESTAURANT
'''menu={
    'chicken_bryni':299,
    'butter_chkn':250,
    'tandoori':300,
    'manchuria':100

}
print(menu['butter_chkn'])   #insert item
menu['chicken_noodles']=80
print(menu)

#pop
menu.pop('manchuria')
print(menu)

#update tandoori cost to 800
menu['tandoori']=800
print(menu)


#return all the values
print(menu.values())


#print key to value 
for k,v in menu.items():
    print(k,'->',v)'''


#count frequency of each number

'''arr=[1,3,6,2,5,3,7,5,1]
#arr=list(map(int,input().split()))

d={}
for i in arr:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)'''

#print unique key values
'''arr=[1,3,6,2,5,3,7,5,1]
d={}
for i in arr:
    if i not in d:
        d[i]=1
        
    else:
        d[i]+=1
for num,count in d.items():
    if count==1:
        print(num)'''
    
    #print keys whose values are greater than one
'''arr=[1,3,6,2,5,3,7,5,1]
d={}
for i in arr:
    if i not in d:
        d[i]=1
        
    else:
        d[i]+=1
for num,count in d.items():
    if count>1:
        print(num)'''

#print parties    keys are ages and values are number of  votes
#1st method
'''congress={
    7:5,
    18:22,
    22:8,
    71:5,
    66:6
}
bjp={
    7:15,
    18:20,
    32:4,
    71:9,
    66:2
}
total_congress=0
total_bjp=0
for i in congress:
    if i>=18:
        total_congress+=congress[i]
print(total_congress)
for i in bjp:
    if i>=18:
        total_bjp+=bjp[i]
print(total_bjp)
total_eligible=total_congress+total_bjp
if total_congress>total_bjp:
    leading="congress"
    vote_difference=total_congress-total_bjp
else:
    leading="bjp"
    vote_difference=total_bjp-total_congress
print("total eligible votes:"+ str(total_eligible))
print(leading+" is leading by "+ str(vote_difference))'''


#2nd method
# Define the votes for each party with ages as keys
'''votes = {
    "Congress": {7: 5, 18: 22, 22: 8,71:5,66:6},
    "BJP": {18: 20, 7: 15, 32: 4,71:9,66:2}
}

# Initialize variables to calculate total eligible votes and total votes for each party
total_votes_congress = 0
total_votes_bjp = 0

# Calculate total votes for each party
for age in votes["Congress"]:
    if age>=18:
        total_votes_congress += votes["Congress"][age]
print(total_votes_congress)

for age in votes["BJP"]:
    if age>=18:
        total_votes_bjp += votes["BJP"][age]
print(total_votes_bjp)

# Calculate the total number of eligible voters
eligible_voters = total_votes_congress+total_votes_bjp

# Determine which party is leading and by how many votes
if total_votes_bjp > total_votes_congress:
    leading_party = "BJP"
    vote_difference = total_votes_bjp - total_votes_congress
else:
    leading_party = "Congress"
    vote_difference = total_votes_congress - total_votes_bjp

print("Total eligible votes: " + str(eligible_voters))
print(leading_party + " is leading by " + str(vote_difference) + " votes.")'''




