from mainConfig import *
import spacy
from spacy import displacy
from nltk.tokenize import sent_tokenize
import os

# txt = ''
# path = result_path + '/The Wall Street Journal/texts/other/'

# for filename in os.listdir(path):
#     if filename.endswith(".txt"):
#         txt += open(path + filename, "r",  encoding='utf-8' ).read()

# num_word = len(txt.split())

# s = sent_tokenize(txt)

# nlp = spacy.load("en_core_web_lg")
# res = [nlp(text)for text in s]

# arr = [ [word.lemma_ ,child.lemma_] for doc in res for word in doc if word.pos_ == 'VERB' for child in word.children  if child.pos_ == 'ADP']
# print(f'it give: {100 * len(arr)/num_word:.2f} phrasal verbs per 100 words')

# saveDict = dict.fromkeys(website_list.keys(), 0)
# for website_name in website_list.keys():
#     path = result_path + '/'+website_name + '/' + website_name + '_Links.txt'
#     file = open(path, 'r+' , encoding='utf-8' )
#     text = file.readlines()
#     saveDict[website_name] = len(text)
# print(saveDict)
