tweets = load_tweets()

awards_dict = {} #key: award_name, value = awards
people_dict = {} #key: person, value = count


def populate_winners():
	stemmed = stem_tweets(tweets)
	relevant = filter_tweets(stemmed, 'win', caseSensitive=False)

	

