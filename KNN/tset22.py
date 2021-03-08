
# -*- coding: utf-8 -*-  

from numpy import *
import operator

##给出训练数据以及对应的类别
def createDataSet():
    group = array([[1.0,2.0],[1.2,0.1],[0.1,1.4],[0.3,3.5]])
    labels = ['A','A','B','B']
    return group,labels

###通过KNN进行分类
def classify(input,dataSet,label,k):
	dataSize=dataSet.shape[0]
	diff = tile(input,(dataSize,1))-dataSet
	sqdiff=diff**2
	squareDist=sum(sqdiff,axis=1)
	dist=squareDist**0.5
	sorted=argsort(dist)
	classCount={}
	for i in range(k):
		votelabel=label[sorted[i]]
		classCount[votelabel]=classCount.get(votelabel,0)+1
	maxCount=0
	for key,value in classCount.items():
		if value >maxCount:
			maxCount=value
			keyc=key
	return keyc

dataSet,labels = createDataSet()
input = array([1.1,0.3])
K = 3
output = classify(input,dataSet,labels,K)
print ("测试数据为:",input,"分类结果为：",output)











