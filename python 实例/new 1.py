#-*- coding: utf-8 -*-

from pylab import *

mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

"""统计源ip流量"""


import sys
import numpy as np
import matplotlib.pyplot as plt


###取得所有字段及其值
def getAllFieldValue(filename):
    fieldvalue=[]
    fr=open(filename)
    for line in fr.readlines():
        line=line.strip()
        listFromLine=line.split('\t')
        if listFromLine[0].find('#')==0:
            continue
        else:
            fieldvalue.append(listFromLine)
    return fieldvalue
	
	
#####第一步：从文件中取得ip及其对应的bytes   
ip=[]

bytes=[]
values=getAllFieldValue('F:\\data\\2016-06-20\\conn.16_34_20-17_00_00.log')
for i in xrange(len(values)):
    ip.append(values[i][2])
    bytes.append(values[i][8])

####第二步：统计ip流量，存储到一个字典       
results={}
ip_set=set(ip)
for ipset in ip_set:
    count=0
    while(ipset in ip):
        siteip=ip.index(ipset)
        bytee=bytes[siteip]
        if bytee=='-':
            count+=0
        else :
            count+=float(bytee)
        ip.pop(siteip)
        bytes.pop(siteip)
    results[ipset]=count

###第三步：对字典排序，取top             
def getValues(d,topnum=10):

	result=sorted(d.iteritems(), key=lambda x:x[1],reverse=True)
	finalResult=result[:topnum]
	return finalResult

def figShow(value_all,top):
   	labels=[]
	quants=[]
	for i in range(top):
		labels.append(value_all[i][1])
		quants.append(value_all[i][0])
	plt.figure(1, figsize=(6,6))
	plt.title('源IP流量统计', bbox={'facecolor':'0.8', 'pad':5})
	colors  = ["pink","coral","yellow","orange"]
	plt.axis('equal')
	plt.pie(quants, colors=colors, labels=labels,autopct='%1.1f%%',pctdistance=0.8, shadow=True);
	plt.show()
				




"""	labels=[]
	quants=[]
	for labels in fieldvalue(key):
		labels.append(key)
	for quants in fieldvalue(value)
		quants.append(value)
		
	plt.figure(1, figsize=(6,6))
	colors  = ["pink","coral","yellow","orange"]

	plt.pie(quants, colors=colors, labels=labels,autopct='%1.1f%%',pctdistance=0.8, shadow=True)
	plt.title('源IP流量统计', bbox={'facecolor':'0.8', 'pad':5})

	plt.show()
	figShow(getValues(results,10),10)
"""




