def showdetail(name,d):
    for i in d:
       if name==d[i][0]:
            print("The employee no is:",i)
            print("The employee name is:",d[i][0])
            print("The employee salary is:",d[i][1])
            break
        
        
    else:
        print("The employee not found..")
def sale():
    for i in d:
        if d[i][1]>=20000:
            print("The employee who got more than 20000:",d[i][0])

d={}



# d={empno:[name,salary],.....}


n=int(input("Enter the No of Employess:"))

for i in range(0,n):
    l=[]
    empno=int(input("Enter the employee NO:"))
    name=input("Enter the Name of employee:")
    sal=float(input("Enter the salary of employee:"))
    l.append(name)
    l.append(sal)
    d[empno]=l
    print()
print(d)    
na=input("Enter the name to find empno:")
showdetail(na,d)
sale()
