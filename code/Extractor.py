from bs4 import BeautifulSoup, SoupStrainer
import requests
import httplib2
import os
from os.path import exists
import time
import final_res as FS
from mainConfig import *
import functions as Fun
import json

# main driver to extract Links
def extractLinks():
    # for each website
    for website_name, link in website_list.items():
        path = result_path + '/scrapped/'+website_name
        
        # in case no previous scraping -> create the folders
        if not os.path.exists(path):
            os.makedirs(path)
        if not os.path.exists(path + '/texts'):
            os.makedirs(path+ '/texts')


        # in case no previous scraping -> create the file to save the scrapped links
        if not os.path.exists(path+"/"+website_name+"_Links.txt"):
            outFile = open(path+"/"+website_name+"_Links.txt", "w+")
            newList = ''
        # if there is previous scraping -> load the previous links
        else :
            outFile = open(path+"/"+website_name+"_Links.txt", "r+")
            newList = outFile.read()

        # scrap the articles links from the website root link
        s = scrapLinks(link)
        
        # the links in a set to avoid duplicates
        newList = set(newList.split('\n'))
        newList.remove('')
        
        # filterring the links
        for x in s:
            newLink = ''
            # if the link is not a picture or a video .. etc -> skip
            if x.lower().endswith(forbidden_ends):
                continue
            # filter special case for each website
            if website_name == 'The New York Daily News' and not x.endswith('html'):
                continue
            if website_name == 'bbc' and  x.startswith('/') and '-' in x :
                newLink = link + x[1:] 
            if x.startswith('/news') and '-' in x  :
                newLink = link + x[1:] 
            if website_name == 'New York Post' and not x.startswith('https://nypost.com/2022'):
                continue
            # if the links is related to the website 
            # and it contains a dash (to avoid links to the website home page)
            # and it is not too short (to avoid links to main pages)
            if x.startswith(link) and '-' in x and len(x) >60:
                newLink = x 
            # if the link is new link -> add it to the list
            if newLink != '' and not newLink in newList :
                newList.add(newLink)

        # save the links to the file
        outFile = open(path+"/"+website_name+"_Links.txt", "w+")
        for x in newList:
            outFile.write(x + "\n")
        outFile.close()




def scrapLinks(link):
    # Request the website
    headers = requests.utils.default_headers()
    headers.update(
        {
            'User-Agent': 'My User Agent 1.0',
        }
    )
    url_extract = requests.get(link, headers= headers).text
    soup = BeautifulSoup(url_extract, )

    # get all the links in the website
    texts = soup.find_all('a')

    # combine all the links in a string
    s = ""
    for L in texts:
        s+= str(L)
    s = set(s.split('"'))

    return s


def scrapArticles():
    # check if there is a previous save point and load it
    save_point_dict = Fun.load(links_save_point_location)

    # for each website
    for website_name in website_list.keys():
        # get the website save point
        save_point = int(save_point_dict[website_name])
        #website_time = time.time()
        # get all the links
        inFile = open(result_path + '/' +website_name+'/'+website_name+"_Links.txt", "r")
        links = inFile.readlines()

        # if all the links are scrapped -> skip
        if len(links) <= save_point:
            continue

        i = 0
        for n in links:
            n = n.strip()
            # skip the links up to the save point
            i += 1
            if i < save_point:
                continue

            # scrap the text from the link and get the genre
            text,genre = scrapText(n.strip())
            # 'discard' is a genre to indicate that the text length is less than the min in the mainConfig
            if(genre == 'discard'):
                continue

            # create the folder for the genre if it does not exist
            path = result_path + '/' + website_name + '/texts/' + genre
            if not os.path.exists(path):
                os.makedirs(path)
            
            # creating a file and name it
            num_files = len(os.listdir(path)) 
            outFile = open(path + '/'+ str(num_files)  +".txt", "w+" , encoding='utf-8' )
            outFile.write(text)
            outFile.close()

        # save the save point
        save_point_dict[website_name] = len(links)
        Fun.save(links_save_point_location, save_point_dict)
        

def scrapText(link):

    # Request the website
    headers = requests.utils.default_headers()
    headers.update(
        {
            'Content-Type': 'application/json',
            'User-Agent': 'My User Agent 1.0',
        }
    )
    url_extract = requests.get(link, headers=headers).text
    soup = BeautifulSoup(url_extract,"html.parser" )

    # take only the paragraphs
    texts = soup.find_all('p')

    s = ""
    
    # combine all the paragraphs in a string
    for text in texts:
        s = s + text.text + "\n"
    # if the text is too short -> discard it
    if len(s) < min_article_length:
        return s, 'discard'
    
    # get the genre of the text and its percentage using the AI model in final_res.py
    genre , chance = FS.predict_from_text(s)
    # if the chance is less than the min -> set the genre to 'other'
    if chance < minGenrePercent:
        genre = "other"
    return s, genre


# flatten a nested list of lists into a single list
def flatten(list_of_lists):
    return [item for sublist in list_of_lists for item in sublist]

def jsonScrapFrom(path):
    return [json.load(open(path + file , encoding= 'UTF-8', errors='replace')) for file in os.listdir(path) if file.endswith('.json')]

def jsonScrap(categ):
    path = data_set_path 
    if categ == categories[-1]:
        folders = ['travel/', 'world/']
        
        txt = [jsonScrapFrom(path + folder) for folder in folders]
        return flatten(txt)
    path += categ + '/'
    return jsonScrapFrom(path)
