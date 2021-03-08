#-*- coding: utf-8 -*-

import re


def getAllFieldValue(filename):
    fieldvalue=[]
    fr=open(filename)
    for line in fr.readlines():
		line=line.strip()
		listFromLine=line.split('\t')
		fieldvalue.append(listFromLine)
    return fieldvalue

toles=[]
results={}
keys=[]
values=[]
values=getAllFieldValue('F:\\data\\2016-06-20\\conn-summary.16_34_20-17_00_00.log')
val=values[4:14]
for i in range(len(val)):
	sum=''.join(val[i])
	tole=sum.split('|',2)
	toles.append(tole)
y=[x[1] for x in toles]
for x in y:
	data=x.split()
	ips=data[0]
	pro=data[1]
	i=ips[:-2]
	ip=i.strip('#')
	keys=ip.split('\t')
	values=pro.split('\t')
	results=dict(zip(keys,values))
	print results




#判断当天0点到现在的整点情况
'''
def txt_wrap_by(self,start_str, end, html):
	start = html.find(start_str)
	if start >= 0:
		start += len(start_str)
		end = html.find(end, start)
		if end >= 0:
			return html[start:end].strip()
for i in f:
	if dt.strftime(dt.now(),'%Y-%m-%d') in i:
		if((dt.now()-(dt.now%86400)+time.timezone)<dt.now()):
		print i
'''