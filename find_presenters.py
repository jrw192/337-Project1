from filter_tweets import filter_tweets
from filter_tweets import filter_tweets_text
from filter_tweets import filter_tweets_strings_remove
from find_awards import find_award
from find_names import find_all_names  #takes in the raw text of a tweet, returns a list of actor/actress names identified from the tweet.
from load_data import load_data
import re
import string
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
import nltk

tt = TweetTokenizer()
stop_words = list(stopwords.words("english")) + ['performance', ]


def find_award_presenters(tweet_list, award):
	#award_stripped = re.sub(r'[^\w\s]\s', '', award) #remove all non-alphanumeric
	award_stripped = award
	for word in stop_words:
		award_stripped = award_stripped.replace(" " + word + " ", ' ')
	award_no_punct = re.sub(r'[^\w\s]', '', award_stripped)

	award_tokenized = tt.tokenize(award_no_punct)
	all_ngrams = nltk.ngrams(award_tokenized, 2)
	tweets = tweet_list
	for token in award_tokenized:
		#print(token)
		filtered = filter_tweets_text(tweets, token, caseSensitive=False)
		if len(filtered) > 0:
			tweets = filtered

	#tweets = filter_tweets_text(tweet_list, award_stripped, caseSensitive=False) + filter_tweets_text(tweet_list, award, caseSensitive=False) + filter_tweets_text(tweet_list, award_no_punct, caseSensitive=False)
	print(award_tokenized)
	print(len(tweets))
	nameFreqs = {}
	known_names = []
	known_awards = []

	for tweet in tweets:
		#we don't want names that come after the word "to" e.g. "presented to xxx"
		toIndex = re.search(r'\bto\b', tweet)
		if not toIndex:
			toIndex = len(tweet)
		else:
			toIndex = toIndex.start()

		people = find_all_names(tweet[:toIndex], known_names)
		for person in people:
			if person in nameFreqs:
				nameFreqs[person] = nameFreqs[person] + 1
			else:
				nameFreqs[person] = 1
		
	return nameFreqs #returns dictionary of names and frequencies







#pass in all tweets, find the presenters associated with each award
def find_presenters(tweet_list, awardsList):
	presenters = {} #presenters = { award_name : {people} }
	#people = { person_name : count }
	known_names = []
	known_awards = []


	presenter_tweets = filter_tweets(tweet_list, 'present[a-z]*', caseSensitive=False)
	presenter_tweets = filter_tweets_strings_remove(presenter_tweets, 'RT', caseSensitive=True)
	#print(len(presenter_tweets))
	for award in awardsList:
		peopleFreqs = find_award_presenters(presenter_tweets, award)
		presenters[award] = peopleFreqs
		




	return presenters

def find_all_presenters(tweet_list, awards_list):
	possible_presenters = find_presenters(tweet_list, awards_list)
	final_presenters = {} #final result
	#print(possible_presenters.keys())

	#TODO: find top 2 most mentioned people for each award, return as awards_presenters
	for award in possible_presenters:
		people = possible_presenters[award]
		first ={}
		second = {}
		first = ["", 0]
		second = ["", 0]

		for person in people: #find the first person
			if people[person] > first[1]:
				first = [person, people[person]]
		for person in people: #find the second person
			if person != first[0] and people[person] > second[1]:
				second = [person, people[person]]
		print("presenters for %s: %s and %s" % (award, first[0], second[0]))

		presenters = [first[0], second[0]]
		if second[0] == "":
			presenters = [first[0]]
		final_presenters[award] = presenters


	print(final_presenters)
	return final_presenters




if __name__ == "__main__":
	tweets = load_data()
	find_all_presenters(tweets[:100000])









