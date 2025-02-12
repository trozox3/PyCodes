import csv
f=open('Testcsv.csv','r',newline='')
e=input("Enter the empno:")
r=csv.reader(f)
l=[]
a=[]
for i in r:
    l=i
    if i[0]==e:
        l.pop()
    else:
        a.append(i)
            
f.close()

b=open('Testcsv.csv','w',newline='')
w=csv.writer(b)
w.writerows(a)
b.close()
