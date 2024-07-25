#Guessing number

import random
ran=random.randint(1,10)
chances=1
while chances<=3:     #while True for infinite loop remove chances
    guess=int(input())
    if guess==ran:
        print("congrats")
        break
    else:
        chances+=1
        continue
if chances>=3:
    print("falied try next time")
