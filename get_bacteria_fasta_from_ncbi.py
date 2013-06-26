import urllib2
from Bio import Entrez,SeqIO
import csv
txt_ftp_location = "ftp://ftp.ncbi.nlm.nih.gov/genomes/GENOME_REPORTS/prok_reference_genomes.txt"
#txt_ftp_location = "ftp://ftp.ncbi.nlm.nih.gov/genomes/GENOME_REPORTS/viruses.txt"
handle = urllib2.urlopen(txt_ftp_location)
response = handle.read()
reader = csv.reader(response.splitlines(), delimiter='\t')
project_ids =[]
outputpath="/data2/Bacteria_Fasta/"
for row in reader:
    project_ids.append(row[3].strip())

Entrez.email = "saketkc@gmail.com"
for id in project_ids:
    handle = Entrez.elink(dbfrom="bioproject", id=id, linkname="bioproject_nuccore")
    record = Entrez.read(handle)
    handle.close()
    if record[0]["LinkSetDb"]:
        id_list = record[0]["LinkSetDb"][0]["Link"]
        nuccore_ids = []
        for link in id_list:
            nuccore_ids.append(link['Id'])

        handle = Entrez.efetch(db="nuccore", id=nuccore_ids, rettype="fasta", retmode="text")
        records = list(SeqIO.parse(handle, "fasta"))
        handle.close()
            # Save them all in one fasta file
        all_ids = (".").join(nuccore_ids)
        SeqIO.write(records, outputpath+"bioprojectId:"+str(id) +"-len:"+ str(len(records)) + "-nuccore-ids:" +all_ids +"-sequences.fasta", "fasta")



