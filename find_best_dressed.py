#python library imports
from collections import Counter
from random import randint

#imports from other files
from filter_tweets import filter_tweets, filter_tweets_remove_temp
from find_names import find_all_names


def find_best_worst_dressed(tweets):

	best_dict = best_dressed(tweets)
	worst_dict = worst_dressed(tweets)

	print(best_dict)
	print(worst_dict)

	# print_results(best_dict)
	# print_results(worst_dict)

	best = []
	worst = []

	while len(best) < 3:
		if best_dict: # if best_dict is not empty
			x = max(best_dict, key=best_dict.get)
			best.append(x)
			del best_dict[x]
		else:
			break

	while len(worst) < 3:
		if worst_dict: # if worst_dict is not empty
			x = max(worst_dict, key=worst_dict.get)
			if x not in best: # if person is not already in best dresssed list
				worst.append(x)
			del worst_dict[x]

	print(best)
	print(worst)

	# returns a tuple (can be changed)
	return best, worst


def best_dressed(tweets):
	
	# get matches w best dressed in tweet
	matches = filter_tweets(tweets, 'best dressed', False)
	# matches = filter_tweets(tweets, 'host', False)

	# remove tweets with 'worst' --> just makes it easier
	matches = filter_tweets_remove_temp(matches, 'worst dressed', False)

	# randomize tweets
	matches = randomize_list(matches, 50)

	# return dictionary
	return counter_helper(matches)


def worst_dressed(tweets):
	
	# get matches w best dressed in tweet
	matches = filter_tweets(tweets, 'worst dressed', False)
	# matches = filter_tweets(tweets, 'host', False)

	# remove tweets with 'worst' --> just makes it easier
	matches = filter_tweets_remove_temp(matches, 'best dressed', False)

	# randomize tweets
	matches = randomize_list(matches, 50)

	# return dictionary
	return counter_helper(matches)


def randomize_list(lst, num):
	temp = lst
	if len(temp) > num: # randomize
		newList = []
		while len(newList) < num:
			rando = randint(0, len(temp)-1)
			newList.append(temp[rando])
			del temp[rando]
		temp = newList
	return temp


def counter_helper(tweets):

	matches = tweets
	names = []
	known_names = []

	for match in matches:
		print(match)
		listOfNames = find_all_names(match, known_names, True)

		doNotAdd = False

		for name in listOfNames:
			if name not in known_names:
				known_names.append(name)

			startIndex = match.find(name)
			endIndex = startIndex + len(name)

			if name[startIndex - 1:startIndex] == '(' and name[endIndex + 1:endIndex+2] == ')':
				doNotAdd = True
			elif name[startIndex - 3:startIndex - 1] == 'in':
				doNotAdd = True

			if not doNotAdd:
				names.append(name)

	myDict = dict(Counter(names))
	return myDict

def print_results(myDict):

	namesDict = myDict
	first = max(namesDict, key=namesDict.get)
	del namesDict[first]
	second = max(namesDict, key=namesDict.get)
	del namesDict[second]
	third = max(namesDict, key=namesDict.get)
	del namesDict[third]
	fourth = max(namesDict, key=namesDict.get)
	del namesDict[fourth]
	fifth = max(namesDict, key=namesDict.get)
	del namesDict[fifth]
	print(first + ", " + second + ", " + third + ", " + fourth + ", " + fifth)

	result = [first, second, third, fourth, fifth]
	return result