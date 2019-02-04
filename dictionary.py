#!/usr/bin/python

#=========================================================================#
# Author      : Ankit Vashistha                                           #
# Script      : dictionary.py                                             #
# Py Versions : 3.5                                                       #
# Required    : json, difflib                                             #
# Execute     : python dictionary.py                                      #
#=========================================================================#

import json
import difflib

def searchWord(word):
        if word == "":
            print('\nWord should have atleast one character!')

        elif (word in data.keys()):
            return data[word]

        elif (word.title() in data.keys()):
            return data[word.title()]

        elif (word.upper() in data.keys()):
            return data[word.upper()]

        else:
            closematch = difflib.get_close_matches(word,data.keys())[0]
            confirmation = (input(f"\nDid you mean: {closematch} (y/n): ")).lower()
            if confirmation == 'y':
                return data[closematch]
            else:
                print('Word Not Found in Dictionary')


print('Loading Data...\n')
data = json.load(open('data.json'))
print('Data Loaded!\n')

word = (input('Enter word to lookup in dictionary: ')).lower()

meanings = searchWord(word)
if meanings == list:
    for meaning in meanings:
        print("\nMEANING: "+meaning)
elif meanings != None:
    print("\nMEANING: "+meanings[0])
