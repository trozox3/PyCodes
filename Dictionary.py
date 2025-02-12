

'''d={'name':'ragul','age':18,'native':'rjpm'}
print(d)


print("printing age from dictionary :",d['age'])
print("Name:",d['name'])
for i in d:
    print(i,":",d[i])


d={}
name=input("enter the name:")
age=int(input("Enter the age:"))
native=input("Enter the native place:")
d['name']=name
d['age']=age
d['native']=native
print(d)

'''
n=int(input("Enter The No of Employoee"))



d={}
for i in range(0,n):
    a=[]
    print("Enter the EmployeeNO:")
    ep=int(input())
    name=input("Enter the Emp Name:")
    sal=float(input("Enter the Emp sal:"))
    
    
    a.append(name)
    a.append(sal)
    print()
    d[ep]=a
print(d)              
