# from mainConfig import *
# import spacy
# from spacy import displacy
# from nltk.tokenize import sent_tokenize
# import os

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
from time import time
import spacy
from spacy import displacy
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
#nlp = spacy.load("en_core_web_lg")

#txt = 'I had played football, tennis and basketball'



#calculate the number of abbreviations from spacy (not working)
def count_abbreviation(txt):
    nlp = spacy.load("en_core_web_lg")
    doc = nlp(txt)
    count = 0
    for token in doc:
        if token.like_num:
            count += 1
    return count
#calculate the number of subordinates from spacy (not working)
def count_subordinate(txt):
    nlp = spacy.load("en_core_web_lg")
    doc = nlp(txt)
    count = 0
    for token in doc:
        if token.dep_ == 'subj':
            count += 1
    return count



#txt = 'do you know where is st mohammed bin zayed '

#txt = 'I will stay in the university or i want to go home.'
#doc = nlp(txt)
#displacy.render(doc, page="false", jupyter=True)
#print(count_abbreviation(txt))
# x = 'bloating, fatigue, bone or joint pain, unintended weight loss, itchy skin rash and abdominal pain, diarrhea and constipation.'
# count = 0
# posTag = nltk.pos_tag(word_tokenize(x))
# nlp = spacy.load("en_core_web_lg")
# doc = nlp(x)
# print(doc[0].text)

# for word in posTag:
#     if word[1] == 'CC':
#         for token in doc:
#             if token.dep_ == 'conj':
#                 print(token.lemma_)
#                 count += 1
# print(count)
import time

print(time.localtime())