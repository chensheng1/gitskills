#!usr/bin/env python
#coding:cp936

k=5   #����Ӳ�ҵı�ֵ
n=100   #��֧����Ǯ
mon=[]   #��ʼ���ı�ֵ����

backmon=[]     #��Ѱ�ı�ֵ��Ŀ�ʹ�С������ʼ��
for i in range(k+1):  #������Ŀ�еı�ֵ�б�
    mon.append(2**i)
mon.reverse()
for m in mon:             #ѡ�����ı�ֵ������nȥ���������õ���ֵ�Ǵ˱�ֵ����Ŀ��������ʣ�µ�Ҫ�����жϵġ�
    backmon.append(n/m)
    n=n%m
for j in range(k+1):
    if backmon[j]!=0:     #�жϴ�ӡ
        print str(mon[j])+'��Ҫ'+str(backmon[j])+'��'


