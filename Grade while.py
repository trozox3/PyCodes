n=int(input("Enter a No of Students:"))

i=0;
while i<n:
    name=input("Enter a Name of Student:")
    m1=int(input("Enter a mark for CS:"))
    m2=int(input("Enter a mark for Maths:"))
    m3=int(input("Enter a mark for DS:"))
    a=(m1+m2+m3)/3
    print("The Average Mark of ",name," is ",a)
    if a>90:
        Grade="A"
    elif a>80:
        Grade="B"
    elif a>70:
        Grade="C"
    elif a>60:
        Grade="D"
    else:
        Grade="F"
    print("The Grade of ",name," is ",Grade)
    print()
    print()


    i+=1
