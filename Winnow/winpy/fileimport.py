"""
Functions to import both class and results folder files
"""


import os, data, csv


def getList(folder):
	return os.listdir(folder)


def loadFile(folder, thisFile, seper):
	return data.Data(folder + "/" + thisFile, seper, skiprow=False)


def loadKT(thisFile, seper):
	return data.Data(thisFile, seper, skiprow=True)


def trueFalse(currentSnp, ktSnps):
	if currentSnp in ktSnps:
		return True
	else:
		return False


def writeCSV(filename, keepToWrite, method="wb", exportDelimiter=","):
	with open(filename + ".txt", method) as openFile:
		openFileWriter = csv.writer(openFile, delimiter=exportDelimiter)
		if method == "wb":
			openFileWriter.writerow(keepToWrite[0])
		currentRow = list()
		for item in keepToWrite[1]:
			currentRow.append(item)
		openFileWriter.writerow(currentRow)