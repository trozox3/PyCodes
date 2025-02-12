
n=int(input("Enter the No of elements :"))

L1=[]
L2=[]
L3=[]
L4=[]
L5=[]
for i in range(0,n):
   a=int(input("Enter the Elements of List 1 :",))
   L1.append(a)
   
for i in range(0,n):
   b=int(input("Enter the Element of List 2 :"))
   L2.append(b)
   
   L3.append(L1[i]*L2[i])
   L4.append(L1[i]+L2[i])
   L5.append(abs(L3[i]-L4[i]))
print()   
print("The List 1:",L1)   
print("The List 2:",L2)   
print("The List 3 Product of List 1&2:",L3)
print("The List 4 SUM of List 1&2:",L4)
print("The List 5 Absolute Difference of List 3&4:",L5)
