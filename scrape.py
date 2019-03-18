#!/usr/bin/python3

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import os

#initiate 1337 scraper
web_req = Request('https://www.1337x.one/top-100-eng-movies', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(web_req).read()
soup = BeautifulSoup(webpage, 'html.parser')

#define capture list
link_list = []

#searches elemts and fills capture list with relative movie links
for td in soup.find_all('td', class_="coll-1 name"):
    for links in td.find_all('a'):
        if not (links.has_attr('class')):
            link_list.append(links['href'])

#define final torrent links
url_prefix = 'https://www.1337x.one'
#loop the captured list 
for link in link_list:
    #initiate temp request/soup variables
    web_req = Request(url_prefix + link, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(web_req).read()
    soup = BeautifulSoup(webpage, 'html.parser')
    #loop returned website elements
    for a_tag in soup.find_all('a', class_='beceafae btn btn-cbebadce'):
        #print(a_tag['href'])
        os.system("transmission-remote -a "+a_tag['href'])
        os.system("echo 'downloading started for: '"+a_tag['href'])
        os.system("echo '---------------------------------------' ")
        

