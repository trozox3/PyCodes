def factorial(n):

    if n==0:
        return 1
    else:
        return n*factorial(n-1)
n=int(input("Enter the No:"))
print("The factorial of no:",factorial(n))


def npr(n,r):
     p=factorial(n)/factorial(n-r)   
     return p
def ncr(n,r):
    c=factorial(n)/(factorial(n-r)*factorial(r))  
    return c
n=int(input("Enter the No:"))
r=int(input("Enter the NO:"))
print("NPR:",npr(n,r))
print("NCR:",ncr(n,r))
