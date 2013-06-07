import csv,sys
filepath = sys.argv[1]
novelvariants_filepath = filepath.split(".")[0]+"_novel_variants.csv"
reader= csv.reader(open(filepath,"r"),delimiter=",")
writer = csv.writer(open(novelvariants_filepath,"w"))
for row in reader:
    if row[8]=="":
        writer.writerow(row)
#writer.close()


