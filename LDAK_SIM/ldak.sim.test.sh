#!/bin/bash
#SBATCH -p normal
#SBATCH -t 00:30:00
#SBATCH -n 1
#SBATCH -A iPlant-Collabs
#SBATCH -J LDAK-SIM-TEST.o
#SBATCH -o LDAK-SIM-TEST.o%j

simOutputName="output"
phenoOutputName="phenos"
numSNPS=1000000
numSamples=1000
numCausals=100
numPhenos=1
heritability=0.8
minmaf=0.01
maxmaf=0.04

ldak.5.94 --make-snps ${simOutputName} --num-snps ${numSNPS} --num-samples ${numSamples} --minmaf ${minmaf} --maxmaf ${maxmaf} 

ldak.5.94 --make-phenos ${phenoOutputName} --bfile ${simOutputName} --num-causals ${numCausals} --num-phenos ${numPhenos} --her ${heritability}

python make_ote.py ${phenoOutputName}.effects ${phenoOutputName}_effects.ote
