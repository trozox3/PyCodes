import pickle
f=open('Emp.dat','ab')
n=int(input("Enter the no of emp:"))



for i in range(0,n):
    l=[]
    a=int(input("Enter the EmpNO:"))
    l.append(a)
    
    b=input("Enter the Name of emp:")
    l.append(b)
    c=int(input("Enter the salary:"))
    l.append(c)
    print()
    
    pickle.dump(l,f)

f.close()    
