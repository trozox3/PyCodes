n=int(input("Enter a NO:"))
sum=0

m=n
while m!=0:
    r=m%10
    m=m//10         
    sum = sum + r**3
    
if sum==n:
    print("The No is Armstrong")
else:
    print("It is Not Armstrong")



