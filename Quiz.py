import random
l=['What is capital of tamilnadu? ','what is 2+2? ','Who is the PM of India?','What is 4+4?','How many letters in car?']
d={0:'chennai',1:'4',2:'modi',3:'8',4:'3'}
point=0
n=''
b=[]
while True:
    while True:
         a=random.randint(0,len(l)-1)
         if l[a] not in b:
              print(l[a])
         else:
              continue
         b.append(l[a])
         print("Enter the answer:")
         n=input()
         if n==d[a]:
             print("Correct answer")
             point+=1
         else:
             print("Wrong answer")
         print()
     
         if len(b)==len(l):
             break

        
    print("Your Score:",point)
    print()
    point=0
    b=[]
    print("Press Y to Restart the Game.... \nPress N to Exit the Game....\n")
    print()
    u=input()
    if u=='Y':
         print("Restating.....The Game! ")
    elif u=='N':
        break
    else:
        print("Wrong Option")
    print()
print("Thank You")
