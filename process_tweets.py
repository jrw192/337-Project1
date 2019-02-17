#python library imports
import nltk
import string
from nltk.tokenize import TweetTokenizer
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
import re

#imports from other files
from filter_tweets import filter_tweets
from load_data import load_data

###
# @param: list of strings
# @return: list of lists of strings
###
def tokenize_tweets(tweet_list):
	tt = TweetTokenizer() #use the tweet tokenizer for better results
	tokenized = []
	for tweet in tweet_list:
		tokenized.append(tt.tokenize(tweet))
	return tokenized

###
# @param: list of lists of strings; expects tokenized tweets
# @return: list of lists of strings
###
def remove_stop_words(tweet_list):
	stop_words = list(stopwords.words("english")) + list(string.punctuation)
	sans_stopwords = [] #we could also remove from tokenized_matches

	for tweet in tweet_list:
		tokenized_tweet = []
		for token in tweet:
			if token.lower() not in stop_words:
				tokenized_tweet.append(token)
		sans_stopwords.append(tokenized_tweet)
	return sans_stopwords

###
# @param: list of lists of strings?
# @return: list of lists of strings?
###
def stem_tweets(tweet_list):
	portstem = PorterStemmer()
	stem_tokens = []
	for i in tweet_list:
		ports =[]
		for j in i:
			ports.append(portstem.stem(j))
		stem_tokens.append(ports)
	return stem_tokens

###
# @param: list of strings; expects tokenized tweet
# @return: list of strings
###
def stem_tweet(tweet):
	ps = PorterStemmer()
	stemmed = []
	for token in tweet:
		stemmed.append(ps.stem(token))
	return stemmed

###
# @param: string
# @return: string
###
def clean_tweet(tweet):
	#print("cleaning tweet....")
	cleaned = re.sub(r'[#@][\w]+', '',tweet) #remove all hashtags and tagged users
	cleaned = re.sub(r'[^\w\s]','',cleaned) #remove all punctuation (non alphanumeric) characters
	return cleaned

###
# @param: list of strings
# @return: list of strings
###
def clean_tweet_list(tweet_list):
	cleaned_tweets = []
	for tweet in tweet_list:
		cleaned_tweets.append(clean_tweet(tweet))

	return cleaned_tweets


###
# @param: list of strings
# @return: list of strings
###
def lemmatize_tweet(tweet):
	if isinstance(tweet, str):
		tt = TweetTokenizer()
		tweet = tt.tokenize(tweet)

	lem = WordNetLemmatizer()
	lemmatized = []

	for token in tweet:
		lemmatized.append(lem.lemmatize(token,"v"))

	return lemmatized

###
# @param: 2d list of strings
# @return: 2d list of strings
###
def lemmatize_tweet_list(tweet_list):
	lemmatized_tweets = []
	for tweet in tweet_list:
		lemmatized_tweets.append(lemmatize_tweet(tweet))

	return lemmatized_tweets


##main function
def process_tweets(param):
	tweets = load_data()

	# print ("loaded")

	#get all tweets containing args[1] the regex search parameter.
	#generally, we want to do search by the award name, then determine the winner from the results.
	matches = filter_tweets(tweets, param, False)

	# print ("matches:  " + str(matches[:10]))

	#tokenize each of the matches
	#here, we create an array tokenized_matches where each index is a tokenized list of a tweet's text.
	tokenized_matches = tokenize_tweets(matches)
	# we probably want to remove stopwords and do stemming/lemmatization after we search for award names,
	# so they don't get distorted

	# print ("tokenized matches:  " + str(tokenized_matches[:10]))

	#remove stop words
	sans_stopwords = remove_stop_words(tokenized_matches)

	# print ("sans stopwords:  " + str(sans_stopwords[:10]))

	#now we want to do stemming/lemmatization on the tokenized text
	#stemming
	stemmed = stem_tweets(sans_stopwords)

	# print("stemmed:  " + str(stemmed[:10]))

	# try lemmatization instead
	lemmatized = lemmatize_tweet_list(sans_stopwords)

	# print("lemmatized:  " + str(lemmatized[:10]))
	

	#print(tokenized_matches)
	# print(sans_stopwords)
	#print('Stem: ', stem_tokens[0], stem_tokens[1])
	#print('Lem: ', lem_tokens[0], lem_tokens[1])
	return tokenized_matches


if __name__ == "__main__":
	process_tweets("Amy Adams")