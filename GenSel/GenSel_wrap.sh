#!/bin/bash

# Load inputs/arguments here
# Note that most of these options have been pulled from the GenSel v3 manual
geno_data=${genotypic_data}
pheno_data=${phenotypic_data}
includeRange='${includeRange}'
excludeFilename='${excludeFilename}'
analysisType='${analysisType}'
varGenotypic='${varGenotypic}'
varResidual='${varResidual}'

# No checks on these first two since they are always required 
echo 'markerFileName	$geno_data' >> command_file.txt
echo 'phenotypeFileName		$pheno_data' >> command_file.txt

# Check if the others exist since they are all optional
# May consider adding others depending on the full list of analysis types and arguments
if [ ! -z $includeRange ];
	echo 'includeRange	$includeRange' >> command_file.txt
fi

if [ ! -z $excludeFilename ];
	echo 'excludeFileName	$excludeFilename' >> command_file.txt
fi

if [ ! -z $analysisType ];
	echo 'analysisType	$analysisType' >> command_file.txt
fi

if [ ! -z $varGenotypic ];
	echo 'varGenotypic	$varGenotypic' >> command_file.txt
fi

if [ ! -z $analysisType ];
	echo 'varResidual	$varResidual' >> command_file.txt
fi 

# Run the program with the created command file
GenSel command_file.txt