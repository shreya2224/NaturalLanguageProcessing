'''
Created on Apr 24, 2016

@author: ShreyaK
'''
from nltk.corpus import wordnet
from nltk.corpus import stopwords
import csv

cachedStopWords = stopwords.words("english")
'''
pun_words = ["store", "collar", "caller"]
'''
pun_words = ["son","sun","birth","berth","dye","die","maul","mall","odor","order","reel","real",
"collar","caller","board","bore","hertz","hurt","cache","cash","debt","death","feather","federal",
"gourd","guard","jester","gesture","anime","enemy","prophet","profit","sine","sign","altitude","attitude"]

text1= []
final_dist = []

with open('C:/Users/ShreyaK/Desktop/NLP/project/test_set.txt',encoding='utf-8-sig') as fp:
    for line in fp:
        text = ' '.join([word for word in line.split() if word not in cachedStopWords]).split()
        
        text1.append(text)
        
        
       

x = 0


   
for i in range(len(text1)):
    sum_dist = 0
    for j in range(len(text1[i])):
            
        pun = pun_words[x]+"."+"n"+"."+"01"
        other = text1[i][j]+"."+"n"+"."+"01"
                        
        a = wordnet.synset(pun)
        b = wordnet.synset(other)
                        
        sim_set = a.path_similarity(b)
        
        '''        
        print("similarity between "+ pun_words[x]+ " and "+ text1[i][j] + " is: " , sim_set)
        '''
        sum_dist = sum_dist + sim_set
    
    
    final_dist.append(sum_dist)
        
        
    x = x+1            
                
print(final_dist)

existingFile = 'C:/Users/ShreyaK/workspace/MyPython/eng_us_2009-1999-2000-1.csv'

outputfile = 'C:/Users/ShreyaK/workspace/MyPython/output.csv'

p = 1

with open(existingFile, 'r') as csvinput:
    with open(outputfile, 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        reader = csv.reader(csvinput)
        
        all = []
        row = next(reader)
        row.append(final_dist[0])
        all.append(row)
        
        for row in reader:
            row.append(final_dist[p])
            all.append(row)
            p = p+1
        writer.writerows(all)
           
print("done!!!")


    
        