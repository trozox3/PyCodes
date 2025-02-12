n=("Table","Chair","Ac","Ironbox","Fan")

'''for i in n:
    if i[0] in "AEIOUaeiou" :
        print(i)'''
i=0        
while i<len(n):
    if n[i][0] in "AEIOUaeiou":
        print(n[i])
    i+=1
