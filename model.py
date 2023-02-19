#!/usr/bin/env python
# coding: utf-8

# In[2]:


'''
from google.colab import drive
drive.mount('/content/drive')
'''


# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df = pd.read_csv('MeTooHate.csv',encoding='latin-1')



# In[3]:


types = np.unique(df.category.values)
evaluation = list(types)


# In[4]:


df = df[['text','category']].dropna()
X = df.text


# In[5]:


y = df.category


# In[6]:


import string
import re

def get_type_index(string):
    return list(types).index(string)

def clean_text(text):
    regex = re.compile('[%s]' % re.escape('|'))
    text = regex.sub(" ", text)
    words = str(text).split()
    words = [i.lower() + " " for i in words]
    words = [i for i in words if not "http" in i]
    words = " ".join(words)
    words = words.translate(words.maketrans('', '', string.punctuation))
    return words


# In[7]:


X = X.apply(clean_text)


# In[8]:



# In[9]:


import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split


# In[10]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)




# In[11]:


import numpy as np
import itertools

## Creating a vectorizer to vectorize text and create matrix of features
## Bag of words technique
class Vectorizer():
    def __init__(self, max_features):
        self.max_features = max_features
        self.vocab_list = None
        self.token_to_index = None

    def fit(self, dataset):
        word_dict = {}
        for sentence in dataset:
            for token in sentence:
                if token not in word_dict:
                    word_dict[token] = 1
                else:
                    word_dict[token] += 1
        word_dict = dict(sorted(word_dict.items(), key=lambda item: item[1], reverse=True))
        end_to_slice = min(len(word_dict), self.max_features)
        word_dict = dict(itertools.islice(word_dict.items(), end_to_slice))
        self.vocab_list = list(word_dict.keys())
        self.token_to_index = {}
        counter = 0
        for token in self.vocab_list:
            self.token_to_index[token] = counter
            counter += 1


    def transform(self, dataset):
        data_matrix = np.zeros((len(dataset), len(self.vocab_list)))
        for i, sentence in enumerate(dataset):
            for token in sentence:
                if token in self.token_to_index:
                    data_matrix[i, self.token_to_index[token]] += 1
        return data_matrix
    
## max features - top k words to consider only
max_features = 2000 

vectorizer = Vectorizer(max_features=max_features)
vectorizer.fit(X_train)

## Checking if the len of vocab = k 
X_train = vectorizer.transform(X_train)
X_test = vectorizer.transform(X_test)


vocab = vectorizer.vocab_list




# In[13]:

from sklearn import metrics
from sklearn import model_selection
from sklearn.linear_model import LinearRegression
import pandas as pd


# In[14]:


#all Features
model  = LinearRegression().fit(X_train,y_train)

# In[15]:




def getBias(str):
    test_list = [str[:len(str)], str[len(str):]]
    
    input_matrix = vectorizer.transform(test_list)
    respond = model.predict(input_matrix)
    return max(respond)

