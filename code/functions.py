import os
from os.path import exists
import csv
from mainConfig import *
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import spacy 
import openpyxl
import matplotlib.pyplot as plt
import time
from scipy.stats import sem
import numpy as np
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

    combinePath = result_path + '/combined/' 
    if not exists(combinePath):
        os.makedirs(combinePath)
    combinePath += categ + '.txt'
    OutFile = open(combinePath, 'w+', encoding='utf-8')

    for website_name in website_list.keys():
        path = result_path + '/'+website_name + '/texts/' + categ + '/'
        if not exists(path):
            continue
        for filename in os.listdir(path):
            if filename.endswith(".txt"):
                Text = open(path + filename, "r" , encoding='utf-8', errors='replace').readlines()

                #t = '-'.join([txt.strip() for txt in Text if len(txt.split()) > 4])
                #s += str('-'.join([txt.strip() for txt in Text if len(txt.split()) > 4]))
                txt = str(''.join([txt.strip() + '\n' for txt in Text if len(txt.split()) > 4]))
                OutFile.write(txt + '\n')


def combine_all():
    for categ in categories:
        combine_categ(categ)


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



def get_word_statistics():
    t = time.time()
    start = time.time()
    abbrv = get_data(abbreviation_location)
    nlp = spacy.load("en_core_web_lg")
    
    write('loading time: ' + str(time.time() - t))
    t = time.time() ##

    for category in categories:
        log.write('\n' + category + '\n')

        path = result_path + '/combined/' + category + '.txt'

        txt = open(path, 'r', encoding='utf-8').read().strip()
        sentences = sent_tokenize(txt)

        tokenized = [word_tokenize(sentence) for sentence in sentences]
        posTags = [nltk.pos_tag(token) for token in tokenized]

        docs = [nlp(sentence) for sentence in sentences]
        txtLength = len(txt.split())
        write( category + ' with text length ' + str(txtLength/1000) + 'k words took: ' + str(time.time() - t) + ' to process ')

        t = time.time() ###

        for rule in rules_results.keys():
            if rule == 'Abbreviation':
                rule_occ = rules_fun[rule] (txt.lower(), abbrv)
            else:
                rule_occ = sum( rules_fun[rule] (doc, posTag)  for (doc,posTag) in zip(docs,posTags))

            rules_results[rule][category] = 100 * rule_occ / txtLength

            write( category + '\t' + rules_abbrv[rule] + '\t' + str(time.time() - t)) ###
            t = time.time() ###
        write ('\n')

    write('\n\nTotal time: ' + str(time.time() - start))

    for rule in rules_results.keys():

        save(result_path + '/word_statistics/' + rule + '.csv', rules_results[rule])
        graph(rule, rules_results[rule])
        plt.savefig(result_path+ '/word_statistics/'  + rule + '.eps', format='eps')
        plt.savefig(result_path+ '/word_statistics/'  + rule + '.png', format='png')
        plt.close()

get_word_statistics()