folders=`ls -d */`
for folder in $folders; do
    path="/data2/Mulherkar_Lab_Data/$folder"
    cd $path
    fastqs=`ls T*`
    for fastq in $fastqs; do
        python /usr/bin/convert_fastq.py $fastq
    done

done
