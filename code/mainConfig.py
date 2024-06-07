# used to configure the whole script

import text_proccessing
import spacy

# variable to control what is the minimum percentage to consider the article as a specific category
# if the article is categorized with less than this percentage will consider it as other
minGenrePercent = 60

# minimum length for the article to pass through the filter 
min_article_length = 100
# any links that ends with this will not pass through the links filter
forbidden_ends = (".svg", ".png", ".jpg", ".jpeg", ".gif")


log = open('./log.txt', 'w+' , encoding='utf-8')

# path to save the result
result_path = "../result"
# path to the data set
data_set_path = "../result/data_set/"
# path to the abbreviation excel file
abbreviation_location = './Abbreviaiton list.xlsx'
# path to the links saving point 
# using the last link so the next time the script run it will start from the last link
links_save_point_location = './Links.csv'
# used for multithreading "more threads -> faster analysis"
number_threads = 1

# will use the large model of spacy because it is more accurate 
# nlp "spacy library" is used to process the text rather than counting the words it self 
nlp = spacy.load("en_core_web_lg")

# list of the main category "stuck with the AI model"
categories = ["tech", "sport", "business", "politics", "entertainment", "other"]


# dictionary maps each rule to its occurance in each category
rules_results = {
    "Coordinary Conjunction": dict.fromkeys(categories, 0),
    "Phrasal Verb": dict.fromkeys(categories, 0),
    "Abbreviation": dict.fromkeys(categories, 0),
    'Subordinating conjunctions': dict.fromkeys(categories, 0), # this will count as 3 instead of 1 in the total
    'Noun and its identifier': dict.fromkeys(categories, 0),
}

# dictionary maps each rule to its function
rules_fun = {
    'Coordinary Conjunction': text_proccessing.CoordinaryConjunction,
    'Phrasal Verb': text_proccessing.count_Phrasal_verb,
    'Abbreviation': text_proccessing.count_Abbreviation,
    'Subordinating conjunctions': text_proccessing.count_Subordinating_conjunctions,
    'Noun and its identifier': text_proccessing.count_Pre_Proper_Noun,
}

# abbreviation for each rule to be used in the excel file 
rules_abbrv = {
    'Coordinating conjunction': "CC",
    'Phrasal Verb': "PV",
    'Abbreviation': "AB",
    'Subordinating conjunction': "SC",
    'Noun and its identifier': "PPN",
}

# dictionary maps each category to its link 
website_list = {
    'New York Post' : 'https://nypost.com/',
    'The Wall Street Journal' : 'https://www.wsj.com/',
    'The New York Times' : 'https://www.nytimes.com/',
    'The Washington Times' : 'https://www.washingtontimes.com/',
    'The New York Daily News' : 'https://www.nydailynews.com/',
    'The Guardian' : 'https://www.theguardian.com/',
    'bbc' : 'https://www.bbc.com/',
}
