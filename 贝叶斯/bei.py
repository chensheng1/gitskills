#!/usr/bin/python  
# -*- coding: utf-8 -*-  
#coding=utf-8

from numpy import *

#词表到向量的转换函数
#数据来自斑点犬爱好者留言板
def loadDataSet():
    postingList = [['my', 'dog', 'has', 'flea', \
                    'problems', 'help', 'please'],
                   ['maybe', 'not', 'take', 'him', \
                    'to', 'dog', 'park', 'stupid'],
                   ['my', 'dalmation', 'is', 'so', 'cute', \
                    'I', 'love', 'him'],
                   ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                   ['mr', 'licks', 'ate', 'my', 'steak', 'how', \
                    'to', 'stop', 'him'],
                   ['quit', 'buying', 'worthless', 'dot', 'food', 'stupid']]
    classVec = [0, 1, 0, 1, 0, 1]  #1代表侮辱性文字，0代表正常言论
    return postingList, classVec


#创建一个包含在所有文档中出现的不重复词的列表
def createVocabList(dataSet):
    vocabSet = set([])   #创建一个空集
    for document in dataSet:
        vocabSet = vocabSet | set(document)  #创建两个集合的并集
    return list(vocabSet)


#输入参数为词汇表及某个文档，输出的是文档向量
def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0]*len(vocabList)  #创建一个其中所含元素都为0的向量
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1  #1表示词汇表中的单词在文档中出现过
        else:
            print "the word: %s is not in my Vocabulary!" % word
    return returnVec
	
	
#朴素贝叶斯分类器训练函数
#输入参数为文档矩阵，每篇文档类别标签所构成的向量
def trainNB0(trainMatrix, trainCategory):
    numTrainDocs = len(trainMatrix)  #文档篇数
    numWords = len(trainMatrix[0])   #单词数
    pAbusive = sum(trainCategory)/float(numTrainDocs)  #侮辱性文档的概率
    p0Num = ones(numWords); p1Num = ones(numWords)  #初始化概率，修正
    p0Denom = 2.0; p1Denom = 2.0   #修正
    for i in range(numTrainDocs):  #对于每篇训练文档
        if trainCategory[i] == 1:  #对于每个训练类别
            p1Num += trainMatrix[i]  #如果词条出现在文档中，增加该词条的计数值。向量相加
            p1Denom += sum(trainMatrix[i]) #增加所有词条的计数值
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    #每个类别的条件概率
    p1Vect = log(p1Num/p1Denom)  #修正
    p0Vect = log(p0Num/p0Denom)
    return p0Vect, p1Vect, pAbusive

	
#朴素贝叶斯分类函数
def classifyNB(vec2Classify, p0Vec, p1Vec, pClass):
    p1 = sum(vec2Classify * p1Vec) + log(pClass)
    p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass)
    if p1 > p0:
        return 1
    else:
        return 0

#测试函数
def testingNB():
    listOPosts, listClasses = loadDataSet()
    myVocabList = createVocabList(listOPosts)
    trainMat = []
    for postinDoc in listOPosts:
        trainMat.append(setOfWords2Vec(myVocabList, postinDoc))
    p0V, p1V, pAb = trainNB0(array(trainMat), array(listClasses))
    testEntry = ['love', 'my', 'dalmation']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print testEntry, 'classified as: ', classifyNB(thisDoc, p0V, p1V, pAb)
    testEntry = ['stupid', 'garbage']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print testEntry, 'classified as: ', classifyNB(thisDoc, p0V, p1V, pAb)
	
if __name__=='__main__':
	listOPosts, listClasses = loadDataSet()
	myVocabList = createVocabList(listOPosts)
	trainMat=[]
	for postinDoc in listOPosts:
		trainMat.append(setOfWords2Vec(myVocabList,postinDoc))
	poV,p1V,pAb=trainNB0(trainMat,listClasses)
	testingNB()
	print pAb,poV,p1V