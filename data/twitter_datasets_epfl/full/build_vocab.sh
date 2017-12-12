#!/bin/bash

# Note that this script uses GNU-style sed. On Mac OS, you are required to first
#    brew install gnu-sed --with-default-names
cat all_full_processed.txt | sed "s/ /\n/g" | grep -v "^\s*$" | sort | uniq -c > vocab_all_full_processed.txt