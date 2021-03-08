#-*- coding: utf-8 -*-

from pylab import *

mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

"""统计源ip流量"""


import sys
import matplotlib.pyplot as plt
import numpy as np

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

###第三步：对字典排序，取top             
def getValues(d,topnum=10):

	result=sorted(d.iteritems(), key=lambda x:x[1],reverse=True)
	finalResult=result[:topnum]
	return finalResult


####第四步：作图show2                     
def fig(value_all,top):
    height=[]
    values=[]
    for i in range(top):
        height.append(value_all[i][1])
        values.append(value_all[i][0])
	
    plt.subplot(211)
    plt.xlabel(u"IP")
    plt.ylabel(u"bytes")
    plt.title(u"IP流量统计")
    xVal=arange(len(values))
    xticks(xVal+0.2/2.0,values,rotation=80)
    
    bar_test=plt.bar(np.arange(top),height, width=0.5,color='r')
    plt.show()
	
	




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



###测试###
fig(getValues(results,10),10)