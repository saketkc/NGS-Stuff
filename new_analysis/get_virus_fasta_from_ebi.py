#!/usr/bin/env python
import urllib2
import re
txt_ftp_location = "ftp://ftp.ncbi.nlm.nih.gov/genomes/GENOME_REPORTS/viruses.txt"
handle = open("virus.txt","r")
response = handle.read()
project_ids = [line for line in response.splitlines()]
outputpath="/data1/Custom_Fasta/"

for id in project_ids:
    try:
        handle = urllib2.urlopen("http://www.ebi.ac.uk/ena/data/view/"+str(id)+"&display=fasta")
        record = handle.read(handle)
        handle.close()
        if not record:
            print "Something not ok with : "+str(id)
        else:
            fasta=open(outputpath+str(id)+".fa","w")
            fasta.write(record)
            fasta.close()
    except:
        print "SOMETHING not ok with id : " + str(id)



