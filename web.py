#coding:utf-8
import sys
import numpy as np
import csv

def getAllFieldValue(filename):
	fieldvalues=[]
	fr=open(filename)
	for line in fr.readlines():
		line=line.strip()
		listFromline=line.split('\t')
		if listFromline[0].find('#')==0:
			continue
		else:
			fieldvalues.append(listFromline)
	return fieldvalues
	

def getValues(d,topnum=20):
	result=sorted(d.iteritems(), key=lambda x:x[1],reverse=True)
	finalResult=result[:topnum]
	return finalResult


webs=[]	
values=getAllFieldValue('F:\\data\\2016-06-20\\dns.16_34_14-17_00_00.log')
for i in range(len(values)):
	webs.append(values[i][8])
results={}
for w in webs:
	if webs.count(w)>0:
		results[w]=webs.count(w)

#print getValues(results,20)

#写成文件csv格式
csvfile=file('F:\\MYeclipse\\test2\\WebRoot\\data.csv','wb')
writer=csv.writer(csvfile)
writer.writerow(['key','values'])
writer.writerows(getValues(results,20))
csvfile.close()