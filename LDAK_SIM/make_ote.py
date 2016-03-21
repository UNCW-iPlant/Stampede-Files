#!/usr/bin/python

import sys

def main():
	input_name = sys.argv[1]
	input_file = file(input_name,'r')
	output_name = sys.argv[2]
	output_file = file(output_name,'w')
	lines = []
	for line in input_file.readlines():
		lines.append(line)
	input_file.close()
	for line in lines:
		output_file.write(line.split()[1]+" "+line.split()[4]+"\n")
	output_file.close()

main()
