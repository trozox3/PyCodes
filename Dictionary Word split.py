a=input("Enter a String:")
w=a.split()
print(w)
d={}
for i in w:
    j=i[0]   # to return first letter of element
    
    if j in d:
        if i not in d[j]:
            d[j].append(i)
    else:
        d[j]=[i]
print(d)        
        
    
