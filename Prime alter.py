n= int(input("Enter a NO:"))
c=0
for i in range(1,n):
 
   if n%i==0:
       c+=1
       

if c==1:
    
   print("the no is prime")
else:
    print("The no is not prime")
  
