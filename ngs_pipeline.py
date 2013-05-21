import argparse
from Bio.Sequencing.Applications import BwaCommandline
parser = argparse.ArgumentParser()
parser.add_argument("-r1", "--read1", help="read1.fastq path", required=True)
parser.add_argument("--read2", help="read2.fastq path", required=True)
parser.add_argument("--reference",help="Absolute path to reference genome")
parser.parse_args()



