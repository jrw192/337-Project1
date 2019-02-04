#python library imports
import nltk
from nltk.tokenize import TweetTokenizer
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords

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

	#remove stop words
	stop_words = list(stopwords.words("english"))
	sans_stopwords = [] #we could also remove from tokenized_matches
	for token in tokenized_matches:
		for word in token:
			if word.lower() not in stop_words:
				sans_stopwords.append(word)

	#now we want to do stemming/lemmatization on the tokenized text
	#stem(tokens), or something like that.

	#try feature engineering with n-grams, etc.
	#---some kind of function here---

	print(tokenized_matches)
	# print(sans_stopwords)
	return tokenized_matches


if __name__ == "__main__":
	main("argo")