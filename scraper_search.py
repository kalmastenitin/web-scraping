import requests
import os
import time
from bs4 import BeautifulSoup
import csv
from abc import *

url = []
USER_AGENT = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

class web_scraping(ABC):

    @abstractmethod
    def scrape(self):
        pass

class GoogleScraper(web_scraping):
    def scrape(self,search_Term):
        self.filename = search_Term
        self.url = 'https://google.com/search?q='+search_Term+'&gws_rd=cr'
        r = requests.get(self.url,headers=USER_AGENT)
        soup = BeautifulSoup(r.content,'html5lib')
        # result_block = soup.find_all('div', attrs={'class':'g'})
        result_block = soup.find_all(class_ = 'g')
        for result in result_block:
            link = result.find('a',href=True)
            title = result.find('h3')
            description = result.find('span',attrs={'class':'st'})
            if link and title:
                link = link['href']
                title = title.get_text()
                if description:
                    description = description.get_text()
                    with open(self.filename+'.csv', 'a', encoding = 'utf-8', newline='') as csv_file:
                        file_is_empty = os.stat(self.filename+'.csv').st_size==0
                        fieldname = ['title','link','description']
                        # print(title, link, description)
                        writer = csv.DictWriter(csv_file,fieldnames=fieldname)
                        if file_is_empty:
                            writer.writeheader()
                        writer.writerow({'title':title,'link':link,'description':description})

class DuckduckgoScraper(web_scraping):
    def scrape(self,search_Term):
        self.filename = search_Term
        self.url = 'https://duckduckgo.com/html?q='+search_Term
        r = requests.get(self.url,headers=USER_AGENT)
        soup = BeautifulSoup(r.content,'html5lib')
        result_block = soup.find_all(class_ = 'result__body')
        for result in result_block:
            link = result.find('a', attrs={'class':'result__a'}, href=True)
            title = result.find('h2')
            description = result.find(attrs={'class':'result__snippet'})
            if link and title:
                link = link['href']
                title = title.get_text()
                if description:
                    description = description.get_text()
                    with open(self.filename+'.csv', 'a', encoding='utf-8',newline='') as csv_file:
                        file_is_empty = os.stat(self.filename+'.csv').st_size==0
                        fieldname = ['title','link','description']
                        writer = csv.DictWriter(csv_file,fieldnames=fieldname)
                        if file_is_empty:
                            writer.writeheader()
                        writer.writerow({'title':title,'link':link,'description':description})

class DuckduckgoScraper(web_scraping):
    def scrape(self,search_Term):
        self.filename = search_Term
        self.url = 'https://duckduckgo.com/html?q='+search_Term
        r = requests.get(self.url,headers=USER_AGENT)
        soup = BeautifulSoup(r.content,'html5lib')
        result_block = soup.find_all(class_ = 'result__body')
        for result in result_block:
            link = result.find('a', attrs={'class':'result__a'}, href=True)
            title = result.find('h2')
            description = result.find(attrs={'class':'result__snippet'})
            if link and title:
                link = link['href']
                title = title.get_text()
                if description:
                    description = description.get_text()
                    with open(self.filename+'.csv', 'a', encoding='utf-8',newline='') as csv_file:
                        file_is_empty = os.stat(self.filename+'.csv').st_size==0
                        fieldname = ['title','link','description']
                        writer = csv.DictWriter(csv_file,fieldnames=fieldname)
                        if file_is_empty:
                            writer.writeheader()
                        writer.writerow({'title':title,'link':link,'description':description})

class bing(web_scraping):
    def scrape(self,search_Term):
        self.filename = search_Term
        self.url = 'https://www.bing.com/search?q='+search_Term
        r = requests.get(self.url,headers=USER_AGENT)
        soup = BeautifulSoup(r.content,'html5lib')
        result_block = soup.find_all(class_ = 'b_algo')
        for result in result_block:
             link = result.find('a',href=True)
             title = result.find('h2')
             description = result.find(attrs={'class':'b_caption'})
             if link and title:
                 link = link['href']
                 title = title.get_text()
                 if description:
                     description = description.get_text()
                     print(link)
                     print(title)
                     print(description)
                     with open(self.filename+'.csv', 'a', encoding='utf-8',newline='') as csv_file:
                         file_is_empty = os.stat(self.filename+'.csv').st_size==0
                         fieldname = ['title','link','description']
                         writer = csv.DictWriter(csv_file,fieldnames=fieldname)
                         if file_is_empty:
                             writer.writeheader()
                         writer.writerow({'title':title,'link':link,'description':description})



if __name__=='__main__':
    # g = GoogleScraper()
    d = yandex()
    search_this = input('Enter Your Search Term: ')
    starttime = time.time()
    # g.scrape(search_this)
    d.scrape(search_this)
    print('That took {} seconds'.format(time.time() - starttime))
