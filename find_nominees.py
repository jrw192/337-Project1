import nltk
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
import string
import numpy
import re
import copy

from process_tweets import lemmatize_tweet, stem_tweet
import find_names as find_people
import find_films
# from find_people import *
# from find_names import *
from filter_tweets import *
from find_award_time import *

from load_data import load_data

tt = TweetTokenizer()
ps = PorterStemmer()
stop_words = list(stopwords.words("english"))+ ['performance','golden', 'globes', 'best', 'wow', 'excellent', 'great', 'whoo', 'yay', 'winner', 'actor', 'actress' ]

# old attempt
###
# @param: tweet - string, award - string
# @return: list of names or None
###
# def find_nominees(tweet, set_nom, year, award):
# 	#print("finding award name....")
# 	text = clean_tweet(tweet).lower()
# 	text = tt.tokenize(text)

# 	nomin = str("nomin")
# 	nomin_found = False

#   # stem all
# 	stemmed = stem_tweet(text)
# 	if "win" in stemmed or "nomine" in stemmed or "nomin" in stemmed:
# 		nomin_found = True

# 	if nomin_found:
# 		print ("hello")

# 		if "actor" in award or "actress" in award:
# 			try:
# 				poss_names = find_people.find_all_names(tweet)
# 			except:
# 				poss_names = []
# 			for name in poss_names:
# 				set_nom.add(name)
# 		else:
# 			try:
# 				poss_films = find_films.find_all_names(tweet, year)
# 			except:
# 				poss_films = []
# 			for name in poss_films:
# 				set_nom.add(name)
			
# 	return set_nom

def find_nominees(tweet, set_nom, award):
	# clean and tokenize
	o_text = clean_tweet(tweet)
	text = tt.tokenize(o_text)

	# remove stop words
	clean_text = []
	for t in text:
		if t not in stop_words:
			clean_text.append(t)

	# tag tokenized tweet
	tagged = nltk.pos_tag(clean_text)
	names = []
	stemmed = stem_tweet([c.lower() for c in clean_text])

	# check for certain key words for nomination
	nomin_found = False
	# if "win" in stemmed or "go" in stemmed or "nomine" in stemmed or "nomin" in stemmed:
	# 	nomin_found = True

	# use nltk to find person tag
	# if nomin_found:
	tree = nltk.ne_chunk(tagged)
	for t in tree:
		if type(t) == nltk.tree.Tree:
			valid = True
			if t.label() == 'PERSON':
				poss = []
				for c in t:
					if str(c[0]).lower() not in award.lower() and str(c[0]).lower() not in stop_words:
						poss.append(str(c[0]))
				names.append(' '.join([p for p in poss]))

	set_nom_copy = copy.deepcopy(set_nom)

	# check for duplicates
	for n in names:
		if len(set_nom) > 0:
			for s in set_nom_copy:
				if s in n and s in set_nom:
					set_nom.remove(s)
					set_nom.add(n)
				elif n not in s :
					set_nom.add(n)
		else:
			set_nom.add(n)
	
	return set_nom
	
# "main" function that finds tweets suitable for the award and finds nominee names/title
# def find_all_nominees(tweet_list, award_list, year):
def find_all_nominees(tweet_list, award_list):

	tweet_list = filter_tweets_remove(tweet_list, "RT", True)

	nominees = {}
	for award in award_list:
		award_tweet_list = find_tweets_of_award(tweet_list, award)
		award_nominees = set()
		for tweet in award_tweet_list:	
			nom_set = find_nominees(tweet, award_nominees, award)
		for nom in nom_set:
			award_nominees.add(nom)
				
		nominees[award] = list(award_nominees)

	return nominees

# filters for tweets that align with category	
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

# if __name__ == "__main__":
# 	year = '2013'
# 	raw_data = load_data(year)

# 	award_list = ['cecil b. demille award', 'best motion picture - drama', 'best performance by an actress in a motion picture - drama', 'best performance by an actor in a motion picture - drama', 'best motion picture - comedy or musical', 'best performance by an actress in a motion picture - comedy or musical', 'best performance by an actor in a motion picture - comedy or musical', 'best animated feature film', 'best foreign language film', 'best performance by an actress in a supporting role in a motion picture', 'best performance by an actor in a supporting role in a motion picture', 'best director - motion picture', 'best screenplay - motion picture', 'best original score - motion picture', 'best original song - motion picture', 'best television series - drama', 'best performance by an actress in a television series - drama', 'best performance by an actor in a television series - drama', 'best television series - comedy or musical', 'best performance by an actress in a television series - comedy or musical', 'best performance by an actor in a television series - comedy or musical', 'best mini-series or motion picture made for television', 'best performance by an actress in a mini-series or motion picture made for television', 'best performance by an actor in a mini-series or motion picture made for television', 'best performance by an actress in a supporting role in a series, mini-series or motion picture made for television', 'best performance by an actor in a supporting role in a series, mini-series or motion picture made for television']
# 	# # print(find_all_nominees(rel_tweets, ['cecil b. demille award', 'best motion picture - drama', 'best performance by an actress in a motion picture - drama', 'best performance by an actor in a motion picture - drama', 'best motion picture - comedy or musical', 'best performance by an actress in a motion picture - comedy or musical', 'best performance by an actor in a motion picture - comedy or musical', 'best animated feature film', 'best foreign language film', 'best performance by an actress in a supporting role in a motion picture', 'best performance by an actor in a supporting role in a motion picture', 'best director - motion picture', 'best screenplay - motion picture', 'best original score - motion picture', 'best original song - motion picture', 'best television series - drama', 'best performance by an actress in a television series - drama', 'best performance by an actor in a television series - drama', 'best television series - comedy or musical', 'best performance by an actress in a television series - comedy or musical', 'best performance by an actor in a television series - comedy or musical', 'best mini-series or motion picture made for television', 'best performance by an actress in a mini-series or motion picture made for television', 'best performance by an actor in a mini-series or motion picture made for television', 'best performance by an actress in a supporting role in a series, mini-series or motion picture made for television', 'best performance by an actor in a supporting role in a series, mini-series or motion picture made for television']))
# 	print(find_all_nominees(raw_data, award_list))



