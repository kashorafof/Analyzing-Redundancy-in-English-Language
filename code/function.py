from bs4 import BeautifulSoup, SoupStrainer
import requests
import httplib2
import os
from os.path import exists
import csv
import copy
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import textProccessing

def scrapText(link):

    
    headers = requests.utils.default_headers()

    headers.update(
        {
            'User-Agent': 'My User Agent 1.0',
        }
    )

    url_extract = requests.get(link, headers=headers).text
    soup = BeautifulSoup(url_extract,"html.parser" )
    texts = soup.find_all('p')
    s = ""
    Length = len(texts)
    for text in texts:
        s = s + text.text + " "
    return s


def get_statistics(text, acc):
    
    for word in words:
        if not (word in acc.keys()):
            acc[word] = 0
        acc[word] = acc[word] + text.count(word)
    return acc

