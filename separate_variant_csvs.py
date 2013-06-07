import sys, csv
filepath = sys.argv[1]
reader = csv.reader(open(filepath,"r"),delimiter=",")
writer_synonymous = csv.writer(open())
for row in reader:

