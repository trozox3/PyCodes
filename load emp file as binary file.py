import pickle
f=open('Emp.dat','rb')
try:
    
    while True:
    
        k=pickle.load(f)
        print(k)
except EOFError:
    
      f.close()
