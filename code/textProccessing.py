
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

def CoordinaryConjunction(txt):
    tokenized = word_tokenize(txt)
    posTag = nltk.pos_tag(tokenized)
    count = 0
    for tag in posTag:
        if(tag[1] == 'CC'):
            count+=+1
    return count

def count_Phrasel_Verb(txt):
    nlp = spacy.load("en_core_web_lg")
    doc = nlp(txt)
    arr = [ [word.lemma_ ,child.lemma_] for word in doc if word.pos_ == 'VERB' for child in word.children  if child.pos_ == 'ADP']
    # for word in doc:
    #     if word.pos_ != 'VERB':
    #         continue
    #     for child in word.children:
    #         if child.pos_ == 'ADP':
    #             print(child)
    # print(len(arr))
    return len(arr)