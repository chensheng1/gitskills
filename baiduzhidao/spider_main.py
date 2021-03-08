# encoding:utf-8
import url_manager, html_downloader, outputer, html_parser
import time

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = outputer.HtmlOutputer()
        
    
    def craw(self, root_url):
        print '123go:'
        self.urls.add_new_url(root_url)
        count = 1
        while self.urls.has_new_url():
            new_url = self.urls.get_new_url()
            print 'craw %d:%s' % (count, new_url)
            html_cont = self.downloader.download(new_url)
            new_urls, new_data = self.parser.parse(new_url, html_cont)
            self.urls.add_new_urls(new_urls)
            self.outputer.collect_data(new_data)
            time.sleep(0.1)
            if count == 10:
                break
            count += 1

        self.outputer.output_html()
            
    
    

if __name__ == '__main__':
    root_url = 'http://baike.baidu.com/view/2857537.htm'
    obj_spider = SpiderMain()
    craw = obj_spider.craw(root_url)