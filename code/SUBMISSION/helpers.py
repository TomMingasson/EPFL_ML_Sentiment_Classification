import numpy as np



''' 
Extracts a dictionary from the .txt file of GloVe Stanford, words are the keys of the dictionary that is composed of the features value for each word.
REMEMBER to set your current directory to the one of .txt file!

Args:
filename (str): name of the file to open

Returns:
dict: extracted glove dictionary

'''
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



'''
Read the vocabulary text file which contains the list of word and the occurrences. 
## REMEMBER to set your current directory to the one of .txt file!

Args:
filename (str): name of the file to open

Returns: 
(dict): dictionnary of words as keys and occurences as values
'''
def read_vocab(filename):
    
    dict_ = {}
    with open(filename, 'r', encoding='utf-8-sig') as datafile:
        for line in datafile:
            occurence = line.strip().split()[0]
            word = line.strip().split()[1]
            dict_[word] = int(occurence)
    return dict_



'''
Extracts from a .txt of tweets the list containing each tweet, the tweets are np.arrays of words, type np.strings
## REMEMBER to set your current directory to the one of .txt file!

Args:
filename (str): name of the file to open

Returns: 
(list<str>): list of tweets
'''
def build_tweets_matrix (filename):
    
    tweets = []
    with open(filename, 'r',encoding="utf8") as f:
        for line in f:
            vector = []
            for word in line.strip().split(' '):
                vector.append(word)
            tweets.append(np.asarray(vector))
            
        f.close();
    
    return tweets



'''
Process the list containing each tweet (arg: tweets) by cutting the end of tweets that are longer than (arg:size) andzero-padding the ones that are shorter

Args:
tweets(list<str>): list of tweets to be padded
size(int): # of words to include in the windowing

Returns:
(list): tweets of the same dimension but padded
'''
def tweet_cut_ZP(tweets, size):
    for i in range(len(tweets)):
        if(len(tweets[i]) > size):
            tweets[i] = tweets[i][0:size]
        elif(len(tweets[i]) < size):
            tweets[i] = np.append(tweets[i][:], np.asarray( ['0'] * ( size-len(tweets[i]) ) ) )
            
    return tweets



'''
Creates numerical representation vector of the tweets given the embedding dictionary and normalized using the tfidf method described in the report.

Args:
words_in_tweet_list(list<str>): list of all tweets
embedding_dict(dict)          : dictionary of embeddings for each word
tfidf_dict(dict)              : tfidf dictionary
stop_word_list(list<str>)     : list of stopwords to include in the preproc
tfidf(bool)                   : boolean for using the tfidf scaling or not

Returns:
(numpy array): representartion embeddings of each tweet
'''
def build_tweet_vector(words_in_tweet_list, embedding_dict, tfidf_dict, stop_word_list, tfidf_bool):
    
    # tweet matrix
    X_tweet = []
    
    for word in words_in_tweet_list:
        
        if word in embedding_dict and not word in stop_word_list:
            
            # read embedding
            word_vector = embedding_dict[word]
            
            # normalize using tfidf
            if tfidf_bool:
                tfidf = tfidf_dict[word][0]*tfidf_dict[word][1]
                word_vector = word_vector*tfidf
                
            # add to tweet matrix
            X_tweet.append(word_vector)
    
    # if non empty tweet matrix
    if X_tweet:

            # take the mean
            X_tweet_processed = np.mean(X_tweet, 0)

    else:
        
        print("'" + ' '.join(words_in_tweet_list) + "' is an empty tweet.")
        X_tweet_processed = []
    
    return X_tweet_processed
