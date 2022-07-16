import text_proccessing
import spacy
minGenrePercent = 60
min_article_length = 100

log = open('./log.txt', 'w+' , encoding='utf-8')

result_path = "../result"
data_set_path = "../data_set/"
abbreviation_location = './Abbreviaiton list.xlsx'
links_save_point_location = './Links.csv'
number_threads = 1


nlp = spacy.load("en_core_web_lg")

categories = ["tech", "sport", "business", "politics", "entertainment", "other"]
forbidden_ends = (".svg", ".png", ".jpg", ".jpeg", ".gif")

rules_results = {
    "Coordinary Conjunction": dict.fromkeys(categories, 0),
    "Phrasal Verb": dict.fromkeys(categories, 0),
    "Abbreviation": dict.fromkeys(categories, 0),
    'Subordinating conjunctions': dict.fromkeys(categories, 0), # this will count as 3 instead of 1 in the total
    'Noun and its identifier': dict.fromkeys(categories, 0),
}

rules_fun = {
    'Coordinary Conjunction': text_proccessing.CoordinaryConjunction,
    'Phrasal Verb': text_proccessing.count_Phrasal_verb,
    'Abbreviation': text_proccessing.count_Abbreviation,
    'Subordinating conjunctions': text_proccessing.count_Subordinating_conjunctions,
    'Noun and its identifier': text_proccessing.count_Pre_Proper_Noun,
}

rules_abbrv = {
    'Coordinary Conjunction': "CC",
    'Phrasal Verb': "PV",
    'Abbreviation': "AB",
    'Subordinating conjunctions': "SC",
    'Noun and its identifier': "PPN",
}

website_list = {
    'New York Post' : 'https://nypost.com/',
    'The Wall Street Journal' : 'https://www.wsj.com/',
    'The New York Times' : 'https://www.nytimes.com/',
    'The Washington Times' : 'https://www.washingtontimes.com/',
    'The New York Daily News' : 'https://www.nydailynews.com/',
    'The Guardian' : 'https://www.theguardian.com/',
    'bbc' : 'https://www.bbc.com/',
}
