def hcf(n,m):
   if n>m:
       x=n
       y=m
   else:
       x=m
       y=n
   r=x%y
   if r==0:
       h=y
   else:
       h=hcf(y,r)
   return h    
       


def lcm(n,m):
    l=(n*m)/hcf(n,m)
    return l



n=int(input("Enter the NO:"))
m=int(input("Enter the No:"))
print("HCF:",hcf(n,m))
print("LCM:",lcm(n,m))
