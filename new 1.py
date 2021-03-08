#-*- coding: utf-8 -*-
"""统计1,2,3,4个数字可以统计多少个不重复数字的三位数并打印"""
count=0
for i in range(1,5):
	for j in range(1,5):
		for k in range(1,5):
			if i!=j and j!=k and i!=k:
				count+=1
				print i*100+j*10+k
print count