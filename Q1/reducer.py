#!/usr/bin/env python3
"""reducer.py"""
import sys

current_word = None
current_docs = []

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    
    # parse the input we got from mapper.py
    word, doc_id = line.split('\t', 1)
    
    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word:
        if doc_id not in current_docs:
            current_docs.append(doc_id)
    else:
        if current_word:
            # write result to STDOUT
            print('%s\t%s' % (current_word, ' '.join(current_docs)))
        current_docs = [doc_id]
        current_word = word

# do not forget to output the last word if needed!
if current_word == word:
    print('%s\t%s' % (current_word, ' '.join(current_docs)))

