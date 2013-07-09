files=`find fastas/ -type f -name "*.fa"`
path="/home/saket/my-softwares/NGS-Stuff/new_analysis"
for file in $files ; do
    input="$path/$file"
    output="$path/$file.pssm"
    python nucleotide_content.py $input > $output
done

