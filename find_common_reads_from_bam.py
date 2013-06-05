import pysam
def calculate_intersection(file1,file2,file3,file4):
    bwa = pysam.Samfile(file1,"rb")
    pssm = pysam.Samfile(file2,"rb")

    unmapped = pysam.Samfile(file3,"rb")
    unmapped_pssm = pysam.Samfile(file4,"rb")
    list1 = [x.qname for x in bwa]
    list2 = [x.qname for x in pssm]

    list3 = [x.qname for x in unmapped]
    list4 = [x.qname for x in unmapped_pssm ]

    set1 = set(list1)
    set2 = set(list2)
    set3 = set(list3)
    set4 = set(list4)

    unmapped_intersect_pssm = set3.intersection(set2)

    unmapped_pssm_intersect_bwa = set4.intersection(set1)

    unmapped_intersect_unmapped_pssm = set3.intersection(set4)
    return str(len(list1))+"\t"+str(len(list2))+"\t"+str(len(list3))+"\t"+str(len(list4))+"\t"+str(len(unmapped_intersect_pssm))+"\t"+str(len(unmapped_pssm_intersect_bwa))+"\t"+str(len(unmapped_intersect_unmapped_pssm))
t755_bwa = "/data2/Cervical_fastq/T755/T755_bwa_sngr_aln.with.readgroups.fixed.rmdup.sorted.bam"
t755_pssm = "/data2/Cervical_fastq/T755/T755_bwapssm_sngr_aln.with.readgroups.fixed.rmdup.sorted.bam"
t755_unmapped = "/data2/Cervical_fastq/unmapped_bams/T755_bwa_sngr_unmapped.bam"
t755_unmapped_pssm = "/data2/Cervical_fastq/T755/T755_bwapssm_sngr_unmapped.bam"

t783_bwa = "/data2/Cervical_fastq/T785/T785_bwa_sngr_aln.with.readgroups.fixed.rmdup.bam"
t783_pssm = "/data2/Cervical_fastq/T785/T785_bwappsm_aln.with.readgroups.fixed.bam"
t783_unmapped ="/data2/Cervical_fastq/unmapped_bams/T785_bwa_sngr_unmapped.bam"
t783_unmapped_pssm = "/data2/Cervical_fastq/T785/T785_bwapssm_sngr_unmapped.bam"


t837_bwa = "/data2/Cervical_fastq/T837/T837_bwa_sngr_aln.with.readgroups.fixed.rmdup.sorted.bam"
t837_pssm = "/data2/Cervical_fastq/T837/T837_bwapssm_sngr_aln.with.readgroups.fixed.rmdup.sorted.bam"
t837_unmapped = "/data2/Cervical_fastq/unmapped_bams/T837_bwa_sngr_unmapped.bam"
t837_unmapped_pssm = "/data2/Cervical_fastq/T837/T837_bwapssm_sngr_unmapped.bam"

t887_bwa = "/data2/Cervical_fastq/T887/T887_bwapssm_sngr_aln.with.readgroups.fixed.rmdup.sorted.bam"
t887_pssm = "/data2/Cervical_fastq/T887/T887_bwapssm_sngr_aln.with.readgroups.fixed.rmdup.sorted.bam"
t887_unmapped = "/data2/Cervical_fastq/unmapped_bams/T887_bwa_sngr_unmapped.bam"
t887_unmapped_pssm = "/data2/Cervical_fastq/T887/T887_bwapssm_sngr_unmapped.bam"

#t937_bwa = "/data2/Cervical_fastq/T937/T937_bwa_aln.with.readgroups.fixed.rmdup.sorted.bam"
#t937_pssm = "/data2/Cervical_fastq/T937/T937_bwa"


bams = [
    {"bwa":t755_bwa,"pssm":t755_pssm,"unmapped":t755_unmapped, "unmapped_pssm": t755_unmapped_pssm, "name":"T755"},
    {"bwa":t783_bwa,"pssm":t783_pssm,"unmapped":t783_unmapped, "unmapped_pssm": t783_unmapped_pssm, "name": "T783"},
    {"bwa":t837_bwa,"pssm":t755_pssm,"unmapped":t837_unmapped, "unmapped_pssm": t837_unmapped_pssm, "name": "T837"},
    {"bwa":t887_bwa,"pssm":t887_pssm,"unmapped":t887_unmapped, "unmapped_pssm": t887_unmapped_pssm, "name": "T887"},

        ]
print "Sample\tBWA\tPSSM\tUnmapped-BWA\tUnmapped-PSSM\tUnmapped-BWA-i-PSSM\tUnmapped-PSSM-i-BWA\tUnmapped-BWA-i-Unmapped-PSSM"
for dicts in bams:
    print dicts["name"]+ "\t", calculate_intersection(dicts["bwa"],dicts["pssm"],dicts["unmapped"], dicts["unmapped_pssm"])
