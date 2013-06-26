## A script to gzip 
## files in a given folder on maximum possible cores with maximum compression


## Run as : 
## user@laptop$ bash gzip_everything.sh foldername
# find -print0 / xargs -0 protects you from whitespace in filenames
# xargs -n 1 means one gzip process per file
# xargs -P specifies the number of jobs
# gzip -9 means maximum compression

#source : http://stackoverflow.com/questions/4341442/gzip-with-all-cores




CORES=$(grep -c '^processor' /proc/cpuinfo)
find $1 -type f -print0 | xargs -0 -n 1 -P $CORES gzip -9


