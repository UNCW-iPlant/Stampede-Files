#!/bin/bash
#SBATCH -J SyngentaAnalysis4 # job name
#SBATCH -o Synout.o%j # output and error file name (%j expands to jobID)
#SBATCH -n 1 # total number of mpi tasks requested
#SBATCH -N 1
#SBATCH -c 4
#SBATCH -p normal # queue (partition) -- normal, development, etc.
#SBATCH -t 36:00:00 # run time (hh:mm:ss) - 24 hours
#SBATCH -A iPlant-Collabs
#SBATCH --mail-user=spt6655@uncw.edu
#SBATCH --mail-type=end # email me when the job finishes

while read line
do time fastlmmc -verboseOutput -bfile $line -fileSim $line -pheno $line.fam_pheno.txt -simOut $line.sim.txt;
time fastlmmc -verboseOutput -bfile $line -sim $line.sim.txt -pheno $line.fam_pheno.txt -out $line.Results.txt;
rm $line.bed $line.bim $line.fam
mv $line.Results.txt $WORK/Syngenta_Results
done < SynNames3.txt
#Clean up remaining outputs
rm *.out.txt