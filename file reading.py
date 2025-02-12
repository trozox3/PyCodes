f=open('Test.txt','r')
print(f.read())
f.seek(0)
print(f.readline())
f.seek(0)# to move the cursor to begining
print((f.readlines()))
f.seek(0)
print(f.read(35))
print(f.tell())


f.close()
