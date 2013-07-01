import os
import glob
dirs=[x[0] for x in os.walk("/data1/Virus_NCBI/")]
all_files=[]
for directory in dirs:
    os.chdir(directory)
    for files in glob.glob("*.fna"):
        all_files.append(directory+'/'+files)

with open("/data1/Virus_NCBI/master_virus.fa","w") as outfile:
    for fname in all_files:
        with open(fname) as infile:
            outfile.write(infile.read())

#print all_files
