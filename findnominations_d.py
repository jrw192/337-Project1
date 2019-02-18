import nltk
import string
import re
from nltk.tokenize import TweetTokenizer
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer


#imports from other files
from filter_tweets import filter_tweets
from loaddatscategories_d import load_datas
from itertools import islice

def findnoms(dicts, original):
	wins={}
	for i in dicts:
		if i[0] > 9 and "#" not in i[1]:
			wins[i[1]]= ""
			if "Category" in i[1]:
				splits= i[1].split()
				joins = " ".join(splits[:2])
				wins[joins] = wins[i[1]]
				del wins[i[1]]

	tokens=[]
	for token in original:
		for lows in token:
			lows=lows.lower()
		for i in token:
			if "should" in token:
				index1=token.index("should")
				if token[index1+1] == "have" and token[index1+2] == "won":
					print(token)
					
	
