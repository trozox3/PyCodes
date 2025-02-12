def saveas(t,t1):
    f=open(t,'r')
    l=f.readlines()
    f.close()
    a=open(t1,'w')
    
    a.writelines(l)
    a.close()

saveas('Test2.txt','Test3.txt')    
