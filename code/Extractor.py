from bs4 import BeautifulSoup, SoupStrainer
import matplotlib.pyplot as plt
import numpy as np
import requests
import httplib2
import os
from os.path import exists
import csv
import copy
import import_ipynb
import nltk
import functions as Fun
import time
import final_res as FS
from scipy.stats import sem
from mainConfig import *


def extractLinks():
    for website_name, link in website_list.items():

        
        path = result_path + '/'+website_name
        if not os.path.exists(path):
            os.makedirs(path)
        if not os.path.exists(path + '/texts'):
            os.makedirs(path+ '/texts')
        
        if not os.path.exists(path+"/"+website_name+"_Links.txt"):
            outFile = open(path+"/"+website_name+"_Links.txt", "w+")
            newList = ''
        else :
            outFile = open(path+"/"+website_name+"_Links.txt", "r+")
            newList = outFile.read()

        s = Fun.scrapLinks(link)

        
        

        
        newList = set(newList.split('\n'))
        newList.remove('')
        
        for x in s:
            newLink = ''
            if x.startswith('/news/2022') and '-' in x and not (".svg" in x or ".png" in x )  :
                newLink = link + x[1:] 
            if (x.startswith(link) and '-' in x and len(x) >60 and not (".svg" in x or ".png" in x)) or x.startswith('https://nypost.com/2022/') :
                newLink = x 
            
            if newLink != '' and not newLink in newList :
                newList.add(newLink)
            
        outFile = open(path+"/"+website_name+"_Links.txt", "w+")
        for x in newList:
            outFile.write(x + "\n")
        websites_num_links[website_name] = len(newList)
        outFile.close()

def scrapLinks(link):

    headers = requests.utils.default_headers()
    headers.update(
        {
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



def scrapArticles():
    for website_name in website_list.keys():

        inFile = open(result_path + '/' +website_name+'/'+website_name+"_Links.txt", "r")
        links = inFile.readlines()
        i = 0
        website_time = time.time()
        for n in links:
            n = n.strip()
            print(website_name, i)
            text,genre = scrapText(n.strip())
            if(genre == 'discard'):
                continue
            path = result_path + '/' + website_name + '/texts/' + genre
            if not os.path.exists(path):
                os.makedirs(path)
            
            num_files = len(os.listdir(path)) 

            outFile = open(path + '/'+ str(num_files)  +".txt", "w+" , encoding='utf-8' )

            outFile.write(text)
            outFile.close()
            i = i+1
        print(time.time() - website_time)
        




def scrapText(link):

    start = time.time()
    headers = requests.utils.default_headers()

    headers.update(
        {
            'Content-Type': 'application/json',
            'User-Agent': 'My User Agent 1.0',
        }
    )

    url_extract = requests.get(link, headers=headers).text
    soup = BeautifulSoup(url_extract,"html.parser" )
    texts = soup.find_all('p')
    s = ""
    Length = len(texts)
    before_merge = time.time()
    for text in texts:
        s = s + text.text + "\n"
    if len(s) < min_article_length:
        return s, 'discard'
    before_categories = time.time()
    genre , chance = FS.predict_from_text(s)
    if chance < minGenrePercent:
        genre = "other"
    print(before_merge-start, time.time()-before_categories, 'Total: ' + str(time.time()-start), genre ,chance)
    return s, genre


#new york daily new stopped at 435
#scrapArticles()