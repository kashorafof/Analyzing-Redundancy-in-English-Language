from bs4 import BeautifulSoup, SoupStrainer
import matplotlib.pyplot as plt
import numpy as np
import requests
import httplib2
import os
from os.path import exists
import csv
import nltk
import time
from scipy.stats import sem
import copy
import text_proccessing

minGenrePercent = 60
min_article_length = 100

result_path = "../result"


categories = ["tech", "sport", "business", "politics", "entertainment", "other"]
rules = ["Coordinary Conjunction", "Phrasel Verb"] # to do
forbidden_ends = (".svg", ".png", ".jpg", ".jpeg", ".gif")
rules_results = {
    "Coordinary Conjunction": dict.fromkeys(categories, 0),
    "Phrasel Verb": dict.fromkeys(categories, 0),
}

rules_fun = {
    'Coordinary Conjunction': text_proccessing.CoordinaryConjunction,
    'Phrasel Verb': text_proccessing.count_Phrasel_Verb,
}



website_list = {
    'New York Post' : 'https://nypost.com/',
    'The Wall Street Journal' : 'https://www.wsj.com/',
    'The New York Times' : 'https://www.nytimes.com/',
    'The Washington Times' : 'https://www.washingtontimes.com/',
    'The New York Daily News' : 'https://www.nydailynews.com/',
    'The Guardian' : 'https://www.theguardian.com/',
    'bbc' : 'https://www.bbc.com/',
}



leftLinks = set([])
