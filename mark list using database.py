import sqlite3
def insert():
    con=sqlite3.connect('Marks.db')
    c=con.cursor()
    reg=int(input("Enter the Register No:"))
    reg=str(reg)
    name=input("Enter the Name of Student:")
    m1=float(input("Enter the marks for subject1:"))
    m2=float(input("Enter the marks for subject2:"))
    m3=float(input("Enter the marks for subject3:"))
    c.execute("SELECT * FROM MARKLIST WHERE REGNO='"+reg+"'")
    table=c.fetchall()
    if table:
        print("Reg no is Already registered!!!")
    else:
        c.execute("INSERT INTO MARKLIST VALUES(:REGNO,:NAME,:MARK1,:MARK2,:MARK3)",{'REGNO':reg,'NAME':name,'MARK1':m1,'MARK2':m2,'MARK3':m3})
        print()

        
    con.commit()
    con.close()
def showall():
    con=sqlite3.connect('Marks.db')
    c=con.cursor()
    c.execute("SELECT * FROM MARKLIST ")
    table=c.fetchall()
    for i in table:
        print("Register Number:",i[0])
        print("Name of Student:",i[1])
        print("Mark1:",i[2])
        print("Mark2:",i[3])
        print("Mark3:",i[4])
        a=i[2]+i[3]+i[4]
        print("Total Mark:",a)
        print("Average Mark:",a/3)
        print()
        
        
        
    con.commit()
    con.close()


def delete():
    con=sqlite3.connect('Marks.db')
    c=con.cursor()
    reg=int(input("Enter the Register No:"))
    reg=str(reg)
    c.execute("SELECT * FROM MARKLIST WHERE REGNO='"+reg+"'")
    table=c.fetchall()
    if not table:
        print("Register Number not Found")
    else:
        c.execute("DELETE FROM MARKLIST WHERE REGNO='"+reg+"'")
        print("Deleteted")
        print()

    con.commit()
    con.close()


def search():
    con=sqlite3.connect('Marks.db')
    c=con.cursor()
    reg=int(input("Enter the Register No:"))
    reg=str(reg)
    c.execute("SELECT * FROM MARKLIST WHERE REGNO='"+reg+"'")
    table=c.fetchall()
    if not table:
        print()
        print("Not found")
        print()
    else:
        for i in table:
            print(i)

    con.commit()
    con.close()
    



def update():
    con=sqlite3.connect('Marks.db')
    c=con.cursor()
    l=int(input("Enter the REGNO to be updated: "))
    l=str(l)
    c.execute("SELECT * FROM MARKLIST WHERE REGNO='"+l+"'")
    table=c.fetchall()
    print("Press 1 to Update Name......")
    print("Press 2 to Update Mark 1......")
    print("Press 3 to Update Mark 2......")
    print("Press 4 to Update Mark 3......")
    o=int(input())
    if o==1:
        n=input("Enter the name:")
        c.execute("UPDATE MARKLIST SET NAME=:na WHERE REGNO='"+l+"'",{'na':n})
    elif o==2:
        m1=float(input("Enter the Mark 1:"))
        c.execute("UPDATE MARKLIST SET MARK1=:m WHERE REGNO='"+l+"'",{'m':m1})
    elif o==3:
        m2=float(input("Enter the Mark 2:"))
        c.execute("UPDATE MARKLIST SET MARK2=:m WHERE REGNO='"+l+"'",{'m':m2})
    elif o==4:
        m3=float(input("Enter the Mark 3:"))
        c.execute("UPDATE MARKLIST SET MARK3=:m WHERE REGNO='"+l+"'",{'m':m3})
    con.commit()
    con.close()


             


             
















con=sqlite3.connect('Marks.db')
c=con.cursor()
c.execute("CREATE TABLE IF NOT EXISTS MARKLIST (REGNO INT,NAME TEXT,MARK1 FLOAT,MARK2 FLOAT,MARK3 FLOAT)")
con.commit()
con.close()



print("!--------------------------------------------------------------------------------------WELCOME---------------------------------------------------------------------------------------!")
while True:
    print("Enter the Option:")
    print("1-Insert")
    print("2-Delete")
    print("3-Search")
    print("4-Update")
    print("5-Showall")
    print("6-Exit")
    l=int(input())
    if l==1:
        insert()
        showall()
    elif  l==2:
        delete()
        showall()
    elif l==3:
        search()
    elif l==4:
        update()
        showall()
    elif l==5:
        showall()
    elif l==6:
        print("!=====================================================================================THANK YOU====================================================================================!")
        break
    else:
        print()
        print("Wrong Choice")
        print()
          
