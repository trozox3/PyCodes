n=[8,9,6,2,4,6,3,2,0,1]

print("Printing full list:\n",n)
print()
print("Inserting 25 on second index\n")
n.insert(2,25)
print(n)
print()
print("Removing 4")
n.remove(4)
print(n)
print()
print("Removing last item")
n.pop()
print(n)
print()
print("Removing 4th item")
x=n.pop(3)
print(n)

print("The fourth element removed",x)
print()
print("Reversing the list")
n.reverse()
print(n)
print()
print("Minumum no and maximum no of list")
a=min(n)
b=max(n)
print("Min:",a)
print("Max:",b)
print()
print("Printing list in asc order")
n.sort()
print(n)
print()
print("Printing in des order")
n.sort(reverse=True)
print(n)
print()
print("Adding item in end of list")
n.append(80)
print(n)
print()


print("Adding list to list")
n1=["a","b","c","d"]
n.append(n1)
print(n)
print()
print("Adding list element to list")
n.extend(n1)
print(n)
print()
print("The total no element in list")

c=len(n)
print(c)
print()


print("Printing 4th item")
d=n[3]
print(d)
print()
print("Printing 4th item from the last")
e=n[-4]
print(e)


print()
print("Counting no of 2")
f=n.count(2)
print(f)
print()

print("Printing 1st four items in list")
print(n[0:4])
print()
print("printing element in nested list")
print(n[9][2])
print()
print(n[8:1:-1])
print()
print(n[2:10:2])
print("Reverse the list")
print(n[-1:-5:-1])





