
minGenrePercent = 0.6
min_article_length = 100

result_path = "../result"


categories = ["tech", "sport", "business", "politics", "entertainment", "others"]
rules = ["Coordinary Conjunction", "Phrasel Verb"] # to do

categories_occurences = dict.fromkeys(categories, 0)



website_list = {
    #'New York Post' : 'https://nypost.com/',
    'The Guardian' : 'https://www.theguardian.com/',
    'The New York Times' : 'https://www.nytimes.com/',
    'The Washington Times' : 'https://www.washingtontimes.com/',
    'The Wall Street Journal' : 'https://www.wsj.com/',
    'The New York Daily News' : 'https://www.nydailynews.com/',
    'bbc' : 'https://www.bbc.com/',
    # 'Khaleej Times' : '',
}
websites_num_links = dict.fromkeys(website_list.keys(), 0)
leftLinks = set([])
