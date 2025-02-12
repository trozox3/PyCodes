import pickle
f=open('Emp.dat','rb')


try:
     l=[]
     while True:
    
        l.append(pickle.load(f))

except EOFError:
    
      f.close()
l.pop(1)

b=open('Emp.dat','wb')
pickle.dump(l,b)
b.close()
c=open('Emp.dat','rb')
try:
    
    while True:
    
        txt=pickle.load(c)
        print(txt)
except EOFError:
    
      c.close()
