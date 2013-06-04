import pysam

def read_sam_or_bam(filelocation):
    sam_or_bam = pysam.Samfile(filelocation,"rb")
    for reads  in sam_or_bam.fetch(until_eof=True):
        seq = Seq
