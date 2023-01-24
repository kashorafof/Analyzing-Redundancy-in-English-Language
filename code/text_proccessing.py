
from requests import post
import spacy
from spacy import displacy


# Script contains all the functions that will be used in the analysis of the text


# calculate the number of CC in the text
def CoordinaryConjunction(doc):
    count = 0

    for itrWord in doc:
        # check if the word is consider as a cc "and , or , but .. etc"
        if itrWord.dep_ == 'cc':
            # count the word
            count += 1
            # go to the head of the word
            father = itrWord.head
            # got for the other words that have a conj relation with the word
            while father.dep_ == 'conj':
                count += 1
                father = father.head

    return count


def count_Phrasal_verb(doc):
    # count all the word with pos = verb and check if it has a child with pos = adp
    return len([ 1 for word in doc if word.pos_ == 'VERB' for child in word.children  if child.pos_ == 'ADP'])


#count the number of subordinate conjunctions in the text "if, because, otrherwise and since"
def count_Subordinating_conjunctions(doc):
    count = 0
    for word in doc:
        #if the word pos is SCONJ "subordinating conjunction"
        if word.pos_ == 'SCONJ':
            # count the word
            count += 1

   
            count += 1
    return count


# one bit for the location of the conjunction
    # becuase of .. i did .. -> 0
    # i did .. because of .. -> 1

# 2 bits for the synonym of the conjunction 
    # because -> 00
    # for -> 01
    # since -> 10
    # in order -> 11


#calculate the number of abbreviations from spacy (not working)
def count_Abbreviation(txt, abbrv):

    # street -> st.
    # doctor -> dr.
    counter = 0
    # count the number of abbreviations in the text either the full word or the short form
    for i in abbrv:
    
        counter = counter + txt.count(" " + i) + txt.count(" "+abbrv[i])
    return counter


def count_Pre_Proper_Noun(doc):
    nnp = False
    prp = False

    for word in doc:
        # check if we found a proper noun
        if word.tag_ == 'NNP':
            nnp = True
        # check if we found a pronoun
        elif word.tag_ == 'PRP':
            prp = True
        # if the sentence contain both proper noun and pronoun return 1
        if nnp and prp: 
            return 1

    return 0


    