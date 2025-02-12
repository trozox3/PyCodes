'''import random
n=random.randint(1,50)

a=0
while a!=n:
    a=int(input("Enter a no :"))
    if a>n:
        print("The no is Greater than N")
    elif a<n:
        print("The no is Lesser than N")
    
if a==n:
    print("You won the game ")


'''
import random
n=random.randint(1,50)

a=0
while True:
    a=int(input("Enter a no from 1 to 50:"))
    if a<1 or a>50:
        print("Enter the no inside the limit")
    elif a>n:
        print("The no is Greater ")
    elif a<n:
        print("The no is Lesser ")
       
    elif a==n:
        
        print("You won the game ")

        break
