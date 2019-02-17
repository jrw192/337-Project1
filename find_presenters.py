from filter_tweets import filter_tweets
from find_awards import find_award
from find_names import find_all_names  #takes in the raw text of a tweet, returns a list of actor/actress names identified from the tweet.
from load_data import load_data
import re




#pass in all tweets, find the presenters associated with each award
def find_presenters(tweet_list):
	presenters = {} #presenters = { award_name : {people} }
	#people = { person_name : count }
	known_people = []


	presenter_tweets = filter_tweets(tweet_list, 'present[a-z]*', caseSensitive=False)
	print(len(presenter_tweets))
	for tweet in presenter_tweets:
		#print(tweet)
		award = find_award(tweet)
		if not award:
			continue

		#we don't want names that come after the word "to" e.g. "presented to xxx"
		toIndex = re.search(r'\bto\b', tweet)
		if not toIndex:
			toIndex = len(tweet)
		else:
			toIndex = toIndex.start()

		people = find_all_names(tweet[:toIndex], known_people)
		if not people:
			continue
			
		known_people += people

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
	# for key in presenters:
	# 	print(key)
	return presenters

def associate_presenters_awards(tweet_list):
	possible_presenters = find_presenters(tweet_list)
	final_presenters = {} #final result
	print(possible_presenters.keys())

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
	associate_presenters_awards(tweets[:50000])









