'''a=input("Enter the String")
d={}
for i in a:
    if i!=" ":
    
      if i in d:
         d[i]+=1
      else:
         d[i]=1
         

print(d)        


for i in d:
    if d[i]>1:
        b=d[i]
        c=i
        print(c,":",b)
'''

n=int(input("Enter the no of Things:"))

a=[]
for i in range(0,n):
    a.append(input("Enter the String:"))

print(a)


d={}

for i in a:
    n=len(i)
    if n in d:
        d[n].append(i)
    else:
        d[n]=[i]
        
print(d)        

        
        



    
