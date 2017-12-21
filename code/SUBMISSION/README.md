# Twitter sentiment analysis using linear and non-linear classification


In the Submission folder there are two type of Jupyter Notebooks in .ipynb. The prefix ['PRE_'] is related to pre-processing procedure. The prefix ['MOD_'] is refered to models application.
'build_vocab.sh' and 'cut_vocab.sh' files are the ones provided which allow us to build the vocabulary. These two shell functions were executed importing os library. 

# RUN.PY
WARNING: train_pos_full.txt, train_neg_full.txt and test_data.txt need to be in the SUBMISSION folder.

run.py generates the preprocessed text files from the row text files and then builds the fasttext model trained on the training files and testing on the test file.
The final output is the submission text file.


# HELPERS.PY
In helpers.py there are useful functions to deal with data extraction. Every function is well documented in the file.


# PREPROCESSINGS.PY
This file contains the functions that allow the tokenization and the preprocessing of the words in order to have the most number of them represented by the Stanford GloVe embeddings.


# PREPROCESSING FILES
These codes are necessary in order to generate the text input for our models.

## PRE_build_stop_words
This notebook builds the text file in which there are the stop words, which will be further ignored from the tweets in the K-nearest neighbour and SVM implementation.

## PRE_build_tfdif
Build Term Frequency inverse Document Frequency and save a .txt file

## PRE_generate_txt_preproc
It creates the txt files of the tweets preprocessed (both the short and the full datasets) as described in the report. These files are the ones used in every model applied. 
WARNING : in order to run those model, this notebooks need to be run.

## PRE_pca
PCA implementation and figure generation shown in the report (Figure 2).

## PRE_standford_vs_epfl
It is a comparison between the Stanford vocabulary and the full dataset provided, counting the lacking words in order to check how many words we are losing with the Standford dictionary.


# MODELS FILES
These notebooks are the real application of all our methods.

## MOD_doc2vec
In order to run this notebook gensim needs to be installed. It prepares the input data for the doc2vec function defining a class to label the files in the supervised phase. SVM is used as classifier and prediction are generated for the submission.

REQUIRES: train_neg_processed.txt, train_pos_processed.txt, test_data_no_id_processed.txt generated from PRE_generate_txt_preproc.ipynb

## MOD_doc2vec_tuning
This notebook uses doc2vec model and, as mentioned before, gensim is needed. It tunes  the hyper-parameter gamma and C of the SVM with doc2vec embeddings. It also generates the figure shown in the report. (Figure 3)

## MOD_fasttext
WARNING : this notebook needs to have the all_full_processed.txt generated from PRE_generate_txt_preproc.

This is the implementation of fasttext, also present in the run.py

## MOD_knn
In this notebook K-nearest neighbors is implemented as classifier and generate the submission file. K is initialized after having tuned in the following notebook.

REQUIRES the following text files: 
* GloVe dictionary
* Stop words
* tfdif
* train_neg_processed and train_pos_processed

## MOD_knn_tuning
This is the tuning of the hyper-parameter K for the K-nearest neighbors classifier.

REQUIRES the following text files: 
* GloVe dictionary
* Stop words
* tfdif.txt
* train_neg_processed and train_pos_processed


## MOD_neural_net
TensorFlow and Keras libraries need to be installed, also processbar2.

Implementation of the fully connected neural network, the script will generate the input vector needed for the neural network as explained in the notebook, it will save the sample matrix in multiple files cause there are memory issues. the same script will then reupload those files to build the full matrix and train the network, then a testing phase is done and a kaggle submission file is produced.

REQUIRES the following text files: 
* GloVe dictionary
* all_full_processed or all_short_processed


## MOD_svm
SVM implementation with the hyper-parameters gamma and C are initialiezed with the values optimized in the following notebook. It also generates the submission file.

REQUIRES the following text files: 
* GloVe dictionary
* Stop words
* tfdif.txt
* train_neg_processed and train_pos_processed

## MOD_svm_tuning
SVM hyper-parameters gamma and C optimization and generation of the figure of the accurancy.

REQUIRES the following text files: 
* GloVe dictionary
* Stop words
* tfdif
* train_neg_processed and train_pos_processed




