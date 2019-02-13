from load_data import load_data
from filter_tweets import filter_tweets
from imdb_search import find_all_names

import nltk
from nltk.tokenize import TweetTokenizer
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import string
import re

def clean_tweet(tweet):
	print("cleaning tweet....")
	cleaned = re.sub(r'#[a-z 0-9]+', '',tweet) #remove all hashtags 
	cleaned = re.sub(r'[^\w\s]','',cleaned) #remove all punctuation characters

	
	print(cleaned)

def tokenize(matches):
	print("tokenizing....")
	tt = TweetTokenizer() #use the tweet tokenizer for better results
	tokenized = []
	for match in matches:
		tokenized.append(tt.tokenize(match))
	return tokenized

def remove_stopwords(tokenized_matches):
	print("removing stopwords....")
	stop_words = list(stopwords.words("english")) + list(string.punctuation)
	sans_stopwords = [] #we could also remove from tokenized_matches
	for token in tokenized_matches:
		token_new = []
		for word in token:
			if word.lower() not in stop_words:
				token_new.append(word)
		sans_stopwords.append(token_new)
	return tokenized_matches

def main():
	tweets = load_data()

	matches = filter_tweets(tweets, 'Amy Adams', False)
	tokenized_matches = remove_stopwords(tokenize(matches))
	string_matches = remove_stopwords(matches)
	print("there are %s tokenized matches...." % len(tokenized_matches))
	
	names = find_all_names(string_matches)
	print(names)



if __name__ == "__main__":
	#clean_tweet("hi, i'm jodie wei and it's nice to meet you! #twitter #hashtag")
	main()





