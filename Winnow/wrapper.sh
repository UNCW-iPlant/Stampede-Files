#!/bin/bash
#set -x
WRAPPERDIR=$( cd "$( dirname "$0" )" && pwd )

#Load the required arguments here and check if they exist

Class=${Class}
if [[ ! -e "$Class" ]]; then
	echo "Known truth file was not found" >&2
	exit 1
fi

Folder=${Folder}
if [[ ! -e "$Folder" ]]; then
	echo "Input folder was not found" >&2
	exit 1
fi

SNP=${SNP}
if [[ ! -n "$SNP" ]]; then
	echo "Name for SNP column is required" >&2
	exit 1
fi

Score=${Score}
if [[ ! -n "$Score" ]]; then
	echo "Name for significance/p-value column is required" >&2
	exit 1
fi

kttype=${kttype}

#Extra places for the optional arguments and checking their existence
verbose=${verbose}
if [[ "${verbose}" == 'True' ]]; then
	VERBOSE="--verbose"
fi

threshold=${threshold}
if [[ -n "${threshold}" ]]; then
	threshold="--threshold ${threshold}"
fi

beta=${BETA}
if [[ -n "${BETA}" ]]; then
	BETA="--beta ${BETA}"	
fi

seper=${seper}
if [[ -n "$seper" ]]; then
	if [ $seper == "whitespace" -o $seper == "comma" ]; then
		SPACE="--seper $seper"
	fi
fi

kttypeseper=${kttypeseper}
if [[ -n "$kttypeseper" ]]; then
	if [ $kttypeseper == "whitespace" -o $kttypeseper == "comma" ]; then
		KTSPACER="--kttypeseper $kttypeseper"
	fi
fi

#Now to execute the main program...
python ./winpy/winnow.py $VERBOSE --Folder "${Folder}" --Class "${Class}" --Snp "${SNP}" --Score "${Score}" --kttype "$kttype" $threshold $BETA $SPACE $KTSPACER