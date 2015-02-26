#!/bin/bash
#SBATCH -J SyngentaAnalysis # job name
#SBATCH -o Synout.o%j # output and error file name (%j expands to jobID)
#SBATCH -n 1 # total number of mpi tasks requested
#SBATCH -p normal # queue (partition) -- normal, development, etc.
#SBATCH -t 24:00:00 # run time (hh:mm:ss) - 24 hours
#SBATCH -A iPlant-Collabs
#SBATCH --mail-user=spt6655@uncw.edu
#SBATCH --mail-type=end # email me when the job finishes

while read line
do fastlmmc -verboseOutput -bfile $line -fileSim $line -pheno $line.fam_pheno.txt -simOut $line.sim.txt;
fastlmmc -verboseOutput -bfile $line -sim $line.sim.txt -pheno $line.fam_pheno.txt -out $line.Results.txt;
done < syn_names.txt
