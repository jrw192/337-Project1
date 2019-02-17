from imdb import IMDb
from imdb.Person import Person
import nltk
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
import string
import re
from process_tweets import lemmatize_tweet, stem_tweet
from find_names import *

tt = TweetTokenizer()
ia = IMDb()
ps = PorterStemmer()
stop_words = list(stopwords.words("english")) + list(string.punctuation)

ia = IMDb()

###
# @param: list of dictionary
# @return: string
###
def imdb_name_search(query):
	print("cross referencing %s with imdb...." % query)

	matches = ia.search_person(query)
	if len(matches) > 0 :
		if matches[0]['name'].lower() == query.lower():
			return matches[0]['name']
	return None

###
# @param: tweet - string
# @return: list of names or None
###
def find_nominees(tweet):
	#print("finding award name....")
	text = clean_tweet(tweet).lower()
	text = tt.tokenize(text)

	lemmatized = lemmatize_tweet(text)
	nomin = str("nomin")
	nomin_found = False

  # stem all
	stemmed = stem_tweet(text)
	if "nomin" in stemmed or "nomine" in stemmed:
		nomin_found = True

	nominee_dict = {}
	if nomin_found:
		nominee_names = find_all_names(tweet)
		nominee_dict = {}
		for name in nominee_names:
			nominee_dict[name] = 0
	
	return nominee_dict

def filter_tweets_by_time(time):
	return None


	

if __name__ == "__main__":
	#find_entities(['My', 'best', 'dressed', 'go', 'to', '..', '•', 'Eva', 'Longoria', '•', 'Amy', 'Adams', '•', 'Naomi', 'Watts', '•', 'Amanda', 'Seyfried', '#GoldenGlobes'])
	argoTweets = ['#Congratulations to @BenAffleck for winning the best Director award for Argo at the golden globes!! FANTASTIC MOVIE http://t.co/TZ47heFF',
			'RT @CNNshowbiz: Best director motion picture #GoldenGlobe awarded to Ben Affleck for "Argo" #GoldenGlobes',
			'@BenAffleck Congratulations‼! Best Director for #Argo! #GoldenGlobes',
			'RT @RajeevMasand: GoldenGlobes: Best Film Drama - Argo!  That is the right choice, baby!',
			'Golden Globes Best Picture (drama) won by Argo, Best Musical/ Comedy taken by Les Miserables with Hugh Jackman as best Actor for his role.']
	#argo won best film: drama, and ben affleck won best director for argo.
	tweets = ['RT @goldenglobes: Best Actress in a Motion Picture - Drama - Jessica Chastain - Zero Dark Thirty - #GoldenGlobes',
			'@BenAffleck Congratulations‼! Best Director for #Argo! #GoldenGlobes',
			'RT @CNNshowbiz: Best supporting actor, motion picture goes to Christoph Waltz for "Django Unchained" #GoldenGlobes',
			'RT @goldenglobes: Best Original Score - Mychael Danna - Life of Pi - #GoldenGlobes',
			'nominees are Amy Adams and Emily Blunt'
			]
	for tweet in tweets:
		find_nominees(tweet)





