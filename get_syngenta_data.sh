cd $WORK
module load irods/3.3.1
timeout 45m iget -V -r -T -f /iplant/home/shared/syngenta_sim/PEDMAP_DE
#Can change this timeout to end after X amount of time
cd ./PEDMAP_DE
ls *.ped > Names.txt
sed 's/\..*$//' Names.txt > syn_names.txt
rm Names.txt
