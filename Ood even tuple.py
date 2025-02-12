n=(8,5,6,6,77,99,66,33,44,55,66,77,74,55)

oddsum=0
evensum=0
opsum=0
epsum=0
for i in range(0,len(n)):
    if n[i]%2==0:
        evensum=evensum+n[i]
    else: 
        oddsum+=n[i]
        
    if i%2==0:
        epsum+=n[i]
    else:
        opsum+=n[i]
print(evensum)
print(oddsum)
print(opsum)
print(epsum)
