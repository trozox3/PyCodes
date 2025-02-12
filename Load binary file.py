import pickle
f=open('data.dat','rb')
k=pickle.load(f)
txt=pickle.load(f)
print(k,txt)
f.close()
