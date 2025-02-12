import csv
f=open('Testcsv.csv','w',newline='')
writer=csv.writer(f)
writer.writerow(["Emp NO","Name","Salary"])
writer.writerow([168,"Ragul",500])
f.close()


