from turtle import pos
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from requests import post
import spacy
from spacy import displacy




# tokenized = word_tokenize(txt)
# nlp = spacy.load("en_core_web_lg")
# doc = nlp(txt)
# posTag = nltk.pos_tag(tokenized)



# if their is a CC word "and, or "
#   calculate the number of conjunction in the sentence 
def CoordinaryConjunction(doc, posTag):
    count = 0
    for word in posTag:
        if word[1] == 'CC':
            for token in doc:
                if token.dep_ == 'conj':
                    count += 1
    return count


def count_Phrasel_Verb(doc, posTag):
    arr = [ [word.lemma_ ,child.lemma_] for word in doc if word.pos_ == 'VERB' for child in word.children  if child.pos_ == 'ADP']
    return len(arr)


#count the number of subordinate conjunctions in the text "if, because, otrherwise and since"
def count_Subordinating_conjunctions(doc, posTag):
    count = 0
    for i in range(len(posTag)):
        if posTag[i][1] == 'IN':
            if(posTag[i][0] == 'in' and posTag[i+1][0] != 'order'): continue
            
            count += 1
            # one bit for the location of the conjunction
                # becuase of .. i did .. -> 0
                # i did .. because of .. -> 1
        
            # 2 bits for the synonym of the conjunction 
                # because -> 00
                # for -> 01
                # since -> 10
                # in order -> 11
    return count

#check if the subordinate clause in the first clause of te sentence


#calculate the number of abbreviations from spacy (not working)
def count_Abbreviation(txt, abbrv):

    # street -> st.
    # doctor -> dr.
    counter = 0
    for i in abbrv:
        counter = counter + txt.count(" " + i) + txt.count(" "+abbrv[i])
    return counter


#check if pronoun in first clause and return either true or false nlp
def count_Pre_Proper_Noun(doc, posTag):
    nnp = False
    prp = False
    for tag in posTag:
        if tag[1] == 'NNP':
            nnp = True
        if tag[1] == 'PRP':
            prp = True
    if nnp and prp: 
        return 1
    return 0


    