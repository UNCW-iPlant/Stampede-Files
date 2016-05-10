#!/bin/bash
tar -xvf AlphaSim1.04.tar.gz
cp AlphaSimSpec.txt AlphaSim/AlphaSimSpec.txt
cd AlphaSim
chmod +x ./AlphaSim1.04 ./AlphaMate ./AlphaFormatter ./AlphaBayesP ./AlphaBayes ./AlphaAGH ./macs

if [  "${specificationFile}" == *AlphaSimSpec.txt ]; then
	echo "Selection, Chromosomes, and SimulatedData directories will be created within the AlphaSim"
	./AlphaSim1.04
else
	echo "Specification file must be named AlphaSimSpec.txt"
fi
