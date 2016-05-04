'''
Created on Apr 24, 2016

@author: ShreyaK
'''
import re
from ast import literal_eval
import requests
from pandas import DataFrame
import os.path
from nltk.corpus import stopwords

StopWords = stopwords.words("english")

corpora={'eng_us_2012':17, 'eng_us_2009':5, 'eng_gb_2012':18, 'eng_gb_2009':6, 
    'chi_sim_2012':23, 'chi_sim_2009':11,'eng_2012':15, 'eng_2009':0,
    'eng_fiction_2012':16, 'eng_fiction_2009':4, 'eng_1m_2009':1, 'fre_2012':19, 'fre_2009':7, 
    'ger_2012':20, 'ger_2009':8, 'heb_2012':24, 'heb_2009':9, 
    'spa_2012':21, 'spa_2009':10, 'rus_2012':25, 'rus_2009':12, 'ita_2012':22}



startYear = 1999
endYear = 2000
corpusNumber = 5
corpus = 'eng_us_2009'
smoothing = 1


filename = '%s-%d-%d-%d.csv' % (corpus, startYear,endYear, smoothing)

def getNgrams(query, corpus, startYear, endYear, smoothing):
    
    
    params = dict(content=query, year_start=startYear, year_end=endYear,
                  corpus=corpora[corpus], smoothing=1)
    
    req = requests.get('http://books.google.com/ngrams/graph', params=params)
    res = re.findall('var data = (.*?);\\n', req.text)
    if res:
        data = {qry['ngram']: qry['timeseries']
                for qry in literal_eval(res[0])}
        df = DataFrame(data)
        df_sum = df.sum(axis=1)
        
        final_sum = df_sum.loc[[0]]
        
        
    else:
        df = DataFrame()
        
    
    
    final_sum.to_csv(filename, mode = 'a', header = False, index = False)
    print('Data saved to %s' % filename)
    return req.url, params['content'], df


with open('C:/Users/ShreyaK/Desktop/NLP/project/test_set.txt',encoding='utf-8-sig') as fp:
    for line in fp:
        urlquery = ','.join([word for word in line.split() if word not in StopWords]).split()
        getNgrams(urlquery, corpus, startYear, endYear, smoothing)
