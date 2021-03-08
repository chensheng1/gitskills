# encoding:utf-8
class UrlManager(object):
    def __init__(self):
        self.newurls = set()
        self.oldurls = set()
    
    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.newurls or url not in self.oldurls:
            self.newurls.add(url)
            

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)
    
    def has_new_url(self):
        return len(self.newurls) != 0

    
    def get_new_url(self):
        newurl = self.newurls.pop()
        self.oldurls.add(newurl)
        return newurl