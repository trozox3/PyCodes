def rp(t):
    f=open(t,'r')
    l=f.readlines()
    print(l)
    w=l.pop(2)
    print("The removed line:",w)
    f.close()
    a=open(t,'w')
    s=('').join(l)  #to convert list to str
    a.write(s)
    a.close()
    
rp('Test1.txt')    
