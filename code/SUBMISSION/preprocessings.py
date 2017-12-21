"""
Adapted from http://nlp.stanford.edu/projects/glove/preprocess-twitter.rb modified by Romain Paulus and Jeffrey Pennington and translated to python by Motoki Wu

Some modifications were applied, here documented
"""

import sys
import re
import os

FLAGS = re.MULTILINE | re.DOTALL

'''
Added longforms: the truncated words like 'm or 'll will be converted into the full form 'am' or 'will'
'''

longforms = {}
longforms[r"'m"] = r" am"
longforms[r"n't"] = r" not"
longforms[r"'s"] = r" is"
longforms[r"'ll"] = r" will"
longforms[r"'re"] = r" are"
longforms[r"'ve"] = r" have"
longforms[r"'d"] = r" would"
    

def hashtag(text):
    text = text.group()
    hashtag_body = text[1:]
    if hashtag_body.isupper():
        result = "<hashtag> {} <allcaps>".format(hashtag_body)
    else:
        result = "<hashtag> {}".format(hashtag_body.lower())
    return result

def allcaps(text):
    text = text.group()
    return text.lower() + " <allcaps>"

def process(text):
    
    # Different regex parts for smiley faces
    eyes = r"[8:=;]"
    nose = r"['`\-]?"

    def re_sub(pattern, repl):
        return re.sub(pattern, repl, text, flags=FLAGS)

    text = re_sub(r"https?:\/\/\S+\b|www\.(\w+\.)+\S*", "<url>")
    text = re_sub(r"/"," / ")
    text = re_sub(r"@\w+", "<user>")
    text = re_sub(r"{}{}[)dD]+|[)dD]+{}{}".format(eyes, nose, nose, eyes), "<smile>")
    text = re_sub(r"{}{}p+".format(eyes, nose), "<lolface>")
    text = re_sub(r"{}{}\(+|\)+{}{}".format(eyes, nose, nose, eyes), "<sadface>")
    text = re_sub(r"{}{}[\/|l*]".format(eyes, nose), "<neutralface>")
    text = re_sub(r"<3","<heart>")
    text = re_sub(r"[-+]?[.\d]*[\d]+[:,.\d]*", "<number>")
    text = re_sub(r"#\S+", hashtag)
    text = re_sub(r"([!?.]){2,}", r"\1 <repeat>")
    text = re_sub(r"\b(\S*?)(.)\2{2,}\b", r"\1\2 <elong>")
    text = re_sub(r"([A-Z]){2,}", allcaps)
    
    for contracted, long in longforms.items():
        text = re_sub(contracted, long)
        
    text = re.sub("\s\s+" , " ", text)

    return text.lower().strip()

'''
Added generate text file function, it applies all the preprocessing for these words in order to adapt them to the Stanford GloVe dictionary

Param:
infilename(str)       : name of file to read
outfilename(str)      : name of file to write
removeDuplicates(bool): removal of duplicates true or false

Returns: 
none
'''

def preprocess_txt_file(infilename, outfilename, removeDuplicates=True):

    # holds lines already seen
    lines_seen = set() 
    cpt_duplicates = 0
    outfile = open(outfilename, "w", encoding='utf-8-sig')
    for line in open(infilename, "r", encoding='utf-8-sig'):
        if line not in lines_seen or not removeDuplicates: # not a duplicate
            outfile.write(process(line)) # processed and write
            outfile.write('\n')
            lines_seen.add(line)
        else:
            cpt_duplicates += 1
    outfile.close()
    if removeDuplicates:
        print("Number of duplicates: ", cpt_duplicates)
    else: 
        print("Eventual duplicates not removed.")

    print("(!!! One new empty line added at the end !!!)") 
