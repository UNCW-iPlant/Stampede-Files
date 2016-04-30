#!/bin/bash

if [ -z ${directory} ]; then
	echo "Invalid directory argument: ${directory}"
else
	ARGS="--dir ${directory}"
fi

if [ "${mode}" == "to" ]; then
	ARGS="to ${ARGS}"
	if [ -z ${output} ]; then
		echo "Output name is set as default"
	else
		ARGS="${ARGS} --output ${output}"
	fi
	if [ -z ${collength} ]; then
		echo "Using default column length"
	else
		ARGS="${ARGS} --collength ${collength}"
	fi
elif [ "${mode}" == "from" ]; then
	ARGS="from ${ARGS}"
	if [ -z ${hdf5File} ]; then
		"echo Invalid input file"
	else
		ARGS="${ARGS} --hdf ${hdf5File}"
	fi
else
	echo "Invalid mode argument: ${mode}"
fi
