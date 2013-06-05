fasta="/data1/reference_build37/human_g1k_v37.fasta"
aln="$4_aln.sam"
if [ "$1" == "bowtie2" ]
then
    fasta="$bowtie_fasta"
    echo "####################################BOWTIE2-ALN-START################################################"
    echo "Starting alignment of $2 at `date`"
    starttime=`date +%s`
    echo `bowtie2 -x /data2/Amit_Dutt_Lab/human_g1k_v37_bowtie2/human_g1k_v37 -1 $2 -2 $3 -S $aln`
    endtime=`date +%s`
    echo "Ended alignment of $2 at `date`"
    ((diff_sec=endtime-starttime))
    echo "###TIME-TAKEN###"
    echo - | awk '{printf "%d:%d:%d","'"$diff_sec"'"/(60*60),"'"$diff_sec"'"%(60*60)/60,"'"$diff_sec"'"%60}'
    echo "###h:m:s###"
    echo "####################################BOWTIE2-ALN-END################################################"
fi
if [ "$1" == "bwa" ]
then
    extension="${2##*.}"
    filename="${2%.*}"
    aln_file1="$filename.sai"
    echo "####################################BWA-ALN-START################################################"
    echo "Starting alignment of $aln_file1 at `date`"
    starttime=`date +%s`
   echo `bwa aln -t 8 $fasta $2 > $aln_file1`
    endtime=`date +%s`
    echo "Ended alignment of $aln_file1 at `date`"
    ((diff_sec=endtime-starttime))
    echo "###TIME-TAKEN###"
    echo - | awk '{printf "%d:%d:%d","'"$diff_sec"'"/(60*60),"'"$diff_sec"'"%(60*60)/60,"'"$diff_sec"'"%60}'
    echo "###h:m:s###"
    echo "####################################BWA-ALN-END################################################"
   
    extension="${3##*.}"
    filename="${3%.*}"
    aln_file2="$filename.sai"
    echo "####################################BWA-ALN-START################################################"
    echo "Starting alignment of $3 at `date`"
    starttime=`date +%s`
    echo `bwa aln  -t 8 $fasta $3 > $aln_file2`
    endtime=`date +%s`
    echo "Ended alignment of $3 at `date`"
    ((diff_sec=endtime-starttime))
    echo "###TIME-TAKEN###"
    echo - | awk '{printf "%d:%d:%d","'"$diff_sec"'"/(60*60),"'"$diff_sec"'"%(60*60)/60,"'"$diff_sec"'"%60}'
    echo "###h:m:s###"
    echo "####################################BWA-ALN-END################################################"
    echo "####################################SAMFILE-GENERATATION-START################################################"
    echo "Starting alignment of $3 at `date`"
    starttime=`date +%s`
  #  bwa sampe -r "@rg\tid:@hwusi-eas100r:6:73:941:1973\tpl:illumina\tlb:lib-rdt\tsm:unknown\tpi:200" /data1/amit_dutt_lab/human_g1k_v37.fasta  $aln_file1 $aln_file2 $2 $3 > aln.sam
    bwa sampe -r "@RG\tID:@HWUSI-EAS100R:6:73:941:1973\tPL:ILLUMINA\tLB:LIB-RDT\tSM:UNKNOWN\tPI:200" /data1/reference_build37/human_g1k_v37.fasta  $aln_file1 $aln_file2 $2 $3 > $aln
    endtime=`date +%s`
    echo "Ended alignment of $3 at `date`"
    ((diff_sec=endtime-starttime))
    echo "###TIME-TAKEN###"
    echo - | awk '{printf "%d:%d:%d","'"$diff_sec"'"/(60*60),"'"$diff_sec"'"%(60*60)/60,"'"$diff_sec"'"%60}'
    echo "###h:m:s###"
    echo "####################################SAMFILE-GENERATATION-END################################################"
fi
if [ "$1" == "soap" ]
then
    fasta="$soap_fasta"
    echo "####################################SOAP-ALN-START################################################"
    echo "Starting alignment of $2 and $3 at `date`"
    starttime=`date +%s`
    echo `soap -a $2 -b $3 -D $fasta -o soap_aln_paired.soap -2 soap_aln_single.soap `
    endtime=`date +%s`
    echo "Ended alignment of $2 and $3 at `date`"
    ((diff_sec=endtime-starttime))
    echo "###TIME-TAKEN###"
    echo - | awk '{printf "%d:%d:%d","'"$diff_sec"'"/(60*60),"'"$diff_sec"'"%(60*60)/60,"'"$diff_sec"'"%60}'
    echo "###h:m:s###"
    echo "####################################SOAP-ALN-END################################################"
    echo "####################################SAMFILE-GENERATATION-START################################################"
    echo "Converting SOAP to SAM at `date`"
    starttime=`date +%s`
    echo `perl /usr/bin/soap2sam.pl soap_aln_paired.soap > aln.sam`
    endtime=`date +%s`
    echo "Ended SOAP to SAM conversion at `date`"
    ((diff_sec=endtime-starttime))
    echo "###TIME-TAKEN###"
    echo - | awk '{printf "%d:%d:%d","'"$diff_sec"'"/(60*60),"'"$diff_sec"'"%(60*60)/60,"'"$diff_sec"'"%60}'
    echo "###h:m:s###"
    echo "####################################SAMFILE-GENERATATION-END################################################"
    
fi
#echo "####################################ADD-READGROUPS-START################################################"
#echo "Adding READ Groups data at `date`"
#starttime=`date +%s`
#echo `java -jar /home/saket/softwares/picard-tools-1.84/AddOrReplaceReadGroups.jar INPUT=aln.sam RGLB=PAIRED_END RGPL=ILLUMINA RGPU=1 RGSM=ACTREC4 OUTPUT=aln.with.readgroups.sam`
#endtime=`date +%s`
#echo "Ended adding READ Groups at `date`"
#((diff_sec=endtime-starttime))
#echo "###TIME-TAKEN###"
#echo - | awk '{printf "%d:%d:%d","'"$diff_sec"'"/(60*60),"'"$diff_sec"'"%(60*60)/60,"'"$diff_sec"'"%60}'
#echo "###h:m:s###"
#echo "####################################ADD-READGROUPS-END################################################"

echo "####################################FixMateInformation-START################################################"
echo "Fixing Mate Information at `date`"
starttime=`date +%s`
aln_fixed_mates="$4_aln.with.readgroups.fixed.sam"
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
aln_fixed_mates_bam="$4_aln.with.readgroups.fixed.bam"
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
aln_rmdup_bam="$4_aln.with.readgroups.fixed.rmdup.bam"
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
aln_sorted_bam="$4_aln.with.readgroups.fixed.rmdup.sorted"
echo `samtools sort $aln_rmdup_bam $aln_sorted_bam`
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
aln_sorted_bam="$4_aln.with.readgroups.fixed.rmdup.sorted.bam"
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
bcf="$4_samtools_mpileup.raw.bcf"
echo `samtools mpileup -uf $fasta $aln_sorted_bam | bcftools view -bvcg - > $bcf`
endtime=`date +%s`
echo "Ended mpileup at `date`"
((diff_sec=endtime-starttime))
echo "###TIME-TAKEN###"
echo - | awk '{printf "%d:%d:%d","'"$diff_sec"'"/(60*60),"'"$diff_sec"'"%(60*60)/60,"'"$diff_sec"'"%60}'
echo "###h:m:s###"
echo "####################################SAM-MPILEUP-END################################################"

echo "####################################GATK-INDEL-START################################################"
echo "Starting indelaligner at `date`"
starttime=`date +%s`
vcf="$4_gatk_unified_genotyper.vcf"
log="$4_gatk_unified_genotyper.log"
java -Xmx20G -jar ~/GenomeAnalysisTK-1.6-9-g47df7bb/GenomeAnalysisTK.jar -T UnifiedGenotyper -R /data1/reference_build37/human_g1k_v37.fasta -I $aln_sorted_bam -o $vcf --genotype_likelihoods_model BOTH --annotateNDA -l INFO -log $log

#echo `java  -Xmx20G -jar /home/saket/softwares/GenomeAnalysisTK-2.3-9/GenomeAnalysisTK.jar -I aln.with.readgroups.baq.rmdup.sorted.bam -R $fasta -T RealignerTargetCreator  -o forIndelRealigner.intervals  -et NO_ET -K /home/saket/softwares/saket.kumar_iitb.ac.in.key`
endtime=`date +%s`
echo "Ended IndelRealigner at `date`"
((diff_sec=endtime-starttime))
echo "###TIME-TAKEN###"
echo - | awk '{printf "%d:%d:%d","'"$diff_sec"'"/(60*60),"'"$diff_sec"'"%(60*60)/60,"'"$diff_sec"'"%60}'
echo "###h:m:s###"
echo "####################################GATK-INDEL-END################################################"

