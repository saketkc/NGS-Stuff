fasta="/data1/reference_build37/human_g1k_v37.fasta"
aln="$3_aln.sam"
    extension="${1##*.}"
    filename="${1%.*}"
    aln_file1="$filename.sai"
    echo "####################################BWA-ALN-START################################################"
    echo "Starting alignment of $aln_file1 at `date`"
    starttime=`date +%s`
   echo `bwa aln -t 16 $fasta $1 > $aln_file1`
    endtime=`date +%s`
    echo "Ended alignment of $aln_file1 at `date`"
    ((diff_sec=endtime-starttime))
    echo "###TIME-TAKEN###"
    echo - | awk '{printf "%d:%d:%d","'"$diff_sec"'"/(60*60),"'"$diff_sec"'"%(60*60)/60,"'"$diff_sec"'"%60}'
    echo "###h:m:s###"
    echo "####################################BWA-ALN-END################################################"
   
    extension="${2##*.}"
    filename="${2%.*}"
    aln_file2="$filename.sai"
    echo "####################################BWA-ALN-START################################################"
    echo "Starting alignment of $2 at `date`"
    starttime=`date +%s`
    echo `bwa aln -t 16 $fasta $2 > $aln_file2`
    endtime=`date +%s`
    echo "Ended alignment of $2 at `date`"
    ((diff_sec=endtime-starttime))
    echo "###TIME-TAKEN###"
    echo - | awk '{printf "%d:%d:%d","'"$diff_sec"'"/(60*60),"'"$diff_sec"'"%(60*60)/60,"'"$diff_sec"'"%60}'
    echo "###h:m:s###"
    echo "####################################BWA-ALN-END################################################"
    echo "####################################SAMFILE-GENERATATION-START################################################"
    echo "Starting alignment of $3 at `date`"
    starttime=`date +%s`
  #  bwa sampe -r "@rg\tid:@hwusi-eas100r:6:73:941:1973\tpl:illumina\tlb:lib-rdt\tsm:unknown\tpi:200" /data1/amit_dutt_lab/human_g1k_v37.fasta  $aln_file1 $aln_file2 $2 $3 > aln.sam
    bwa sampe -r "@RG\tID:@HWUSI-EAS100R:6:73:941:1973\tPL:ILLUMINA\tLB:LIB-RDT\tSM:$3\tPI:200" /data1/reference_build37/human_g1k_v37.fasta  $aln_file1 $aln_file2 $1 $2 > $aln
    endtime=`date +%s`
    echo "Ended alignment of $3 at `date`"
    ((diff_sec=endtime-starttime))
    echo "###TIME-TAKEN###"
    echo - | awk '{printf "%d:%d:%d","'"$diff_sec"'"/(60*60),"'"$diff_sec"'"%(60*60)/60,"'"$diff_sec"'"%60}'
    echo "###h:m:s###"
    echo "####################################SAMFILE-GENERATATION-END################################################"

echo "####################################FixMateInformation-START################################################"
echo "Fixing Mate Information at `date`"
starttime=`date +%s`
aln_fixed_mates="$3_aln.with.readgroups.fixed.sam"
#echo `java -jar -Xmx20G /usr/bin/picard-tools/AddOrReplaceReadGroups.jar INPUT=aln.sam RGLB=PAIRED_END RGPL=ILLUMINA RGPU=1 RGSM=B2 OUTPUT=aln.with.readgroups.sam`
echo `java -Xmx20G -jar /home/saket/softwares/picard-tools-1.84/FixMateInformation.jar  VALIDATION_STRINGENCY=SILENT INPUT=$aln OUTPUT=$aln_fixed_mates`
endtime=`date +%s`
echo "Ending Fix Mate Information at `date`"
((diff_sec=endtime-starttime))
echo "###TIME-TAKEN###"
echo - | awk '{printf "%d:%d:%d","'"$diff_sec"'"/(60*60),"'"$diff_sec"'"%(60*60)/60,"'"$diff_sec"'"%60}'
echo "###h:m:s###"
echo "####################################FixMateInformation-END################################################"

echo "####################################SAMTOOLS-VALIDATION-START################################################"
echo "Adding READ Groups data at `date`"
starttime=`date +%s`

echo `java -jar /home/saket/softwares/picard-tools-1.84/ValidateSamFile.jar I=$aln_fixed_mates O=validate_sam_file_results.txt`
endtime=`date +%s`
echo "Ended adding READ Groups at `date`"
((diff_sec=endtime-starttime))
echo "###TIME-TAKEN###"
echo - | awk '{printf "%d:%d:%d","'"$diff_sec"'"/(60*60),"'"$diff_sec"'"%(60*60)/60,"'"$diff_sec"'"%60}'
echo "###h:m:s###"
echo "####################################SAMTOOLS-VALIDATION-END################################################"


echo "####################################SAM-TO-BAM-START################################################"
echo "Converting SAM TO BAM at `date`"
starttime=`date +%s`
aln_fixed_mates_bam="$3_aln.with.readgroups.fixed.bam"
#echo `samtools view -bS aln.with.readgroups.fixed.sam > aln.with.readgroups.bam`
echo `java -Xmx20G -jar /home/saket/softwares/picard-tools-1.84/SamFormatConverter.jar I=$aln_fixed_mates O=$aln_fixed_mates_bam VALIDATION_STRINGENCY=SILENT `
endtime=`date +%s`
echo "Ended SAM TO BAM conversion at `date`"
((diff_sec=endtime-starttime))
echo "###TIME-TAKEN###"
echo - | awk '{printf "%d:%d:%d","'"$diff_sec"'"/(60*60),"'"$diff_sec"'"%(60*60)/60,"'"$diff_sec"'"%60}'
echo "###h:m:s###"
echo "####################################SAM-TO-BAM-END################################################"




echo "####################################RMDUP-START################################################"
echo "Starting PCR removal at `date`"
starttime=`date +%s`
aln_rmdup_bam="$3_aln.with.readgroups.fixed.rmdup.bam"
echo `samtools rmdup $aln_fixed_mates_bam $aln_rmdup_bam`
endtime=`date +%s`
echo "Ended PCR removal at `date`"
((diff_sec=endtime-starttime))
echo "###TIME-TAKEN###"
echo - | awk '{printf "%d:%d:%d","'"$diff_sec"'"/(60*60),"'"$diff_sec"'"%(60*60)/60,"'"$diff_sec"'"%60}'
echo "###h:m:s###"
echo "####################################RMDUP-END################################################"

echo "####################################SAM-SORT-START################################################"
echo "Starting PCR removal at `date`"
starttime=`date +%s`
aln_sorted_bam="$3_aln.with.readgroups.fixed.rmdup.sorted"
echo `samtools sort -@ 16 -m 800M $aln_rmdup_bam $aln_sorted_bam`
endtime=`date +%s`
echo "Ended PCR removal at `date`"
((diff_sec=endtime-starttime))
echo "###TIME-TAKEN###"
echo - | awk '{printf "%d:%d:%d","'"$diff_sec"'"/(60*60),"'"$diff_sec"'"%(60*60)/60,"'"$diff_sec"'"%60}'
echo "###h:m:s###"
echo "####################################SAM-SORT-END################################################"

echo "####################################SAM-INDEX-START################################################"
echo "Starting indexing at `date`"
starttime=`date +%s`
aln_sorted_bam="$3_aln.with.readgroups.fixed.rmdup.sorted.bam"
echo `samtools index $aln_sorted_bam`
endtime=`date +%s`
echo "Ended indexing at `date`"
((diff_sec=endtime-starttime))
echo "###TIME-TAKEN###"
echo - | awk '{printf "%d:%d:%d","'"$diff_sec"'"/(60*60),"'"$diff_sec"'"%(60*60)/60,"'"$diff_sec"'"%60}'
echo "###h:m:s###"
echo "####################################SAM-INDEX-END################################################"


echo "####################################SAM-MPILEUP-START################################################"
echo "Starting mpileup at `date`"
starttime=`date +%s`
bcf="$3_samtools_mpileup.raw.bcf"
echo `samtools mpileup -uf $fasta $aln_sorted_bam | bcftools view -bvcg - > $bcf`
endtime=`date +%s`
echo "Ended mpileup at `date`"
((diff_sec=endtime-starttime))
echo "###TIME-TAKEN###"
echo - | awk '{printf "%d:%d:%d","'"$diff_sec"'"/(60*60),"'"$diff_sec"'"%(60*60)/60,"'"$diff_sec"'"%60}'
echo "###h:m:s###"
echo "####################################SAM-MPILEUP-END################################################"

echo "####################################UNMAPPED_READS-EXTRACT-START################################################"
echo "Starting extraction at `date`"
starttime=`date +%s`
unmapped="$3_unmapped_bam.bam"
echo `samtools view -f 0x04 -h -b $aln_sorted_bam -o $unmapped`
endtime=`date +%s`
echo "Ended extraction at `date`"
((diff_sec=endtime-starttime))
echo "###TIME-TAKEN###"
echo - | awk '{printf "%d:%d:%d","'"$diff_sec"'"/(60*60),"'"$diff_sec"'"%(60*60)/60,"'"$diff_sec"'"%60}'
echo "###h:m:s###"
echo "####################################UNMAPPED_READS-EXTRACT-END################################################"

virus_sai="$1.virus.sai";
virus_unmapped="$1.virus.unmapped.bam"
virus_mapped="$1.virus.mapped.bam"
bwa aln -b /data2/Virus_Fasta/Virus_Fasta.fa $unmapped > $virus_sai;
bwa samse /data2/Virus_Fasta/Virus_Fasta.fa $virus_sai $unmapped | samtools view - -Sb -f 0x04 -o $virus_unmapped | samtools view - -Sb -F 0x04 -o $virus_mapped;
