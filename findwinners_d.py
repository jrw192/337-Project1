import nltk
import string
import re
from nltk.tokenize import TweetTokenizer
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
# from find_nominated_people import *
# from find_names import *
# from find_films import *
# from find_hosts import *
# from find_presenters import *


#imports from other files
from filtercategories_d import filter_tweets
from loaddatscategories_d import load_data
from itertools import islice

def findwinner(dicts, original):
	wins={}
	for i in dicts:
		wins[i]= ""

	

	strings=""
	for i in wins:
		h={}
		if "–" in i:
			gemp= i.replace("– ", "")
			strings=gemp
		else:
			strings=i

		tokens=[]
		splits=[]
		splits2=[]
		splits3=[]
		textss=""
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
				#textss=textss.append(token)
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
				#textss=textss.append(token)

		#sending it off to the other functions, turning it into one long string of texts so other functions can read it
		# textss is all the tweets that talk about each category and ptextss is just a copy of what's in textss
		#uncomment below for other functions
		# ptextss=""
		# for i in textss:
		# 	for j in i:
		# 		ptextss=" ".join(j)
		# ptextss+=ptextss

		wins[i]=goesto(tokens, strings)
			#uncomment below to see for other functions, 
			# "Nominees" : find_nominees(ptextss)
			# "Presenters":associate_presenters_awards(ptextss)
			# "Hosts": find_hosts(ptextss)
		
	return wins



	
def goesto(texts, category):

	winn=[]
	winners=[]
	newlist=[]
	inde=0
	index3=0
	index4=0
	index5=0
	index6=0

	stop_wordss=list(string.punctuation) + [" , ", "..." ,"…", "for", "RT", "go", "way", "SURPRISE", 'NOT',"A", "FUCK"]+list(stopwords.words("english"))
	news=["BBC","FOX","ABC"]
	for text in texts:
		for low in text:
			low=low.lower()
		
		if "goes" in text and "to" in text:
			index3=text.index("goes")
			if text[index3+1] == "to" and text[index3+2] not in stop_wordss:
				index4 = text.index("to")

				for i in text[(index4+1):]:
					if "#"  in i or "http" in i or i in stop_wordss:
						pass
					elif "@" in i:
						if "_" in i:
							pass
						else:
							for j in news:
								if j.upper() in i.upper():
									pass
								else:
									winn.append(i)
					else:
						winn.append(i)
		else:
			if "wins" in text:
				index3=text.index("wins")
		#print(text)"Wo"
				for i in text[:(index3)]:
					if "#"  in i or "http" in i or i in stop_wordss:
						pass
					elif "@" in i:
						if "_" in i:
							pass
						else:
							for j in news:
								if j.upper() in i.upper():
									pass
								else:
									winn.append(i)
					else:
						winn.append(i)
			if "won" in text:
				index3=text.index("won")
				for i in text[:(index3)]:
					if "#"  in i  or"http" in i or i in stop_wordss:
						pass
					elif "@" in i:
						if "_" in i:
							pass
						else:
							for j in news:
								if j.upper() in i.upper():
									pass
								else:
									winn.append(i)
					else:
						winn.append(i)



	winnerss={}
	

	if not winn:
		return "Winner Already Stated"
	for i in winn:

		if i in winnerss:
			winnerss[i]+=1
		else:
			winnerss[i]=0

	#print(winnerss)

	maximum= max(winnerss.values())
	
	winner_names = (" ".join([k for k, v in winnerss.items() if v == maximum])).replace("@","")
	
		

	#print(winner_names)



	return winner_names
