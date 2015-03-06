"""
Performance measures for testing applications in Winnow
"""


import numpy as np
import pandas as pd
from scipy import stats
import doctest

#Root mean squared error
def rmse(betaColumn, betaTrueFalse):
	betaColumn = np.array(betaColumn)
	betaTrueFalse = np.array(betaTrueFalse)
	return np.mean(np.square(np.subtract(betaColumn, betaTrueFalse)))
""">>>betaColumn=np.array(1,2,3,4,5,6)
>>>betaTrueFalse=np.array("""


#Mean Absolute Error
def mae(betaColumn, betaTrueFalse):
	betaColumn = np.array(betaColumn)
	betaTrueFalse = np.array(betaTrueFalse)
	return np.mean(np.absolute(np.subtract(betaColumn, betaTrueFalse)))


def r(betaColumn, betaTrueFalse):
	betaColumn = np.array(betaColumn)
	betaTrueFalse = np.array(betaTrueFalse)
	return stats.stats.pearsonr(betaColumn, betaTrueFalse)[0]
"""Produces the correlation coefficient
>>>x=[1,2,3,4,5]
>>>y=[5,9,10,12,13]
>>>r(x,y)
0.96457886
"""
def r2(betaColumn, betaTrueFalse):
	betaColumn = np.array(betaColumn)
	betaTrueFalse = np.array(betaTrueFalse)
	return np.square(stats.stats.pearsonr(betaColumn, betaTrueFalse)[0])
"""Produces the coefficient of determination
>>>x=[3,4,5,6,7]
>>>y=[9,10,13,12,18]
>>>r2(x,y)
0.81300813
"""

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
"""Defines the area under the reciever-operator curve
>>>
>>>
>>>
>>
"""
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
"""Returns the error value of the analysis (NOT standard error!)
>>>snpTF=[True,False,True,True,True,False,False,True,False,False,True,False]
>>>threshold=0.05
>>>score=[0.003,0.65,0.004,0.006,0.078,0.003,0.0001,0.513,0.421,0.0081,0.043,0.98]
>>>error(snpTF,threshold,score)

"""

def sens(snpTrueFalse, threshold, scoreColumn):
	truePositives = float(tp(snpTrueFalse, threshold, scoreColumn))
	falseNegatives = float(fn(snpTrueFalse, threshold, scoreColumn))
	return truePositives / (truePositives + falseNegatives)
"""Returns the sensitivty value of the analysis
>>>snpTF=[True,False,True,True,True,False,False,True,False,False,True,False]
>>>threshold=0.05
>>>score=[0.003,0.65,0.004,0.006,0.078,0.003,0.0001,0.513,0.421,0.0081,0.043,0.98]

"""

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
"""Returns the Youden statistic
>>>snpTF=[True,False,True,True,True,False,False,True,False,False,True,False]
>>>threshold = 0.05
>>>score=[0.003,0.65,0.004,0.006,0.078,0.003,0.0001,0.513,0.421,0.0081,0.043,0.98]
>>>youden(snpTF,threshold,score)

"""