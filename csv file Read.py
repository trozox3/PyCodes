import csv
f=open('Testcsv.csv','r',newline="")
reader=csv.reader(f)
for i in reader:
    print(i)
f.close()
