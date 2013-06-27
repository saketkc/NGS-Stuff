import os
import sys

import pysam
from Bio import SeqIO, Seq, SeqRecord

def convert_to_fasta(in_file):
    out_file = "%s.fa" % os.path.splitext(in_file)[0]
    with open(out_file, "w") as out_handle:

        SeqIO.write(bam_to_fasta(in_file), out_handle, "fasta")

def bam_to_fasta(in_file):

    bam_file = pysam.Samfile(in_file, "rb")
    for read in bam_file:
        seq = Seq.Seq(read.seq)
        if read.is_reverse:
            seq = seq.reverse_complement()
        rec = SeqRecord.SeqRecord(seq, read.qname, "", "")
        yield rec

if __name__ == "__main__":
    convert_to_fasta(*sys.argv[1:])

