#-*- coding: utf-8 -*-
"""一个整数加上100是完全平方数，再加上168也是完全平方数"""
import math
num=1
while True:
	if math.sqrt(num+100)-int(math.sqrt(num+100))==0 and math.sqrt(num+268)-int(math.sqrt(num+268))==0:
		print(num)
		break
	num+=1