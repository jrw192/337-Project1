from filter_tweets import filter_tweets
from find_awards import find_award
from find_names import find_all_names  #takes in the raw text of a tweet, returns a list of actor/actress names identified from the tweet.
from load_data import load_data

presenters = {} #presenters = { award_name : {people} }
#people = { person_name : count }

#pass in all tweets, find the presenters associated with each award
def find_presenters(tweet_list):
	presenter_tweets = filter_tweets(tweet_list, 'present[a-z]*', caseSensitive=False)
	print(len(presenter_tweets))
	for tweet in presenter_tweets:
		award = find_award(tweet)
		if not award:
			continue
		known_people = list(presenters.keys())
		people = find_all_names(tweet, known_people)
		if not people:
			continue

		if award in presenters:
			curPeople = presenters[award]
			for person in people:
				if person in curPeople:
					curPeople[person] = curPeople[person] + 1
				else:
					curPeople[person] = 1
			presenters[award] = curPeople
		else:
			curPeople = {}
			for person in people:
				curPeople[person] = 1
			presenters[award] = curPeople
	for key in presenters:
		print(key)
	return presenters



if __name__ == "__main__":
	tweets = load_data()
	find_presenters(tweets)





