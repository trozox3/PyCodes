import pickle
f=open('data.dat','wb')
list=['Hello everyone','I am Ragul','i was learning python']
txt='\nIt is encrypted\n'
pickle.dump(list,f)
pickle.dump(txt,f)

f.close()

