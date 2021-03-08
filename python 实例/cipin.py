#coding=utf-8  


import os
import sys
import jieba
import time

reload(sys)  
sys.setdefaultencoding("utf-8") 


path = r'G:\\yuanyang\\common.txt'
read_txt = open(path, 'r')
ShuiBa_word_list = []  # 汇总水吧的所有词语的列表（有顺序，重复）
ShuiBa_word_set = set() # 得到水吧所有词语的集合（无顺序，不重复）
for line in read_txt.readlines():
    line = line.replace(' ', '')
    line = line.strip('\n')
    word_list = jieba.lcut(line, cut_all=False)  #cut_all=false精准模式
    word_set = set(word_list)

    ShuiBa_word_list = ShuiBa_word_list + word_list 
    ShuiBa_word_set = ShuiBa_word_set.union(word_set)
	
ast=[]
for word in ShuiBa_word_set:
	fre = ShuiBa_word_list.count(word)
	lu=(float(fre)/len(ShuiBa_word_list))*100
	lu1=str(lu)+'%'
	ast.append((word,fre,lu1))
	# open("G:\\yuanyang\\results.txt",'w').write(word + '' + str(fre) + '\n')
	# print(word, str(fre))  #打印词语及其频率
ast.sort(lambda x,y:cmp(x[1],y[1]),reverse=True)

for a in ast:
    f = open("G:\\yuanyang\\results.txt",'a')
    f.write(str(a[0]) + '  ' + str(a[1]) + '  '+str(a[2])+'\n')
	
'''
with open("G:\\yuanyang\\common.txt") as wf,open("G:\\result.txt",'w') as wf2:  

for word in wf:  
	
	for item in word_lst:  
		 for item2 in item:  
			if item2 not in word_dict:
				word_dict[item2] = 1  
			else:  
				word_dict[item2] += 1  
for key in word_dict:  
	print key,word_dict[key]  
	wf2.write(key+' '+str(word_dict[key])+'\n')
'''