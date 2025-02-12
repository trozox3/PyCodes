n=int(input("Enter the no of Fib seris:"))
a=[0,1]


for i in range(2,n):
    a.append(a[i-1]+a[i-2])
print(a)    

    
