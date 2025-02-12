def mean(l):
    sum=0
    for i in l:
        sum=sum+i
    
    mean=sum/len(l)
    return mean

def median(l):
    l.sort()
    if len(l)%2==0:
        mid=int(len(l)/2)
        a=(l[mid-1]+l[mid])/2
        return a
    else:
        mid=int((len(l)+1)/2)
        b=l[mid-1]
        return b
def mode(l):
    maxn=1

    x=0
    for i in l:
        m= l.count(i)
        print(m)
        if m>maxn:
            maxn=m
            x=i
    return x


