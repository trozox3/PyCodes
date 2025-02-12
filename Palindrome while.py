n=input("Enter a String:")
b=""
i=0
while i<len(n):
    b=n[i]+b
    i+=1
if n==b:
    print("Palindrome")
else:
    print("Not Palindrome")
    
