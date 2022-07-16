import os
from os.path import exists
import csv
from mainConfig import *
import spacy 
import openpyxl
import matplotlib.pyplot as plt
import time
from scipy.stats import sem
import numpy as np
import json
from spacy.tokens import Doc

def save(File_name, dict):
    with open(File_name , 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(dict.keys())
        writer.writerow(dict.values())

def load(File_name):
    if not exists(File_name ):
        save(File_name, dict())
        return dict()

    with open(File_name , 'r') as csvfile:
        reader = csv.reader(csvfile)
        return dict(zip(next(reader), next(reader)))

def docSave(docs, file):
    with open(file, 'w', newline='', errors = 'replace') as jsonFile:
        json.dump([doc.to_json() for doc in docs], jsonFile)

def docLoad(file):
    with open(file, 'r', newline='', errors = 'replace') as jsonFile:
        docs_json = json.load(jsonFile)
        return [ sent for doc_json in docs_json for sent in Doc(nlp.vocab).from_json(doc_json).sents]




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

def num_Articles():
    categories_Dict = dict.fromkeys(categories, 0)
    for category in categories:
        for webste_name in website_list.keys():
            path = result_path + '/'+webste_name + '/texts/' + category + '/'
            if not exists(path):
                continue
            categories_Dict[category] += len(os.listdir(path))
    return categories_Dict


def combine_categ(categ):
    txts = [open(result_path + '/'+ webSite + '/texts/' + categ + '/' + filename, 'r+', encoding='utf-8', errors='replace').read().strip().lower() for webSite in website_list.keys() for filename in os.listdir(result_path + '/' + webSite + '/texts/' + categ + '/') if filename.endswith(".txt")]
    return txts


def graph(word, occurrences):
    x= plt
    error = sem(list(occurrences.values()))
    standard_deviation = '{:.2f}'.format(np.std(list(occurrences.values())))
    #The error is Standard Error of Mean
    x.bar(range(len(occurrences)), list(occurrences.values()), yerr = error, tick_label=list(occurrences.keys()), alpha = 0.75,capsize = 3)
    x.Axes.set_xmargin(plt.gca(), 0.02)
    x.title(word)
    x.xlabel('categories')
    x.ylabel('occurrences per 100 word')
    x.figtext(0, 0,'Standard deviation: '+str(standard_deviation))
    # plt.savefig(result_path+ '/word_statistics/'  + word + '.eps', format='eps')
    return x


def get_data(location):

    abbreviations = {}
    workbook = openpyxl.load_workbook(location)
    sheet = workbook.active

    for i in range(2,sheet.max_row):
        abbreviations[sheet.cell(i,1).value.strip().lower()] = sheet.cell(i,2).value.strip().lower()
    
    return abbreviations
log = open( './log.txt', 'w+', encoding='utf-8')

def write(x):
    print(x)
    log.write(x + '\n')



def analyse_txts(txts):
    piped = [pipe for pipe in nlp.pipe(txts,n_process = number_threads, batch_size= 20)]
    return [sent for pipe in piped for sent in pipe.sents]

def get_word_statistics():
    print ('start1')
    t = time.time()
    start = time.time()
    abbrv = get_data(abbreviation_location)
    
    for category in categories:
        t = time.time() ###
        txts = combine_categ(category)
        docs = analyse_txts(txts)
        txt = '\n'.join(txts)
        txtLength = len(txt.split())
        
        write( category + ' analys done in: ' + str(time.time() - t)) ###
        t = time.time() ###
        for rule in rules_results.keys():
            if rule == 'Abbreviation':
                rule_occ = rules_fun[rule] (txt, abbrv) 
            else:
                rule_occ = sum( rules_fun[rule] (doc) for doc in docs)

            rules_results[rule][category] = 100 * rule_occ / txtLength

            write( category + '\t' + str(rules_abbrv[rule]) + '\t' + str(time.time() - t) + '\tocc: ' + str(rules_results[rule][category]) + '\n') ###
        
    #print(rules_results)
    return rules_results

