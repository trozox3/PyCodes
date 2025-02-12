import csv
f=open('Testcsv.csv','a',newline='')
writer=csv.writer(f)
writer.writerows([[174,"Rishi",6000],[171,"Rake",800]])
writer.writerow([196,"Shriram",400])
f.close()
