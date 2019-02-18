#python library imports

#main 

import nltk
import string
from nltk.tokenize import TweetTokenizer
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer


#imports from other files
from filtercategories_d import filter_tweets
from loaddatscategories_d import load_data
from findwinners_d import findwinner
#from findnominations_d import findnoms

def mains():
	tweets = load_data()
	matches = filter_tweets(tweets, False)
	tt = TweetTokenizer() 
	tokenized_matches = []
	for match in matches:
		tokenized_matches.append(tt.tokenize(match))

	index = 0
	winlist =["win", "winner", "won", "winning", "wins"]
	categories=[]

	for i in tokenized_matches:
		i=[x.lower() for x in i]
		if "won" in i or "win" in i or "winner" in i or "winning" in i or "wins" in i:
			if  "best" in i or "Best" in i:
				category = []
				for j in i:
					if j == "best" or j == "Best":
						index =i.index(j)
						category=i[index:]
				categories.append(category)

	stop_wordss=list(string.punctuation) + list(stopwords.words("english"))+ [" , ", "goes","award","for","to", "i", "win", "winner", "...", "category"]
	final=[]
	index2=0
	for i in categories:
		name=[]
		for j in i:
			if j in stop_wordss or "#" in j or"http" in j.lower():
				index2=i.index(j)
				name=i[:(index2)]
				break
		if len(name)>2:
			final.append(name)

	


	dicts ={}
	generaldict={}
	combines=""

	for i in final:
		combines = " ".join([x.capitalize() for x in i])

		if combines in dicts:
			dicts[combines] += 1
		
		else:
			dicts[combines]=1


	listawards=[]

	listawards= sorted(((v,k) for k,v in dicts.items()), reverse=True)
	

	limit=0
	if len(tokenized_matches)>450000:
		limit=20
	elif len(tokenized_matches)<450000 and len(tokenized_matches) >300000:
		limit=12
	else:
		limit=9
	findwinner(listawards,tokenized_matches,limit)


	


if __name__ == "__main__":
	mains()