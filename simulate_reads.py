import os,shutil
import subprocess

fastq1 = sys.argv[1]
fastq2 = sys.argv[2]
name = sys.argv[3]
simulated1 = fastq1+".simulated"
simulated2 = fastq2+".simulated"

def simulate_reads(substitutionrate=0.001,insertsize=250,insertsd=60,simulate-minindellen=0,simulate_maxindellen=0,simulate_duplications,simulate_numsubstitutions):

    command = "stampy -g /data1/reference_index/human_g1k_v37 -h /data1/reference_index/human_g1k_v37 -S --inde "+ fastq1+","+fastq2
    stdout=open("stampystdout.log","wb")

    stderr=open("stampystderr.log","wb")
    proc = subprocess.Popen( args=command, shell=True, stderr=stderr.fileno(),stdout=stdout.fileno() )
    returncode = proc.wait()
    stdout.close()
    stderr.close()


