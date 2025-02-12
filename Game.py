
import random

l=1
u=50
p=""


while True:
    n=random.randint(l,u)
   # n=int((l+u)/2)       
    print("you no is ",n)
    p=input("correct?")
    if p=="Lesser":
        l=n+1
    elif p=="Greater":
        u=n-1
    elif p=="Yes":
        print("I win")
        break
    
    

