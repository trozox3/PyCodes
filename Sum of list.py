'''n=[2,3,4,5,6,7,8,9]
sum=0
for i in n:
    sum=sum+i
print("Printing the sum of list:",sum)


n=[]
for i in range(0,9):
    n.append(input())
print(n)
a=max(n)
print("Greatest of the list:",a)




n=[]
i=0

while True:
    print("Enter the element")
    n.append(input())
    a=input("To STOP enter stop or CON:\n")
    if a=='stop':
        break
    else:
        continue
print(n)
b=min(n)
print("Min of list:",b)

    

    
'''
n=[]


for i in range(0,9):
    
    n.append(int(input()))
    
       
print(n)
a=n[0]
for i in range(0,9):
    if a<n[i]:
        a=n[i]
    
        
    
print(a)

