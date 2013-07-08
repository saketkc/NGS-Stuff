#!/usr/bin/env python
import urllib2
import re
txt_ftp_location = "ftp://ftp.ncbi.nlm.nih.gov/genomes/GENOME_REPORTS/viruses.txt"
handle = open("papillomavirus.txt","r")
response = handle.read()
handle.close()
project_ids = [line for line in response.splitlines()]
outputpath="/home/saket/my-softwares/NGS-Stuff/new_analysis/fastas/"
#project_ids=["X74475"]
for id in project_ids:
    try:
        handle = urllib2.urlopen("http://www.ebi.ac.uk/ena/data/view/"+str(id)+"&display=fasta")
#        print handle.geturl()
        record = handle.read()
#        print type(record)
#        handle.close()
#        print record
        if record=="":
            print record
            print "Something not ok with : "+str(id)
        else:
            fasta=open(outputpath+str(id)+".fa","w")
            fasta.write(record)
            fasta.close()
    except:
        print "SOMETHING not ok with id : " + str(id)



