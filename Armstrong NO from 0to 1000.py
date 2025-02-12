



for i in range(0,1001,1):
    sum=0
    for n in str(i):                  
        sum = sum + int(n)**3
    
    if sum == i:                                   
       print(i," is Armstrong NO")
    else:
       continue
    
    
