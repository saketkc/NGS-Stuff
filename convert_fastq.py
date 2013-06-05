import sys
filename = sys.argv[1]
filetowrite = filename.split(".")[0]+"_sngr"+".fastq"
from Bio import SeqIO
SeqIO.convert(filename,"fastq-illumina",filetowrite,"fastq")
