import numpy as np

def build_tweet_vector(words_in_tweet_list, embedding_dict, tfidf_dict, stop_word_list, method_list):
    
    # tweet matrix
    X_tweet = []
    
    for word in words_in_tweet_list:
        
        if word in embedding_dict and not word in stop_word_list:
            
            # read embedding
            word_vector = embedding_dict[word]
            
            # normalize using tfidf
            if 'tfidf' in method_list:
                tfidf = tfidf_dict[word][0]*tfidf_dict[word][1]
                word_vector = word_vector*tfidf
                
            # add to tweet matrix
            X_tweet.append(word_vector)
    
    # if non empty tweet matrix
    if X_tweet:
        
        # mean of the word vectors
        if 'mean' in method_list:

            X_tweet_processed = np.mean(X_tweet, 0)

        else:

            print("Error: no tweet vector computed.")
            return

    else:
        print("'" + ' '.join(words_in_tweet_list) + "' is an empty tweet.")
        X_tweet_processed = []
    
    return X_tweet_processed