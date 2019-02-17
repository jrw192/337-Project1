import nltk
import string
import re
from nltk.tokenize import TweetTokenizer
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from find_nominated_people import *
from find_names import *
from find_films import *
from find_hosts import *
from find_presenters import *


#imports from other files
from filtercategories_d import filter_tweets
from loaddatscategories_d import load_data
from itertools import islice

def findwinner(dicts, original,limit): #filters out tweets to find ones that mention the winners
	wins={}
	for i in dicts:
		if i[0] > limit and "#" not in i[1]:
			wins[i[1]]= ""

	

	strings=""
	for i in wins:
		h={}
		if "–" in i:
			gemp= i.replace("– ", "")
			strings=gemp
		else:
			strings=i
		texts=""
		tokens=[]
		splits=[]
		splits2=[]
		splits3=[]
		splits=strings.split()
		for word in strings.split():
		 	splits2.append(word.lower())
		splits3=" ".join(splits2)

		for token in original:
			if (strings in " ".join(token)):
				for j in token:
					j=j.lower()
				if "goes" in token and "to" in token and len(token)>2:
					tokens.append(token)				
				elif not tokens:
					for j in token:
						if j.lower() == "wins" or j.lower() == "won":
							tokens.append(token)
			textss=textss.append(token)
			elif (splits3 in " ".join(token)):
				for j in token:
					j=j.lower()
				if "goes" in token and "to" in token and len(token)>2:
					tokens.append(j)		
				elif not tokens:
					for j in token:
						if j.lower() == "wins" or j.lower() == "won":
							tokens.append(j)
				elif "tv" in splits3:
					if "goes" in token and "to" in token and len(token)>2:
						for j in token:
							if "tv" == j or "television" ==j:
								tokens.append(token)
				textss=textss.append(token)


		
		#sending it off to the other functions, turning it into one long string of texts so other functions can read it
		# textss is all the tweets that talk about each category and ptextss is just a copy of what's in textss
		ptextss=""
		for i in textss:
			for j in i:
				ptextss=" ".join(j)
		ptextss+=ptextss
		winner=""
		possiblewinner =find_names(ptextss)
		if (possiblewinner == None):
			winner=possiblewinner
		else:
			winner=possiblewinner

		wins[i]={"Winner": winner
				"Nominees" : find_nominees(ptextss)
				"Presenters":associate_presenters_awards(ptextss)
				"Hosts": find_hosts(ptextss)}

	print(wins[i])

