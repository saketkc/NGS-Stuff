import sys,csv
reader1 = csv.reader(open(sys.argv[1]),delimiter=",")
reader2 = csv.reader(open(sys.argv[2]),delimiter=",")
row_count1 = sum(1 for row in reader1 )

row_count2= sum(1 for row in reader1 )


for row1 in reader1:
    for row2 in reader2:
        if row1==row2
