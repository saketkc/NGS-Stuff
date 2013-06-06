import subprocess,sys
prefix=sys.argv[2]
filename=sys.argv[1]
command = "bwa aln -b Virus_fasta_reference/Virus_Fasta.fa " + filename +" > " + prefix+".sai"
command1 = "bwa samse Virus_fasta_reference/Virus_Fasta.fa "+prefix+".sai " + filename +" |  samtools view - -Sb -o " + prefix+"_all.bam"
command2 = "samtools view "+ prefix+"_all.bam"+ " -b -F 0x04 -o " + prefix+"_unmapped.bam"

command3 = "samtools view "+ prefix+"_all.bam"+ " -b -F 0x04 -o " + prefix+"_mapped.bam"


c1=subprocess.Popen(command,shell=True)
out,err=c1.communicate()


c1=subprocess.Popen(command1,shell=True)
out,err=c1.communicate()
c1=subprocess.Popen(command2,shell=True)
out,err=c1.communicate()
c1=subprocess.Popen(command3,shell=True)
out,err=c1.communicate()
