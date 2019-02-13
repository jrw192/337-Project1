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

def tokenize_tweets(tweet_list):
	tt = TweetTokenizer() #use the tweet tokenizer for better results
	tokenized = []
	for tweet in tweet_list:
		tokenized.append(tt.tokenize(tweet))
	return tokenized


def remove_stop_words(tweet_list):
	stop_words = list(stopwords.words("english")) + list(string.punctuation)
	sans_stopwords = [] #we could also remove from tokenized_matches
	for token in tweet_list:
		token_new = []
		for word in token:
			if word.lower() not in stop_words:
				token_new.append(word)
		sans_stopwords.append(token_new)
	return sans_stopwords

def stem_tweets(tweet_list):
	portstem = PorterStemmer()
	stem_tokens = []
	for i in tweet_list:
		ports =[]
		for j in i:
			ports.append(portstem.stem(j))
		stem_tokens.append(ports)
	return stem_tokens

def lemmatize_tweets(tweet_list):
	lem = WordNetLemmatizer()
	lem_tokens = []

	for token in tweet_list:
		token_new = []
		for word in token:
			token_new.append(lem.lemmatize(word,"v"))
		lem_tokens.append(token_new)
	return lem_tokens


##main function
def process_tweets(param):
	tweets = load_data()

	#get all tweets containing args[1] the regex search parameter.
	#generally, we want to do search by the award name, then determine the winner from the results.
	matches = filter_tweets(tweets, param, False)

	#tokenize each of the matches
	#here, we create an array tokenized_matches where each index is a tokenized list of a tweet's text.
	tokenized_matches = tokenize_tweets(matches)
	# we probably want to remove stopwords and do stemming/lemmatization after we search for award names,
	# so they don't get distorted

	#remove stop words
	sans_stopwords = remove_stop_words(tokenized_matches)
	

	#now we want to do stemming/lemmatization on the tokenized text
	#stemming
	stemmed = stem_tweets(sans_stopwords)
	# try lemmatization instead
	lemmatized = lemmatize_tweets(sans_stopwords)
	

	#print(tokenized_matches)
	# print(sans_stopwords)
	#print('Stem: ', stem_tokens[0], stem_tokens[1])
	#print('Lem: ', lem_tokens[0], lem_tokens[1])
	return tokenized_matches


if __name__ == "__main__":
	process_tweets("Amy Adams")