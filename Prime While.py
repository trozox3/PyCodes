n=int(input("Enter a No: "))
i=2 # 2
prime=True

while i<int(n/2): # factor of 60 is 30 so it is enough to check until 30
    if n%i==0:                       # 1 and same no 
      prime=False
      break
    i+=1
if prime:
    print("The no is Prime")
else:
    print("The no is not a Prime")
