def askcontry(i='INDIA'):
    print("Your Contry is:",i)

a=input("You are from Which contry?:")
if a=="":
    askcontry()
else:
    askcontry(a)




