#!/usr/bin/env python
import re,sys
from Bio import SeqIO
input_fasta = sys.argv[1]
nucleotides=['A','T','G','C']
motifs_count = {i+j:0 for i in nucleotides for j in nucleotides}
for rec in SeqIO.parse(input_fasta,"fasta"):
    position = 0
    for motif in motifs_count.keys():
        regexp = re.compile(motif)
        while True:
            matches = regexp.search(rec.seq.tostring(), position)
            if matches is None:
                break
            position= matches.start() + 1
            motifs_count[motif]+=1

all_matrix = [i+j for i in nucleotides for j in nucleotides]
row1 ="A\t"
row2 ="T\t"
row3="G\t"
row4 = "C\t"
row5 = "N\t"
row0 = "\tA\tT\tG\tC\tN"
row_A = [motifs_count['A'+str(i)] for i in nucleotides]
sum_A =sum(row_A)*1.0
row_T = [motifs_count['T'+str(i)] for i in nucleotides]
sum_T =sum(row_T)*1.0
row_G = [motifs_count['G'+str(i)] for i in nucleotides]
sum_G =sum(row_G)*1.0
row_C = [motifs_count['C'+str(i)] for i in nucleotides]
sum_C =sum(row_C)*1.0
row_N = [motifs_count['N'+str(i)] for i in nucleotides]
sum_N =sum(row_N)*1.0

row1  += ("\t").join("%0.3f" % (r/sum_A) for r in row_A)
row2  += ("\t").join("%0.3f" % (r/sum_T) for r in row_T)
row3  += ("\t").join("%0.3f" % (r/sum_G) for r in row_G)
row4  += ("\t").join("%0.3f" % (r/sum_C) for r in row_C)

row5  += ("\t").join(str(r/sum_N) for r in row_N)
print row0
print row1
print row2
print row3
print row4
print row5
