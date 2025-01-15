import os
import cv2
import pandas as pd
import nltk
import dataset

nltk.download('punkt_tab')

# csv file path
csv_path = 'data.csv'
df = dataset.get_data()
df.to_csv(csv_path,index=False)

# get data from csv file
def get_data(path=csv_path):
    
    return df

# add new_data to csv file
def add_data(image,description):
    new_data = pd.DataFrame({
        'Chemin_d_acces': [image],
        'Description': [description]
    })
    df = pd.concat([df,new_data],ignore_index=True)
    df.to_csv(csv_path,index=False)
    
# remove data from csv file
def remove_data(index):
    df.drop(index,inplace=True)
    df.to_csv(csv_path,index=False)

# to get the corpus of the descriptions
def get_corpus():
    corpus = []
    for i in range(len(df)):
        corpus.append(df['Description'][i])
    return corpus

# to plot an image
def plot_image(index):
    img = cv2.imread(df['Chemin_d_acces'][index])
    cv2.imshow('Image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

# to get the description of an image
def get_description(index):
    return df['Description'][index] 

def get_tokenized_corpus():
    corpus = get_corpus()
    tokenized_corpus = []
    for sentence in corpus:
        tokenized_sentence = nltk.word_tokenize(sentence)
        tokenized_corpus.append(tokenized_sentence)
    return tokenized_corpus

# to tokenize a sentence
def tokenize(sentence):
    return nltk.word_tokenize(sentence)
