import  MMM

n=int(input("Enter the no of  element in list:"))
l=[]
for i in range(0,n):
    l.append(int(input("Enter a number:")))
    print()


print("Mean:",MMM.mean(l))
print("Median:",MMM.median(l))
print("Mode:",MMM.mode(l))
