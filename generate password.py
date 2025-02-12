import random

def genpass(len=8):
    a=['@','#','$','&']
    u=chr(random.randint(65,90))
    l=chr(random.randint(97,122))
    s=random.choice(a)
    d=random.randint(10000,99999)
    p=u+l+s+str(d)
    p=random.sample(p,len)
    p=('').join(p)
    return p

print(genpass())


while True:
    n=input("Type to Y to continue or N to stop:")
    if n=='y':
        
       print(genpass())
    elif n=='n':
        break
    else:
        print("Wrong choice")
