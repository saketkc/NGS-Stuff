import sys, re
from Bio import SeqIO
import matplotlib.pyplot as plt
class GetPSSM:
    def __init__( self, filelocation, fastq_format ):
        self.filelocation = filelocation
        self.fastq_format = fastq_format
        self.is_casava = False
        self.nucleotides=['A','G','T','C','N']
        self.per_base_count = {i:0 for i in self.nucleotides}
        self.read_wise_motif_count={}
        self.read_wise_motif_count = {}
        self.records = None
        self.casava_regexp = re.compile('@.* [^:]*:N:[^:]*:')
        self.fails_casava = re.compile('@.* [^:]*:Y:[^:]*:')

         assert fastq_format in ['fastq', 'fastq-sanger', 'fastq-illumina', 'fastq-solexa']

    def run_index( sel):
        self.fastq_index = SeqIO.index(self.filelocation, self.fastq_format)
        self.set_casava()
        self.filter_casava()
        return self.fastq_index

    def read_in_memory( self ):
        self.records = [rec for rec in SeqIO.parse(self.filelocation, self.fastq_format)]
        return True

    def create_motif_regex(motif):
        return re.compile(motif)

    def get_read_wise_motif_content( self, per_base_content=True ):
        for i,rec in enumerate(self.records):
            motifs_count = {i+j:0 for i in self.nucleotides for j in self.nucleotides }
            if per_base_content:
                self.per_base_count = {i:rec.tostring().count(i) for i in self.nucleotides}
            position = 0
            for motif in motifs_count.keys():
                position=0
                regexp = self.create_motif_regex(motif)
                while True:
                    result = regexp.search(rec.tostring(), position)
                    if result is None:
                        break
                    else:
                        position+=1
                        motifs_count[motif]+=1
            self.read_wise_motif_count[i]= motifs_dict
        return True







    def set_casava( self) :
        key = self.fastq_index.keys()[2]
        print key
        print self.fastq_index[key]

        if self.casava_regexp.match(key):
            self.is_casava=True
        return True

    def filter_casava( self ):
        if self.is_casava:
            for key in self.fastq_index:
                print key
                if self.fails_casava.match(key):
                    print key
        return True

    def get_sequences( self ):
        for key in self.fastq_index:
            print self.fastq_index[key]

if __name__=="__main__":
    get_pssm = GetPSSM(sys.argv[1], "fastq")
    get_pssm.run_index()

#    for keys in get_pssm.run_index():
 #       print keys

