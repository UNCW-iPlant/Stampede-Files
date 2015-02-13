"""
Performance measures for testing applications in Winnow
"""


import numpy as np
import pandas as pd
from scipy import stats
import random


def rmse(betaColumn, betaTrueFalse):
	betaColumn = np.array(betaColumn)
	betaTrueFalse = np.array(betaTrueFalse)
	return np.mean(np.square(np.subtract(betaColumn, betaTrueFalse)))


def mae(betaColumn, betaTrueFalse):
	betaColumn = np.array(betaColumn)
	betaTrueFalse = np.array(betaTrueFalse)
	return np.mean(np.absolute(np.subtract(betaColumn, betaTrueFalse)))


def r(betaColumn, betaTrueFalse):
	betaColumn = np.array(betaColumn)
	betaTrueFalse = np.array(betaTrueFalse)
	return stats.stats.pearsonr(betaColumn, betaTrueFalse)[0]


def r2(betaColumn, betaTrueFalse):
	betaColumn = np.array(betaColumn)
	betaTrueFalse = np.array(betaTrueFalse)
	return np.square(stats.stats.pearsonr(betaColumn, betaTrueFalse)[0])


def auc(snpTrueFalse, scoreColumn):
	scoreColumn = np.array(scoreColumn)
	snpTrueFalse = np.array(snpTrueFalse)
	x1 = scoreColumn[snpTrueFalse == True]
	n1 = x1.size
	x2 = scoreColumn[snpTrueFalse == False]
	n2 = x2.size
	r = stats.rankdata(np.hstack((x1,x2)))
	auc = (np.sum(r[0:n1]) - n1 * (n1+1)/2) / (n1 * n2)
	return 1 - auc


def tp(snpTrueFalse, threshold, scoreColumn):
	testColumn = list()
	for each in scoreColumn:
		if float(each) < threshold:
			testColumn.append(True)
		else:
			testColumn.append(False)
	count = 0
	truePositives = 0
	for each in testColumn:
		if each is True and snpTrueFalse[count] is True:
			truePositives += 1
		count += 1
	return truePositives


def fp(snpTrueFalse, threshold, scoreColumn):
	testColumn = list()
	for each in scoreColumn:
		if float(each) < threshold:
			testColumn.append(True)
		else:
			testColumn.append(False)
	count = 0
	falsePositives = 0
	for each in testColumn:
		if each is True and snpTrueFalse[count] is False:
			falsePositives += 1
		count += 1
	return falsePositives


def tn(snpTrueFalse, threshold, scoreColumn):
	testColumn = list()
	for each in scoreColumn:
		if float(each) < threshold:
			testColumn.append(True)
		else:
			testColumn.append(False)
	count = 0
	trueNegatives = 0
	for each in testColumn:
		if each is False and snpTrueFalse[count] is False:
			trueNegatives += 1
		count += 1
	return trueNegatives


def fn(snpTrueFalse, threshold, scoreColumn):
	testColumn = list()
	for each in scoreColumn:
		if float(each) < threshold:
			testColumn.append(True)
		else:
			testColumn.append(False)
	count = 0
	falseNegatives = 0
	for each in testColumn:
		if each is False and snpTrueFalse[count] is True:
			falseNegatives += 1
		count += 1
	return falseNegatives


def tpr(snpTrueFalse, threshold, scoreColumn):
	truePositives = tp(snpTrueFalse, threshold, scoreColumn)
	count = 0.0
	for each in snpTrueFalse:
		if each is True:
			count += 1.0
	return float(truePositives/count)


def fpr(snpTrueFalse, threshold, scoreColumn):
	falsePositives = fp(snpTrueFalse, threshold, scoreColumn)
	count = 0.0
	for each in snpTrueFalse:
		if each is False:
			count += 1.0
	return float(falsePositives/count)


def error(snpTrueFalse, threshold, scoreColumn):
	truePositives = float(tp(snpTrueFalse, threshold, scoreColumn))
	falsePositives = float(fp(snpTrueFalse, threshold, scoreColumn))
	trueNegatives = float(tn(snpTrueFalse, threshold, scoreColumn))
	falseNegatives = float(fn(snpTrueFalse, threshold, scoreColumn))
	return (falseNegatives + falsePositives) / (truePositives + trueNegatives + falsePositives + falseNegatives)


def sens(snpTrueFalse, threshold, scoreColumn):
	truePositives = float(tp(snpTrueFalse, threshold, scoreColumn))
	falseNegatives = float(fn(snpTrueFalse, threshold, scoreColumn))
	return truePositives / (truePositives + falseNegatives)


def spec(snpTrueFalse, threshold, scoreColumn):
	trueNegatives = float(tn(snpTrueFalse, threshold, scoreColumn))
	falsePositives = float(fp(snpTrueFalse, threshold, scoreColumn))
	return trueNegatives / (trueNegatives + falsePositives)


def precision(snpTrueFalse, threshold, scoreColumn):
	truePositives = float(tp(snpTrueFalse, threshold, scoreColumn))
	falsePositives = float(fp(snpTrueFalse, threshold, scoreColumn))
	return truePositives / (truePositives + falsePositives)


def youden(snpTrueFalse, threshold, scoreColumn):
	sensitivity = float(sens(snpTrueFalse, threshold, scoreColumn))
	specificity = float(spec(snpTrueFalse, threshold, scoreColumn))
	return sensitivity + specificity - 1.0
