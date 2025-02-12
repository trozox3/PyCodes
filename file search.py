def search(t,w):
    f=open(t,'r')
    l=f.readlines()
    '''words=f.read().split()
    if w in words:
        print("Word is found")
    else:
        print("Not found")
   
'''        
        
    





 
    
    c=0
    for i in l:
        a=i.split()
        
        if w in a :

            c+=1
            
    if c>0:
         print("Word Found")
    else:
         print("Not found")
    print("The word occurs ", c,'times')     
search('Test3.txt','python')
