from bs4 import BeautifulSoup, SoupStrainer
import requests
import httplib2
import os
from os.path import exists
import csv
import copy
import textProccessing
from mainConfig import *



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

def filter_links():
    for website_name in website_list.keys():
        path = result_path + '/'+website_name + '/' + website_name + '_Links.txt'
        file = open(path, 'r+' , encoding='utf-8' )
        s = ''
        text = file.readlines()
        for line in text:
            line = line.strip()
            if line.lower().endswith(forbidden_ends):
                continue
            s += line + '\n'
        open( path , 'w+', encoding= 'utf-8').write(s)


def num_link():
    num_link = dict.fromkeys(website_list.keys(), 0)
    for website_name in website_list.keys():
        path = result_path + '/'+website_name + '/' + website_name + '_Links.txt'
        file = open(path, 'r+' , encoding='utf-8' )
        text = file.readlines()
        num_link[website_name] = len(text)
    return num_link

def save(dict):
    with open('result.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(dict.keys())
        writer.writerow(dict.values())
def load():
    with open('result.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        return dict(zip(next(reader), next(reader)))


print (int (load()['bbc']))