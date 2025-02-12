def area1():
    r=float(input("Enter Radius:"))
    a=3.14*r*r
    print("Area of circle :",a)

area1()
def area2(r):
    a=3.14*r*r
    print("Area of circle :",a)
    



r=float(input("Enter the radius:"))
area2(r)


def area3():
    r=float(input("Enter Radius:"))
    a=3.14*r*r
    return a


print("Area of circle:",area3())

def area4(r):
    a=3.14*r*r
    return a


r=float(input("Enter the radius:"))
print("Area of circle:",area4(r))
