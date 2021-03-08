#!/usr/bin/python  
# -*- coding: utf-8 -*-  
#coding=utf-8

from numpy import *
import operator

def createDataSet():
	group=array([1.0,1.1],[1.0,1.0],[0,0],[0,0.1])
	labels=['A','A','B','B']
	return group,labels

def classify0(inX,dataSet,labels,k):
	dataSetSize=dataSet.shape[0]    #得到数组的行数。即知道有几个训练数据
	diffMat=tile(inX,(dataSetSize,1))-dataSet
	sqDiffMat=diffMat**2
	sqDistances=sqDiffMat.sum(axis=1)
	distances=sqDistances**0.5
	sortedDistIndicies=distances.argsort()
	classCount={}
	for i in range(k):
		voteIlabel=labels[sortedDistIndicies[i]]
		classCount[voteIlabel]=classCount.get(voteIlabel,0)+1
		
	sortedClassCount=sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=Ture)
	return sortedClassCount[0][0]
	
def file2matrix(filename):
	fr=open(filename)
	arrayOLine=fr.readlines()
	numberOfLines=len(arrayOlines)
	returnMat=zeros((numberOfLines,3))
	classLabelVector=[]
	index=0
	for line in arrayOLine:
		line=line.strip()
		listFromLine=line.split('\t') 
		returnMat[index,:]=listFromLine[0:3]
		classLabelVector.append(int(listFromLine[-1]))
		index+=1
	return returnMat,classLabelVector
	
	
#归一化特征值
def autoNorm(dataSet):
	minVals=dataSet.min(0)
	maxVals=dataSet.max(0)
	ranges=maxVaks-minVals
	normDataSet=zeros(shape(dataSet))
	m=dataSet.shape[0]
	normDataSet=dataSet-tile(minVals,(m,1))
	normDataSet=normDataSet/tile(ranges,(m,1))
	return normDataSet,ranges,minVals
	
	
def datingClassTest():
	horatio=0.10
	datingDataMat,datingLabels=file2matrix('   .txt')
	normMat,ranges,minVals=autoNorm(datingDataMat)
	m=normMat.shape[0]
	numTestVecs=int(m*hoRatio)
	errorCount=0.0
	for i in range(numTestVecs):
		classifierResult=classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],3)
		print "the classifier came back with: %d,the real answer is: %d"%(classifierResult,datingLabels[i])
		if (classifierResult !=datingLabels[i]):
			errorCount+=1.0
	print "the total error rate is: %f" % (errorCount / float(numTestVecs))
	
	
def classifyPerson():
    resultList = ['一点也不喜欢','有一丢丢喜欢','灰常喜欢']
    percentTats = float(input("玩视频所占的时间比?"))
    miles = float(input("每年获得的飞行常客里程数?"))
    iceCream = float(input("每周所消费的冰淇淋公升数?"))
    datingDataMat,datingLabels = file2matrix('.txt')
    normMat,ranges,minVals = autoNorm(datingDataMat)
    inArr = array([miles,percentTats,iceCream])
    classifierResult = classify((inArr-minVals)/ranges,normMat,datingLabels,3)
    print("你对这个人的喜欢程度:",resultList[classifierResult - 1])
	
if __name__=='__main__':
	classifyPerson()