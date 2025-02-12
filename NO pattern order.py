n=int(input("Enter No Of Rows"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()    




n=int(input("Enter No Of Rows"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(n,end=" ")
    print()    

#to print character  in design (1 2 3 4 5 4 3 2 1)
n=int(input("Enter No Of Rows"))
a=input("Enter a Character:")
for i in range(1,n+1):
    for j in range(1,i+1):
        print(a,end=" ")
    print()    


for i in range(n-1,0,-1):
    for j in range(i,0,-1):
        print(a,end=" ")
    print()    
