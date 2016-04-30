#!/bin/bash
#SBATCH -p development
#SBATCH -t 00:30:00
#SBATCH -n 15
#SBATCH -A iPlant-Collabs 
#SBATCH -J test-hdf5_convert

#Testing convert to
mode="to"
directory="test_data/"
output="test_hdf5_out"
../wrapper.sh
