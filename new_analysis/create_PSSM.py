#!/usr/bin/env python
import sys, re
from Bio import SeqIO
import matplotlib.pyplot as plt
class GetPSSM:
    def __init__( self, filelocation, fastq_format ):
        self.filelocation = filelocation
        self.fastq_format = fastq_format
        self.is_casava = False
        self.nucleotides=['A','G','T','C','N']

        self.per_base_count = {}
        self.read_wise_motif_count={}
        self.read_wise_motif_count = {}
        self.records = None
        self.casava_regexp = re.compile('@.* [^:]*:N:[^:]*:')
        self.fails_casava = re.compile('@.* [^:]*:Y:[^:]*:')
        assert fastq_format in ['fastq', 'fastq-sanger', 'fastq-illumina', 'fastq-solexa']

    def run_index( self ):
        self.fastq_index = SeqIO.index(self.filelocation, self.fastq_format)
        self.set_casava()
        self.filter_casava()
        self.records = [self.fastq_index[index] for index in self.fastq_index.keys()]
        return self.records

    def guess_read_length(self):
        try:
            self.read_lengths = [len(rec.seq) for rec in self.records]
            self.read_length = max(self.read_lengths)
            self.total_bases = sum(self.read_lengths)
            return self.read_length
        except:
            raise "10 reads should be present"


    def read_in_memory( self ):
        self.records = [rec for rec in SeqIO.parse(self.filelocation, self.fastq_format)]
        return self.records

    def create_motif_regex(self, motif):
        return re.compile(motif)

    def get_read_wise_motif_content( self, per_base_content=True):
        self.per_position_base_content = {i:{n:0 for n in self.nucleotides} for i in range(0,self.read_length)}
        for i,rec in enumerate(self.records):
            for pos,nuc in enumerate(rec.seq.tostring()):
                self.per_position_base_content[pos][nuc]+=1
            if per_base_content:
                base_count = {n:rec.seq.tostring().count(n) for n in self.nucleotides}
                self.per_base_count[i] = base_count
            motifs_count = {i+j:0 for i in self.nucleotides for j in self.nucleotides }
            for motif in motifs_count.keys():
                position=0
                regexp = self.create_motif_regex(motif)
                while True:
                    matches = regexp.search(rec.seq.tostring(), position)
                    if matches is None:
                        break
                    position= matches.start() + 1
                    motifs_count[motif]+=1
            self.read_wise_motif_count[i]= motifs_count
        return self.read_wise_motif_count

    def create_cpg_matrix(self ):
        motifs_count = {i+j:0 for i in self.nucleotides for j in self.nucleotides }
        for readnumber in self.read_wise_motif_count.keys():
            for motif in motifs_count.keys():
                motifs_count[motif]+=self.read_wise_motif_count[readnumber][motif]


        all_matrix = [i+j for i in self.nucleotides for j in self.nucleotides]
        row1 ="A\t"
        row2 ="T\t"
        row3="G\t"
        row4 = "C\t"
        row5 = "N\t"
        row0 = "\tA\tT\tG\tC\tN"
        row_A = [motifs_count['A'+str(i)] for i in self.nucleotides]
        sum_A =sum(row_A)*1.0
        row_T = [motifs_count['T'+str(i)] for i in self.nucleotides]
        sum_T =sum(row_T)*1.0
        row_G = [motifs_count['G'+str(i)] for i in self.nucleotides]
        sum_G =sum(row_G)*1.0
        row_C = [motifs_count['C'+str(i)] for i in self.nucleotides]
        sum_C =sum(row_C)*1.0
        row_N = [motifs_count['N'+str(i)] for i in self.nucleotides]
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
    def set_casava( self) :
        key = self.fastq_index.keys()[1]
        #print key
        #print self.fastq_index[key]
        if self.casava_regexp.match(key):
            print "CASAVA"
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
    #get_pssm.read_in_memory()
    get_pssm.run_index()
    get_pssm.guess_read_length()
    get_pssm.get_read_wise_motif_content()
    read_wise_motif_count = get_pssm.read_wise_motif_count
    get_pssm.create_cpg_matrix()
    """
    filter motif in get
    print get_pssm.per_base_count
    base_content = get_pssm.per_position_base_content
    for i in base_content.keys():
        for j in base_content[i].keys():
            if base_content[i][j] !=0:
                print i,j,base_content[i][j]

    #get_pssm.run_index()

#    for keys in get_pssm.run_index():
 #       print keys
    """
