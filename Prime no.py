n= int(input("Enter a NO:"))
prime=True
for i in range(2,n):
 
   if n%i==0:
       prime=False
       break;

if prime:
    
   print("the no is prime")
else:
    print("The no is not prime")
  
