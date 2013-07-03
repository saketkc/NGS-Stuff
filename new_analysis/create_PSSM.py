import sys, re
from Bio import SeqIO
class GetPSSM:
    def __init__( self, filelocation, fastq_format ):
        self.filelocation = filelocation
        self.fastq_format = fastq_format
        self.is_casava = False
        self.casava_regexp = re.compile('@.* [^:]*:N:[^:]*:')
        self.fails_casava = re.compile('@.* [^:]*:Y:[^:]*:')

        assert fastq_format in ['fastq', 'fastq-sanger', 'fastq-illumina', 'fastq-solexa']
    def run_index( self, index=True ):
        self.fastq_index = SeqIO.index(self.filelocation, self.fastq_format)
        self.set_casava()
        self.filter_casava()
        return self.fastq_index
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

