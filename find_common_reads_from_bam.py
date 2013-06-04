import sys,pysam
def calculate_intersection(file1,file2):
    bwa1 = pysam.Samfile(file1,"rb")
    bwa2 = pysam.Samfile(file2,"rb")
    list1 = [x.qname for x in bwa1]
    list2 = [x.qname for x in bwa2]
    set1 = set(list1)
    set2 = set(list2)
    intersection = set1.intersection(set2)
    print "File1\t\tFile2\t\tIntersection"
    print str(len(list1))+"\t\t"+str(len(list2))+"\t\t"+str(len(intersection))

calculate_intersection(sys.argv[1], sys.argv[2])
