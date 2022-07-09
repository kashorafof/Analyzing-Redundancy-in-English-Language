import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import spacy
from spacy import displacy




# tokenized = word_tokenize(txt)
# nlp = spacy.load("en_core_web_lg")
# doc = nlp(txt)
# posTag = nltk.pos_tag(tokenized)



#if their is a CC 
#calculate the normal conj from the nlp
def CoordinaryConjunction(doc, posTag):

    count = 0
    for word in posTag:
        if word[1] == 'CC':
            #count += 1
            for token in doc:
                if token.dep_ == 'conj':
                    count += 1
    return count

def count_Phrasel_Verb(doc, posTag):
    arr = [ [word.lemma_ ,child.lemma_] for word in doc if word.pos_ == 'VERB' for child in word.children  if child.pos_ == 'ADP']
    return len(arr)