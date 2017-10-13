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

def cleanTitle(data):
    title = ''
    if 'concept' in data:
        if '#text' in data['concept']['title'] and 'ph' in data['concept']['title']:
            if isinstance(data['concept']['title']['ph'], list) and 'ph' in data['concept']['title']:
                title = ''
                for i in data['concept']['title']['ph']:
                    title += str(data['concept']['title']['#text']) + str(i['#text']) 
                title = title.split()
            else:
                title = str(data['concept']['title']['#text']) + str(data['concept']['title']['ph']['#tail']) 
                title = title.split()
        elif '#text' in data['concept']['title'] and 'i' in data['concept']['title']:
            if isinstance(data['concept']['title']['i'], list) and 'i' in data['concept']['title']:
                title = ''
                for i in data['concept']['title']['i']:
                    title += str(data['concept']['title']['#text']) + str(i['#text']) 
                title = title.split()
            else:
                title = str(data['concept']['title']['#text']) + ' ' + str(data['concept']['title']['i']['#tail']) 
                title = title.split()
        else:
            title = str(data['concept']['title'])
            title = title.split()
    return title

def cleanDetails(data):
    content = ''
    if 'concept' in data:
        if 'conbody' in data['concept']:
            if isinstance(data['concept']['conbody']['p'], list):
                content = ''
                for j in data['concept']['conbody']['p']:
                    if j is not None:
                        #text = j['#text'] if '#text' in j else ''
                        if '#text' in j:
                            text = j['#text']
                        else:
                            text = ''
                        content += text
                        if 'ph' in j:
                            try:
                                if isinstance(j['ph'], list):
                                    for i in j['ph']:
                                        content += ' ' + i['#tail']
                                else:
                                    content += ' ' + j['ph']['#tail']
                            except TypeError:
                                pass
                        elif 'uicontrol' in j:
                            try:
                                if isinstance(j['uicontrol'], list):
                                    for i in j['uicontrol']:
                                        content += ' ' + i['#tail']
                                else:
                                    content += ' ' + j['uicontrol']['#tail']
                            except TypeError:
                                pass
                        elif 'xref' in j:
                            try:
                                if isinstance(j['xref'], list):
                                    for i in j['xref']:
                                        content += ' ' + i['#tail']
                                else:
                                    content += ' ' + j['xref']['#tail']
                            except TypeError:
                                pass
    return content

def extractSingleFile(filename):
    try:
        with open(filename) as data_file:    
            data = json.load(data_file)
            title = cleanTitle(data)
            content = cleanDetails(data)
            mt = ""
            for r in title:
                r = r.lower()
                if r not in stop_words:
                    mt += " " + r
            mt = re.sub('[^A-Za-z ]+', '', mt)
            print(mt, content)
    except UnicodeError:
        pass
    except KeyError:
        pass


#extractSingleFile("alert_cpt.json")
extractAllFiles()