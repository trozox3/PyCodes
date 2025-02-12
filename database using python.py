import sqlite3
def insert():
      con=sqlite3.connect('Emp.db')
      c=con.cursor()
      r=int(input("Enter the Empno: "))
      n=input("Enter the name:")
      b=float(input("Enter the salary:"))
      r=str(r)
      c.execute("SELECT * FROM SALARY WHERE EMPNO='"+r+"'")
      
      table=c.fetchall()
      if table:
          print("Emp no exists")
      else:
          c.execute("INSERT INTO SALARY VALUES(:EMPNO,:EMPNAME,:BASIC)",{'EMPNO':r,'EMPNAME':n,'BASIC':b})
      con.commit()
      con.close()
  
def showall():
      con=sqlite3.connect('Emp.db')
      c=con.cursor()
      c.execute('SELECT * FROM SALARY')
      table =c.fetchall()
      for i in table:
          print("EmpNO:",i[0])
          print("Empname:",i[1])
          print("Basic:",i[2])
          a=(i[2])*(20/100)
          print("DA:",a)
          b=(i[2])*(10/100)
          print("HRA:",b)
          c=a+b+i[2]
          print("Net Salary:",c)
          print()
      con.commit()
      con.close()
def delete():
      con=sqlite3.connect('Emp.db')
      c=con.cursor()
      r=int(input("Enter the Empno: "))
      r=str(r)
      c.execute("SELECT * FROM SALARY WHERE EMPNO='"+r+"'")
      table=c.fetchall()
      if not table:
          print("no such record")
      else:
          c.execute("DELETE FROM SALARY WHERE EMPNO='"+r+"'")
          print("data deleted")
      
      con.commit()
      con.close()

def search():
      con=sqlite3.connect('Emp.db')
      c=con.cursor()
      r=int(input("Enter the Empno: "))
      r=str(r)
      c.execute("SELECT * FROM SALARY WHERE EMPNO='"+r+"'")
      table=c.fetchall()
      if not table:
          print("no such record")
      else:
          
          for t in table:
             print(t)
          print("data found")
      
      con.commit()
      con.close()
      


      
def update():
     con=sqlite3.connect('Emp.db')
     c=con.cursor()
     r=int(input("Enter the Empno: "))
     r=str(r)
     c.execute("SELECT * FROM SALARY WHERE EMPNO='"+r+"'")
     table=c.fetchall()
     opt=int(input("Type 1 for name change , 2 for Salary change...."))
     if opt ==1:
         oldvalue=table[0][1]
         newvalue=input("Enter the name :")
         c.execute("UPDATE SALARY SET EMPNAME=:n WHERE EMPNO='"+r+"' ",{'n':newvalue})
     elif opt==2:
         oldvalue=table[0][2]
         newvalue=float(input("Enter the salary :"))
         c.execute("UPDATE SALARY SET BASIC=:n WHERE EMPNO='"+r+"' ",{'n':newvalue})
     con.commit()
     con.close()
    

     
con=sqlite3.connect('Emp.db')
c=con.cursor()
c.execute('CREATE TABLE IF NOT EXISTS SALARY(EMPNO INT,EMPNAME TEXT,BASIC FLOAT)')

con.commit()
con.close()
#insert()
#showall()
#delete()
#showall()
#search()
#update()
#showall()
print("!---------------------Welcome-----------------------!")
while True:
  

   print("1-Insert") 
   print("2-Delete \n3-Search \n4-Update \n5-Showall \n6-Exit")
   l=int(input("Enter the serial no to perform operation:"))
   if l==1:
         insert()
   elif l==2:
         delete()
   elif l==3:
         search()
   elif l==4:
         update()
   elif l==5:
         showall()
   elif l==6:
         print("!-----------------------Thank You-----------------------------!")
         break
   else:
         print()
         print("Wrong option")
         print()
