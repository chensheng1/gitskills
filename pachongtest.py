#coding=utf-8
import re
import urllib

def getHtml(url):
	page=urllib.urlopen(url)
	html=page.read()
	return html

def getImg(html):
	reg = r'src="(.+?\.jpg)" pic_ext' 
	imgre=re.compile(reg)
	imglist=re.findall(imgre,html)
	x=0
	for imgurl in imglist:
		urllib.urlretrieve(imgurl,'D:/test/%s.jpg'%x)
		x+=1

if __name__ == '__main__':     
    html = getHtml("http://tieba.baidu.com/p/2460150866")  
    getImg(html)  		
