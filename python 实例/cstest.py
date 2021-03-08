#!usr/bin/env python
#coding:cp936

k=5   #设置硬币的币值
n=100   #所支付的钱
mon=[]   #初始化的币值数组

backmon=[]     #找寻的币值数目和大小，并初始化
for i in range(k+1):  #生成题目中的币值列表
    mon.append(2**i)
mon.reverse()
for m in mon:             #选择最大的币值，并用n去除以它，得到的值是此币值的数目，余数是剩下的要继续判断的。
    backmon.append(n/m)
    n=n%m
for j in range(k+1):
    if backmon[j]!=0:     #判断打印
        print str(mon[j])+'需要'+str(backmon[j])+'个'


