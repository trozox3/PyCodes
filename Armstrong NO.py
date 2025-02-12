n=input("Enter a NO:")
sum=0
for i in n:
    
    sum=sum+int (i)**3
if str (sum)== n:                                   # type convertion 
    print("The Given No is Armstrong NO")
else:
    print("The given NO is Not Armstrong no")
    
