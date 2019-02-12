from imdb import IMDb
from imdb.Person import Person
import nltk
from nltk.tokenize import TweetTokenizer
import re


tt = TweetTokenizer()
ia = IMDb()

def imdb_name_search(query):
	print("cross referencing %s with imdb...." % query)

	matches = ia.search_person(query)
	if len(matches) > 0 :
		if matches[0]['name'].lower() == query.lower():
			return matches[0]['name']
	return None

def clean_tweet(tweet):
	print("cleaning tweet....")
	cleaned = re.sub(r'#[\w]+', '',tweet) #remove all hashtags 
	cleaned = re.sub(r'[^\w\s]','',cleaned) #remove all punctuation characters
	return cleaned

##find NNP entities in one tweet
def find_entities(text):
	print("finding entities in tweet....")
	entities = []
	cleaned = clean_tweet(text)
	tokenized = tt.tokenize(cleaned)
	tagged = nltk.pos_tag(tokenized)
	for item in tagged:
		if item[1] == "NNP":
			entities.append(item[0])
	return entities

##try all adjacent pairs of NNP to locate names
def find_names(entity_list):
	print("finding names from entity list....")
	names = []
	i = 0
	while i < (len(entity_list)-1):
		testName = entity_list[i] + " " + entity_list[i+1]
		match = imdb_name_search(testName)
		if match :
			names.append(match)
			i += 2 #we found a pair of words that form a name, don't use the last name as the next pass' first name
			continue
		else:
			i += 1
	return names
	
def find_all_names(text): #takes in the raw text of a tweet, returns a list of actor/actress names identified from the tweet.
	entities = find_entities(text)
	names = find_names(entities)
	print(names)
	return names


if __name__ == "__main__":
	#find_entities(['My', 'best', 'dressed', 'go', 'to', '..', '•', 'Eva', 'Longoria', '•', 'Amy', 'Adams', '•', 'Naomi', 'Watts', '•', 'Amanda', 'Seyfried', '#GoldenGlobes'])
	text = "My best dressed go to .. • Eva Longoria • Amy Adams • Naomi Watts • Amanda Seyfried  #GoldenGlobes"
	text1 = "Daniel Day-Lewis wins Best Performance Motion Picture."
	text2 = "i love emily blunt."
	text3 = "I Love Emily Blunt."
	find_all_names(text)






