## Extracts a dictionary from the .txt file of GloVe Stanford, words are the keys of the dictionary 
## that is composed of the features value for each word.

## REMEMBER to set your current directory to the one of .txt file!

## RETURNS: Dictionary

import numpy as np

def build_glove_dict (filename):
  
    glove_dict = {}
    with open(filename, 'r', encoding="utf8") as f:
        for line in f:
            vector = []
            word = line.split(' ')[0]
            for num in line.strip().split(' ')[1:]:
                vector.append(float(num))
            glove_dict[word] = np.asarray(vector)
            
        f.close()
    
    return glove_dict

## Extracts from a .txt of tweets the list containing each tweet, the tweets are np.arrays of words, type np.strings

## REMEMBER to set your current directory to the one of .txt file!

## RETURNS: list of strings arrays

def build_tweets_matrix (filename):
    
    tweets = []
    with open(filename, 'r') as f:
        for line in f:
            vector = []
            for word in line.strip().split(' '):
                vector.append(word)
            tweets.append(np.asarray(vector))
            
        f.close();
    
    return tweets

## Process the list containing each tweet (arg: tweets) by cutting the end of tweets that are longer than (arg:size) and
## zero-padding the ones that are shorter

## WARNING: the zero padding may have to be done symmetrically, not only in one end.......boh!

## RETURNS: another list of tweets of the same dimension

def tweet_cut_ZP(tweets, size):
    for i in range(len(tweets)):
        if(len(tweets[i]) > size):
            tweets[i] = tweets[i][0:size]
        elif(len(tweets[i]) < size):
            tweets[i] = np.append(tweets[i][:], np.asarray( ['0'] * ( size-len(tweets[i]) ) ) )
            
    return tweets
