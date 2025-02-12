'''
n=input("Enter a NO:")
sum=0
i=0
while i<len(n):
    sum = sum +int(n[i])**3
    i+=1
if str(sum)==n:
    print("The No is Armstrong")
else:
    print("It is Not Armstrong")
'''





i=0

while i<1001:
    m=i

    sum=0
    while m!=0:
        j=m%10
        m=m//10
        sum=sum+j**3
        
    
    if sum==i:
       print(sum,"is Armstrong")
    i+=1



