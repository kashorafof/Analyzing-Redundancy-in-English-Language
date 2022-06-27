from bs4 import BeautifulSoup, SoupStrainer
import requests
import httplib2
import os
from os.path import exists
import csv
import copy
import textProccessing
from mainConfig import *

def scrapLinks(link):

    headers = requests.utils.default_headers()
    headers.update(
        {
            'Content-Type': 'application/json',
            'User-Agent': 'My User Agent 1.0',
        }
    )

    url_extract = requests.get(link, headers= headers).text
    s = ""
    if link == "https://nypost.com/":
        link = link + "20"
    soup = BeautifulSoup(url_extract, )
    texts = soup.find_all('a')
    for L in texts:
        s+= str(L)
    s = set(s.split('"'))
    return s




def get_statistics(text, acc):
    
    for word in words:
        if not (word in acc.keys()):
            acc[word] = 0
        acc[word] = acc[word] + text.count(word)
    return acc



def num_links():
    i = 0
    for website_name in website_list.keys():
            path = result_path + '/' +website_name+'/'+website_name+"_Links.txt"
            if not exists(path):
                print(website_list,0)
                continue
            inFile = open(path, "r")
            links = inFile.readlines()
            print(website_name, len(links))
            i = i+len(links)
    print(i)


num_links()
