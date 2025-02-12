def ip(t):
    f=open(t,'r')
    l=f.readlines()
    a=len(l)
    print("No of lines : ",a)
    c=0
    b=0
    
    for i in l:
        c=c+len(i)
        
        b=b+len(i.split())
        
            
    print("No of words:",b)
    print("No of characters:",c)    
    f.close()
    
ip('Test1.txt')

def ip1(t):
    f=open(t,'r')
    lines=f.readlines()
    f.seek(0)
    chars=f.read()
    words=chars.split()
    l=len(lines)
    c=len(chars)
    w=len(words)
    f.close()
    return l,c,w
        
        
            
      
    

l,c,w=ip1('Test1.txt')


print("No of lines,Characters,words:",l,c,w)


