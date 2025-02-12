def simpint(p,n,r=18.2):
    i=(p*n)*(r/100)
    return i


p=float(input("Enter the Principle amount:"))
n=int(input("Enter the no of Years:"))
r=input("Enter the intrest rate:")
#if r=='':
    #print("The simple intrest :",simpint(p,n))
#else:
    
print("The simple intrest :",simpint(p,n,float(r)))
