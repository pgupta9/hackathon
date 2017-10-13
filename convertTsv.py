import json
import os
from pprint import pprint
import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words('english'))

directory = '/Users/ADITYA/data/hack2017/prob2_readOUTInteractingIN/hackathon2017_data/la-help-files/json_en_US/concept/'
os.chdir(directory)

def extractAllFiles() :
    for filename in os.listdir(directory):
        if filename.endswith(".json"): 
            extractSingleFile(filename)
            continue
        else:
            continue

def extractSingleFile(filename):
    try:
        with open(filename) as data_file:    
            data = json.load(data_file)
            title = ''
            if 'concept' in data:
                if '#text' in data['concept']['title'] and 'ph' in data['concept']['title']:
                    if isinstance(data['concept']['title']['ph'], list) and 'ph' in data['concept']['title']:
                        for i in data['concept']['title']['ph']:
                            title = str(data['concept']['title']['#text']) + str(i['#text']) 
                        title = title.split()
                    else:
                        title = str(data['concept']['title']['#text']) + str(data['concept']['title']['ph']['#tail']) 
                        title = title.split()
                elif '#text' in data['concept']['title'] and 'i' in data['concept']['title']:
                    if isinstance(data['concept']['title']['i'], list) and 'i' in data['concept']['title']:
                        title = ''
                        for i in data['concept']['title']['i']:
                            title = str(data['concept']['title']['#text']) + str(i['#text']) 
                        title = title.split()
                    else:
                        title = str(data['concept']['title']['#text']) + ' ' + str(data['concept']['title']['i']['#tail']) 
                        title = title.split()
                else:
                    title = str(data['concept']['title'])
                    title = title.split()
                mt = ""
                for r in title:
                    r = r.lower()
                    if r not in stop_words:
                        mt += " " + r
                mt = re.sub('[^A-Za-z ]+', '', mt)
                print(mt, data['concept']['conbody'])
    except UnicodeError:
        pass
    except KeyError:
        pass


#extractSingleFile("alert_cpt.json")
extractAllFiles()