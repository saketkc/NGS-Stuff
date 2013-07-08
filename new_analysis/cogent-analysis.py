#!/usr/bin/env python
from cogent import LoadSeqs, DNA
from cogent.core.usage import DinucUsage
import sys
input_fasta = "human.fasta"#sys.argv[1]
nucleotides = ['A','G','C','U']
fasta = LoadSeqs(input_fasta, moltype=DNA,aligned=False,format='fasta')
print fasta[0]
#for rec in fasta:
#    print rec
#du  = DinucUsage(y_pseudo_seq, Overlapping=True)
