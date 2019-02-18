import nltk
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
import string
import re
from process_tweets import lemmatize_tweet, stem_tweet
from find_films import *
from filter_tweets import filter_tweets_by_time, filter_tweets_text
from find_award_time import *

from load_data import load_data

tt = TweetTokenizer()
ps = PorterStemmer()
stop_words = list(stopwords.words("english")) + ['performance', ]

###
# @param: tweet - string, award - string
# @return: list of names or None
###
def find_nominees(tweet):
	#print("finding award name....")
	text = clean_tweet(tweet).lower()
	text = tt.tokenize(text)

	# nomin = str("nomin")
	# nomin_found = False

  # # stem all
	# stemmed = stem_tweet(text)
	# if "nomin" in stemmed or "nomine" in stemmed:
	# 	nomin_found = True

	nominee_list = []
	# if nomin_found:
	nominee_list = find_all_names(tweet)

	return nominee_list
	

def find_all_nominees(tweet_list, awards_list):
	nominees = {}

	for award in awards_list:
		award_tweet_list = find_tweets_of_award(tweet_list, award)
		
		nominees[award] = []
		for tweet in award_tweet_list:
			results = find_nominees(tweet)
			for result in results:
				if result not in nominees[award]:
					nominees[award].append(result)

	return nominees
			
def find_tweets_of_award(tweet_list, award):
	award_stripped = award
	for word in stop_words:
		award_stripped = award_stripped.replace(" " + word + " ", ' ')
	award_no_punct = re.sub(r'[^\w\s]', '', award_stripped)

	award_tokenized = tt.tokenize(award_no_punct)
	tweets = tweet_list
	for token in award_tokenized:
		filtered = filter_tweets_text(tweets, token, caseSensitive=False)
		if len(filtered) > 0:
			tweets = filtered
	return tweets

if __name__ == "__main__":

	raw_data = load_data('2013')
	time = find_start_time(raw_data, "golden globes")
	rel_tweets = filter_tweets_by_time(raw_data, time)
	print(find_all_nominees(rel_tweets, ['cecil b. demille award', 'best motion picture - drama', 'best performance by an actress in a motion picture - drama', 'best performance by an actor in a motion picture - drama', 'best motion picture - comedy or musical', 'best performance by an actress in a motion picture - comedy or musical', 'best performance by an actor in a motion picture - comedy or musical', 'best animated feature film', 'best foreign language film', 'best performance by an actress in a supporting role in a motion picture', 'best performance by an actor in a supporting role in a motion picture', 'best director - motion picture', 'best screenplay - motion picture', 'best original score - motion picture', 'best original song - motion picture', 'best television series - drama', 'best performance by an actress in a television series - drama', 'best performance by an actor in a television series - drama', 'best television series - comedy or musical', 'best performance by an actress in a television series - comedy or musical', 'best performance by an actor in a television series - comedy or musical', 'best mini-series or motion picture made for television', 'best performance by an actress in a mini-series or motion picture made for television', 'best performance by an actor in a mini-series or motion picture made for television', 'best performance by an actress in a supporting role in a series, mini-series or motion picture made for television', 'best performance by an actor in a supporting role in a series, mini-series or motion picture made for television']))



