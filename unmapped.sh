unmapped="$2.unmapped.bam"
sai="$2.virus.sai"
all_virus="$2.virus.bam"
unmapped_virus="$2.virus.unmappped.bam"
mapped_virus="$2.virus.mapped.bam"

samtools view -f 0x04 -h -b $1 -o $unmapped
bwa aln -b $3 $unmapped > $sai
bwa samse -r "@RG\tID:$2\tPL:ILLUMINA" $3 $sai $unmapped | samtools view - -Sb -o $all_virus; samtools view $all_virus -b -F 0x04 -o $mapped_virus; samtools view $all_virus -b -f 0x04 -o $unmapped_virus;
echo "MAPPED READS"
samtools view -c $mapped_virus
samtools view -c $unmapped_virus
