import urllib2, cookielib

url = 'http://www.baidu.com'


re1=urllib2.urlopen(url)
print re1.getcode()
print len(re1.read())


request = urllib2.Request(url)
request.add_header('User-Agent', 'Mozilla/5.0')
re2=urllib2.urlopen(url)
print re2.getcode()
print len(re2.read())


cj=cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
re3=urllib2.urlopen(url)
print re3.getcode()
print cj
print len(re3.read())