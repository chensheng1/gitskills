# encoding:utf-8
from bs4 import BeautifulSoup
import re
import urlparse
class HtmlParser(object):
    
    
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        # $在正则中指明必须以前面什么结尾。
        links = soup.find_all('a',href=re.compile(r'/view/\d+\.htm$'))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
            
        return new_urls
    
    
    def _get_new_data(self, page_url, soup):
        res_data = {}
        
        # url
        res_data['url'] = page_url
        
        #<dd class="lemmaWgt-lemmaTitle-title"> <h1>title</h1>
        title_note = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title'] = title_note.get_text()
        
        #<div class="lemma-summary" label-module="lemmaSummary">
        summary_note = soup.find('div', class_='lemma-summary')
        if summary_note is None:
            # <div class="lemmaWgt-subLemmaListTitle">
            summary_note = soup.find('div', class_='lemmaWgt-subLemmaListTitle')
        res_data['summary'] = summary_note.get_text()
        
        return res_data
    
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data