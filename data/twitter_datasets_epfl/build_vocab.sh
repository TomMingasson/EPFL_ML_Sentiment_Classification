#!/bin/bash

# Note that this script uses GNU-style sed. On Mac OS, you are required to first
#    brew install gnu-sed --with-default-names
cat all.txt | sed "s/ /\n/g" | grep -v "^\s*$" | sort | uniq -c > vocab_all.txt