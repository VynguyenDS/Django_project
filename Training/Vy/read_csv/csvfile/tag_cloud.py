import logging
import pandas as pd
from vncorenlp import VnCoreNLP
import re
import numpy as np

import re


# read_data and using NLP create segmentation words
def nlp_tokenize(path):
    data = pd.read_excel(path)
    data = data[['ID', 'Content', 'ID người đăng']]
    data = data.dropna()
    data['Content'] = data['Content'].str.strip()
    data['Content'] = data['Content'].str.lower()
    data['status'] = data['Content']


    for i in range(len(data['status'])):
        data['status'].iloc[i] = re.sub('\W+', ' ', data['Content'].iloc[i])
        data['Content'].iloc[i] = data['status'].iloc[i]
    vncorenlp_file = r'VnCoreNLP/VnCoreNLP-1.1.1.jar'
    vncorenlp = VnCoreNLP(vncorenlp_file)
    # content = vncorenlp.tokenize(content)
    for i in range(len(data['status'])):
        data['status'].iloc[i] = vncorenlp.tokenize(data['status'].iloc[i])
    key_word = []
    for i in data['status']:
        key_word = key_word + i

    vncorenlp.close()
    return key_word, data[['Content', 'ID', 'ID người đăng']]


# processing data
def stop_word(data):
    stop_word = pd.read_excel('data_csv/stopword.xlsx')
    stop_word = list(stop_word['stopword'])
    keywords = sum(data, [])
    keywords = [i.replace('_', ' ') for i in keywords]
    table = []
    for i in keywords:
        if i not in table and (i not in stop_word) and (len(i) > 2):
            table.append(i)
    case = {}
    for i in table:
        case[i] = 0
        for j in keywords:
            if (j in i) and (len(j) == len(i)):
                case[i] = case[i] + 1
    word, frequently = case.keys(), case.values()
    count_word = pd.DataFrame([word, frequently]).T
    count_word.columns = ['word', 'frequently']
    count_word = count_word.sort_values(by='frequently', ascending=False).reset_index()
    count_word = count_word.drop(['index'], axis=1)
    return count_word[0:50]

# data = nlp_tokenize('../data_csv/mitsubishi.xlsx')
# print(data)
#
# count_word = stop_word(data)
# print(count_word)
