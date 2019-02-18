# -*- coding: UTF-8 -*-
from imdb import IMDb
from imdb.Person import Person
import nltk
from nltk.tokenize import TweetTokenizer
import re
from nltk.corpus import stopwords


tt = TweetTokenizer()
ia = IMDb()

def imdb_name_search(query):

	matches = ia.search_person(query)
	if len(matches) > 0 :
		match = re.sub(r'[^\w\s]', '', matches[0]['name'])
		print(match)
		if query.lower() == match.lower():
			print(match, "found")
			return matches[0]['name']
	return None

def clean_tweet(tweet, removeTweetHandles = False):
	cleaned = re.sub(r'#[\w]+', '',tweet) #remove all hashtags 

	#1: for find hosts
	if removeTweetHandles:
		cleaned = re.sub(r'\s@\S+\s', '', cleaned) #remove '@sometwitterhandle: ' (i.e. RT format)
		# because @perezhilton had a popular tweet about worst dressed and was classified as one

	#2: if @ preceded by RT, remove word
	elif "RT" in tweet:
		cleaned = re.sub(r'^RT\s@\S+\s', '', cleaned) #remove 'RT @sometwitterhandle: ' (i.e. RT format)

	#3: if @ not preceeded by RT, remove @ and split word into 2 parts based on capitalization
	# iterate through tweet
	# if you find an @: remove it and split word into 2 based on camelcase
	else:
		start = cleaned.find("@")
		stop = 0
		while start != -1:
			stop = cleaned.find(" ", start)
			temp = camel_case_split(cleaned[start+1: stop]) #remove @ and split camelcase word
			cleaned = cleaned[:start] + temp + cleaned[stop:]
			start = cleaned.find("@")

	cleaned = re.sub(r'[^\w\s]','',cleaned) #remove all punctuation characters
	return cleaned

## split camel case words
## https://stackoverflow.com/questions/29916065/how-to-do-camelcase-split-in-python
def camel_case_split(identifier):
    matches = re.finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', identifier)
    temp = [m.group(0) for m in matches]
    final = ''
    for t in temp:
    	final += t + ' '
    return final[:-1]

##find NNP entities in one tweet
def find_entities(text, removeTweetHandles):
	entities = []
	cleaned = clean_tweet(text, removeTweetHandles)
	tokenized = tt.tokenize(cleaned)
	tagged = nltk.pos_tag(tokenized)
	for item in tagged:
		if item[1] == "NNP":
			entities.append(item[0])
	non_names = ['golden', 'globes', 'red', 'carpet', 'rt', 'nbc', 'tnt', 'enews', 'award', 'best', 'actor', 'actress', 'film', 'picture'] + list(stopwords.words("english"))
	lower_entities = [item.lower() for item in entities]
	for non in non_names:
		if non in lower_entities:
			nonIndex = lower_entities.index(non)
			#print("entities: %s, lower_entities: %s, non: %s, nonIndex: %s" % (entities, lower_entities, non, nonIndex))
			entities.pop(nonIndex)
			lower_entities.pop(nonIndex)
	return entities

##try all adjacent pairs of NNP to locate names
def find_names(entity_list, known_names):
	names = []
	i = 0
	while i < (len(entity_list)-1):
		testName = entity_list[i] + " " + entity_list[i+1]

		match = False
		if testName in known_names:
			print("%s is a known name" % testName)
			match = testName
		else:
			print("cross referencing %s with imdb" % testName)
			match = imdb_name_search(testName)
		if match :
			names.append(match)
			i += 2 #we found a pair of words that form a name, don't use the last name as the next pass' first name
			continue
		else:
			i += 1
	return names
	
def find_all_names(text, known_names=[], removeTweetHandles = False): #takes in the raw text of a tweet and list of known names, returns a list of actor/actress names identified from the tweet.
	entities = find_entities(text, removeTweetHandles)
	names = find_names(entities, known_names)
	print(names)
	return names


if __name__ == "__main__":
	#find_entities(['My', 'best', 'dressed', 'go', 'to', '..', '•', 'Eva', 'Longoria', '•', 'Amy', 'Adams', '•', 'Naomi', 'Watts', '•', 'Amanda', 'Seyfried', '#GoldenGlobes'])
	text = "My best dressed go to .. • Eva Longoria • Amy Adams • Naomi Watts • Amanda Seyfried  #GoldenGlobes"
	text1 = "Daniel Day-Lewis wins Best Performance Motion Picture."
	text2 = "i love emily blunt."
	text3 = "I Love Emily Blunt."
	text4 = "#Congratulations to @BenAffleck for winning the best Director award for Argo at the golden globes!! FANTASTIC MOVIE http://t.co/TZ47heFF"
	text5 = "Finally, the category we've all been waiting for. Best original score, motion picture: Mychael Danna, Life of Pi. #GoldenGlobes"
	text6 = "Tina and Amy hosting golden globes ahhhhh let the humor begin"

	#'#Congratulations to @BenAffleck for winning the best Director award for Argo at the golden globes!! FANTASTIC MOVIE http://t.co/TZ47heFF',
	#		'RT @CNNshowbiz: Best director motion picture #GoldenGlobe awarded to Ben Affleck for "Argo" #GoldenGlobes',
	#		'@BenAffleck Congratulations‼! Best Director for #Argo! #GoldenGlobes',
	#		'RT @RajeevMasand: GoldenGlobes: Best Film Drama - Argo!  That is the right choice, baby!',
	#		'Golden Globes Best Picture (drama) won by Argo, Best Musical/ Comedy taken by Les Miserables with Hugh Jackman as best Actor for his role.'

	#find_all_names(text4)
	imdb_name_search('Daniel DayLewis')







