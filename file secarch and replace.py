def replace(t,w1,w2):
    f=open(t,'r')
    lines=f.readlines()
    

    
    for l in range(0,len(lines)):
        words=lines[l].split()
        for w in range(0,len(words)):
            if w1==words[w]:
                words[w]=w2
        lines[l]=(' ').join(words)
        
    txt=('\n').join(lines)
    
    f.close()
    a=open(t,'w')
    a.write(txt)
    a.close()
            
replace('Test2.txt','python','program')
