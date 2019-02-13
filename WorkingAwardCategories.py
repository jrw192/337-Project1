#python library imports
import nltk
import string
from nltk.tokenize import TweetTokenizer
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer


#imports from other files
from filter_tweets import filter_tweets
from load_data import load_data

def main(param):
	tweets = load_data()

	#get all tweets containing args[1] the regex search parameter.
	#generally, we want to do search by the award name, then determine the winner from the results.
	matches = filter_tweets(tweets, param, False)

	#tokenize each of the matches
	#here, we create an array tokenized_matches where each index is a tokenized list of a tweet's text.
	tt = TweetTokenizer() #use the tweet tokenizer for better results
	tokenized_matches = []
	for match in matches:
		tokenized_matches.append(tt.tokenize(match))

	# we probably want to remove stopwords and do stemming/lemmatization after we search for award names,
	# so they don't get distorted

# /*
# 	#remove stop words
# 	stop_words = list(stopwords.words("english")) + list(string.punctuation)
# 	sans_stopwords = [] #we could also remove from tokenized_matches
# 	for token in tokenized_matches:
# 		token_new = []
# 		for word in token:
# 			if word.lower() not in stop_words:
# 				token_new.append(word)
# 		sans_stopwords.append(token_new)

	#now we want to do stemming/lemmatization on the tokenized text
	#stem(tokens), or something like that.

	# Stemming
	# portstem = PorterStemmer()
	# stem_tokens = []
	# for i in sans_stopwords:
	# 	ports =[]
	# 	for j in i:
	# 		ports.append(portstem.stem(j))
	# 	stem_tokens.append(ports)

	# # Lemmatization
	# lem = WordNetLemmatizer()
	# lem_tokens = []

	# for token in sans_stopwords:
	# 	token_new = []
	# 	for word in token:
	# 		token_new.append(lem.lemmatize(word,"v"))
	# 	lem_tokens.append(token_new)

	#try feature engineering with n-grams, etc.
	#---some kind of function here---
	index = 0;
	#category=[]
	# categories=[]
	# for i in tokenized_matches:
	# 	#category = []
	# 	for j in i:
	# 		if j == "best" or j == "Best":
	# 			category.append(j)
	# 			index =i.index(j)
	# categories.append(category)
		
	categories=[]
	for i in tokenized_matches:
		if  "best" in i or "Best" in i:
			category = []
			for j in i:
				if j == "best" or j == "Best":
					index =i.index(j)
					category=i[index:]
			categories.append(category)

	final=[]
	index2=0
	for i in categories:
		names=[]
		for j in i:
			j.capitalize()
			if j in list(string.punctuation) or j in list(stopwords.words("english") or j == " , " or j == "goes"):
				index2=i.index(j)
				name=i[:(index2)]
		if len(name)>1:
			final.append(name)


	dicts ={}
	combines=""

	for i in final:
		combines = " ".join(i)
		if combines in dicts:
			dicts[combines] += 1
		else:
			dicts[combines]=1

	print (sorted( ((v,k) for k,v in dicts.items()), reverse=True))
		# for l in k[index:]:
		# 	while l[0] not in list(string.punctuation):
		# 		category.append(l)
		# categories.append(category)



	#print(tokenized_matches)
	# print(sans_stopwords)
	#print('Normal: ', most)
	# print('Stem: ', stem_tokens[0], stem_tokens[1])
	# print('Lem: ', lem_tokens[0], lem_tokens[1])
	return tokenized_matches


if __name__ == "__main__":
	main("argo")