import nltk
import string
import re
from nltk.tokenize import TweetTokenizer
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer


#imports from other files
from filtercategories_d import filter_tweets
from loaddatscategories_d import load_data
from itertools import islice

def findwinner(dicts, original,limit):
	wins={}
	for i in dicts:
		if i[0] > limit and "#" not in i[1]:
			wins[i[1]]= ""

	

	strings=""
	for i in wins:
		
		if "–" in i:
			gemp= i.replace("– ", "")
			strings=gemp
		else:
			strings=i
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
			elif (splits3 in " ".join(token)):
				for j in token:
					j=j.lower()
				if "goes" in token and "to" in token and len(token)>2:
					tokens.append(j)		
				elif not tokens:
					for j in token:
						if j.lower() == "wins" or j.lower() == "won":
							tokens.append(j)
		

		wins[i]={"Winner":goesto(tokens, strings)}
	print(wins)


	
def goesto(texts, category):

	winn=[]
	winners=[]
	newlist=[]
	inde=0
	index3=0
	index4=0
	index5=0
	index6=0

	stop_wordss=list(string.punctuation) + [" , ", "..." ,"…", "for", "RT", "go", "way", "SURPRISE", 'NOT',"A" ]+list(stopwords.words("english"))
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
	winner_name = " ".join([k for k, v in winnerss.items() if v == maximum])



	return winner_name


