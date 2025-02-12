import pickle
e=int(input("Enter the emp no:"))
f=open('Emp.dat','rb')
try:
    k=[]
    while True:
        k.append(pickle.load(f))

except EOFError:
    f.close()

for i in range(0,len(k)):
    if k[i][0] == e:
        sal=int(input("Enter the salary:"))
        
        k[i][2]=sal




a=open('Emp.dat','wb')
pickle.dump(k,a)
a.close()   
    
