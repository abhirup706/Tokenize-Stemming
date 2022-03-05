# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 16:07:11 2022

@author: Abhirup Bhattacharya
"""

#import all the required packages for the code
import glob
import re
import string
import time
import sys
import operator
from operator import itemgetter
from audioop import reverse
import xml.dom.minidom as minidom
import nltk
from nltk.stem.porter import *


#Initialize the count variables below
docCount = 0
tokCount = 0
wordCount = 0
stemCount = 0

#Inilitialize the dictionary for the tokenized and the stmmed words
wordDict = {}
stemDict = {}

#======================
#Part 1 - Tokenization
#======================

#Funcion to tokenize the input sentence
#Input  -> text to be tokenized
#Output -> List of tokens
def tokenize(text):

	#print("text1" + text)
	text = text.replace("\'s","")
	#print("text3"+ text)
	words = re.sub('[^a-zA-Z]+',' ',text).split()
	return [word.strip() for word in words if word.strip() != '']



#Function to parse the Cranfield document and call the tokenize function with the content of <TEXT> Tag
#It builds a dictionary of tokens with the corresponding frequencies

def dictBuild():
	global docCount
	global tokCount

	files = glob.glob(path)

	toklist = []
	
	for file in files:
		docCount += 1
		#file_ptr = open(file,"r")
		file_ptr = minidom.parse(file)
		data = file_ptr.getElementsByTagName('TEXT')[0]
		text = data.firstChild.data
		#sent = file_ptr.read().lower() 
		sent = str(text).lower()
		#print(sent)
		inp_sent = re.sub('<[^>]*>','',sent)
		toklist = tokenize(inp_sent)
		#print(toklist)
		for tok in toklist:

			tokCount += 1 
			#increment count of total number of tokens encountered
			#In case the token is already present in the wordDict, increment the current frequency, 
			#else add an entry in te dictionary with frequency 1
			if tok in wordDict:
				wordDict[tok] += 1
			else:
				wordDict[tok] = 1

		
#Set the path variable to the command line argument provided		
path = sys.argv[1] + "/*"

#Calling the dictBuild function and computing the time taken
startTime = int(round(time.time() * 1000))
dictBuild()
endTime = int(round(time.time() * 1000))

print("\n===================================================================")
print("=====================  TOKENIZATION STATS  =========================")
print("===================================================================\n")

print(" Time taken for tokenization                              : "+ str(endTime-startTime) + " milliseconds")
print(" Number of tokens  in the Cranfield text collection       : "+ str(tokCount))
print(" Number of unique words  in the Cranfield text collection : "+ str(len(wordDict.keys())))

singleWordCount = 0

#Count the number of tokens in the dictionary with frequency 1
for word in wordDict:
	if (wordDict[word] == 1):
		singleWordCount += 1

print(" Number of words occuring once in Cranfield collection    : "+ str(singleWordCount))

#Find the 30 most highest frequency words in the dictionary
print("\n The 30 most frequent words are                           :")
for word in dict(sorted(wordDict.items(), key = itemgetter(1), reverse = True)[:30]):
	print("  "+word + " : " + str(wordDict[word]))


avgWord = tokCount/docCount

print("\n Average words per document in Cranfield collection       : "+ str(avgWord))



#======================
#Part 1 - Temming
#======================

#Function to stem the tokens and build a dictionary of stems

ps = PorterStemmer() #create object of the PorterStemmer() Class

def stemming():
	files = glob.glob(path)

	global tokList
	global docCount
	global stemCount

	for file in files:
		docCount += 1

		file_ptr = minidom.parse(file)
		data = file_ptr.getElementsByTagName('TEXT')[0]
		text = data.firstChild.data
		#sent = file_ptr.read().lower() 
		sent = str(text).lower()
		#print(sent)
		inp_sent = re.sub('<[^>]*>','',sent)
		toklist = tokenize(inp_sent)

		for tok in toklist:
			stemCount += 1
			stemWord = ps.stem(tok)
			if stemWord in stemDict:
				stemDict[stemWord] += 1
			else:
				stemDict[stemWord] = 1

docCount = 0

#Calling the stemming function and computing the time taken
startTime = int(round(time.time() * 1000))
stemming()
endTime = int(round(time.time() * 1000))

#Count the number of stems in the dictionary with frequency 1
singleStemCount = 0
for stem in stemDict:
	if (stemDict[stem] == 1):
		singleStemCount += 1

print("\n")

print("\n===================================================================")
print("====================  STEMMING STATS  =============================")
print("===================================================================\n")

print()

#List of unique stems are the list of keys in the stem-frequency dictionary
stemCount = len(stemDict.keys())
print(" Time taken for Stemming                                       : "+ str(endTime-startTime) + " milliseconds")
print(" Number of stems in the Cranfield text collection              : "+ str(stemCount))
print(" Number of word stems occuring once in Cranfield collection    : "+ str(singleStemCount))

#Finding the 30 most frequent stemmed words with the frequencies
print("\n The 30 most frequent stems are                           :")
for word in dict(sorted(stemDict.items(), key = itemgetter(1), reverse = True)[:30]):
	print("  " + word + " : " + str(stemDict[word]))

avgStem = stemCount/docCount

print("\n Average stems per document in Cranfield collection          : "+ str(avgStem))
