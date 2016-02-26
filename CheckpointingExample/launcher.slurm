#!/bin/bash
#
#         <------ Setup Parameters ------>
#
#SBATCH -J Parametric
#SBATCH -n 16
#SBATCH -p development
#SBATCH -o Parametric.o%j
#SBATCH -t 00:05:00

export LAUNCHER_PLUGIN_DIR=$LAUNCHER_DIR/plugins
export LAUNCHER_RMI=SLURM
export LAUNCHER_JOB_FILE=jobfile

$LAUNCHER_DIR/paramrun