## ------------------------------------------------------------------
# The tweet text files "train_neg_full.txt", "train_pos_full.txt" and "test_data.txt" must be in the same folder as the present script "run.py"
## ------------------------------------------------------------------


# setup
print("Setup...")
print(' ')
# ------------------------------------------------------------------

import fasttext
import numpy as np 
import os
from preprocessings import preprocess_txt_file
from create_csv_submission import create_csv_submission
import time
import datetime

# preprocess the tweet text files (full version)
print("Preprocessing")
print(' ')
# ------------------------------------------------------------------

# training tweet text files
print("Generate preprocessed training tweet text files...")

# train_neg_full
infilename = 'train_neg_full.txt'
outfilename = infilename[:-4] + '_processed.txt'
preprocess_txt_file(infilename, outfilename, removeDuplicates=True)

# train_pos_full
infilename = 'train_pos_full.txt'
outfilename = infilename[:-4] + '_processed.txt'
preprocess_txt_file(infilename, outfilename, removeDuplicates=True)

# test tweet text file
print("Generate preprocessed test tweet text files...")

# remove id
outfile = open('test_data_no_id.txt', "w", encoding='utf-8-sig')
with open('test_data.txt', 'r', encoding='utf-8-sig') as f:
    for line in f:
        tweet = line.split(',')[1:]
        outfile.write(''.join(tweet))      
outfile.close()

# preprocess
infilename = 'test_data_no_id.txt'
outfilename = infilename[:-4] + '_processed.txt'
preprocess_txt_file(infilename, outfilename, removeDuplicates=False)


# read the preprocess tweet tect files
print("Read preprocessed tweet text files...")
print(' ')
# ------------------------------------------------------------------

# filenames
fname_neg = 'train_neg_full_processed.txt'
fname_pos = 'train_pos_full_processed.txt'
fname_test = 'test_data_no_id_processed.txt'

# read 
with open(fname_neg, 'r', encoding="utf-8-sig") as f:
    text_neg_tr = f.readlines()
with open(fname_pos, 'r', encoding="utf-8-sig") as f:
    text_pos_tr = f.readlines()
with open(fname_test, 'r', encoding="utf-8-sig") as f:
    text_test = f.readlines()


# format tweets to be readable by fastText model
print("Format tweets...")
print(' ')
# ------------------------------------------------------------------

# format negative tweets
string_to_add = '__label__-1 '
with open(fname_neg, 'r', encoding="utf-8-sig") as f:
    lines = [''.join([string_to_add, x.strip(),'\n']) for x in f]   
with open('mytrain_neg.txt', 'w') as f:
    f.writelines(lines) 

# format positive tweets
string_to_add = '__label__1 '
with open(fname_pos, 'r', encoding="utf-8-sig") as f:
    lines = [''.join([string_to_add, x.strip(),'\n']) for x in f]   
with open('mytrain_pos.txt', 'w') as f:
    f.writelines(lines) 
    
# read formated data
with open('mytrain_pos.txt', 'r', encoding="utf-8-sig") as f1:
    lines1 = f1.readlines()
with open('mytrain_neg.txt', 'r', encoding ="utf-8-sig") as f2:
    lines2 = f2.readlines()    
with open('train_all.txt', 'w') as f:
    f.writelines(lines1)
    f.writelines(lines2)
    
# fastText
print("FastText...")
print(' ')
# ------------------------------------------------------------------

# init: build a cbow model
print("init...")
model = fasttext.cbow('all_full_processed.txt', 'model', ws = 10)

# fit
print("fit...")
classifier = fasttext.supervised('train_all.txt', 'model', label_prefix='__label__')

# predict
print("predict...")
labels = classifier.predict(texts)

# format predictions
y_pred = np.array([int(labels[x][0]) for x in range(len(labels))])

# Submission
print("Create a submission text file...")
print(' ')
# ------------------------------------------------------------------
# output file name
i = datetime.datetime.now()
name = "sub_" + time.strftime("%d_%m_%Y") +  "_%sh_%smin" % (i.hour, i.minute)
ids_test = range(1, test_arrays.shape[0]+1)

# write submission file
create_csv_submission(ids_test, y_pred, name)