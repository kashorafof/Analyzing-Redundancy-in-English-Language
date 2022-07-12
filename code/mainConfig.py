import text_proccessing

minGenrePercent = 60
min_article_length = 100

log = open('./log.txt', 'w+' , encoding='utf-8')

result_path = "../result"
abbreviation_location = './Abbreviaiton list.xlsx'
links_save_point_location = './Links.csv'


categories = ["tech", "sport", "business", "politics", "entertainment", "other"]
forbidden_ends = (".svg", ".png", ".jpg", ".jpeg", ".gif")

rules_results = {
    "Coordinary Conjunction": dict.fromkeys(categories, 0),
    "Phrasel Verb": dict.fromkeys(categories, 0),
    "Abbreviation": dict.fromkeys(categories, 0),
    'Subordinating conjunctions': dict.fromkeys(categories, 0), # this will count as 3 instead of 1 in the total
    'Pre proper noun': dict.fromkeys(categories, 0),
}

rules_fun = {
    'Coordinary Conjunction': text_proccessing.CoordinaryConjunction,
    'Phrasel Verb': text_proccessing.count_Phrasel_Verb,
    'Abbreviation': text_proccessing.count_Abbreviation,
    'Subordinating conjunctions': text_proccessing.count_Subordinating_conjunctions,
    'Pre proper noun': text_proccessing.count_Pre_Proper_Noun,
}

rules_abbrv = {
    'Coordinary Conjunction': "CC",
    'Phrasel Verb': "PV",
    'Abbreviation': "AB",
    'Subordinating conjunctions': "SC",
    'Pre proper noun': "PPN",
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
