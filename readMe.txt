The program consists of 3 functions namely:
1. tokenize() -> responsible for splitting th terms, ignoring numbers, removing "'s" from possessives and and any special characters.
2. buildDictionary() -> this function is used to build a dictionary of the tokenized words, returned from the tokenize() function.
3. stemming() -> this function also uses the tokenize() function to tokenize the document and use the NLTK package implementation of the porter algorithm to perform stemming.
A dictionary of the stemmed words similar to the tokenized word dictionary is then built in this function.

The Cranfield text collection has been used as an input for tokenizing and stemming.
Only the contents of the <TEXT> tags have been used as instructed.


Following packages have been used:
-----------------------------------
glob,re,string,time,sys,operator,audioop,xml.dom.minidom
nltk 

Steps needed to run:
====================

Installation of dependencies:
------------------------------
pip3.6 install --user nltk

Code Execution:
--------------
python3.6 tokstem.py /people/cs/s/sanda/cs6322/Cranfield


