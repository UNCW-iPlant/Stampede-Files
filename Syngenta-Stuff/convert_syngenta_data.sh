#This script assumes you have the PhenoExtracter file 
#and the fastlmmc executable in the folder with the syngenta datasets
module load plink
time while read line
do plink --noweb --file $line --make-bed --out $line
rm *.log *.nosex 
python PhenoExtracter.py -f $line.fam
done < syn_names.txt
