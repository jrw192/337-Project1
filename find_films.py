from imdb import IMDb
from imdb.Person import Person
import nltk
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
import re
import string


tt = TweetTokenizer()
ia = IMDb()
ps = PorterStemmer()
stop_words = list(stopwords.words("english")) + list(string.punctuation)

def imdb_film_search(query, year):
	# print("cross referencing %s with imdb...." % query)

	matches = ia.search_movie(query)
	if len(matches) > 0 :
		movie_year = int(matches[0]['year'])
		if matches[0]['title'].lower() == query.lower() and (movie_year <= int(year) and movie_year >= int(year)-2):
			#print("FOUND: ", matches[0]['title'])
			return matches[0]['title']
	return None

def clean_tweet(tweet):
	# print("cleaning tweet....")
	cleaned = re.sub(r'[#@][\w]+', '',tweet) #remove all hashtags 
	cleaned = re.sub(r'http://.+', '', cleaned) #remove all links
	cleaned = re.sub(r'[^\w\s]', '', cleaned) #remove all punctuation characters
	
	return cleaned

##find NNP entities in one tweet
def find_entities(text):
	#print("finding entities in tweet....")
	entities = []
	cleaned = clean_tweet(text)
	tokenized = tt.tokenize(cleaned)
	tagged = nltk.pos_tag(tokenized)
	for item in tagged:
		if item[1] == "NNP":
			entities.append(item[0])
	return entities

##try n-grams of words
def find_names(text, entities, year):
	#print("finding names from entity list....")
	# common_award_words = ['director', 'best', 'picture', 'film', 'movie', 'television']
	names = []
	cleaned = clean_tweet(text)
	tokenized = tt.tokenize(cleaned)
	for entity in entities:
		#print("testing entity: %s" % entity)
		# if entity.lower() not in common_award_words:
			newTokens = tokenized[tokenized.index(entity):]
			#print(newTokens)
			title = []
			last = min(5, len(newTokens))
			for i in range(0, last): #most films aren't longer than five words long
				title.append(newTokens[i])
				test = ps.stem(newTokens[i])
				if test not in stop_words: #movie titles don't end in a stopword
					#print("searching film title: " , title)
					if imdb_film_search(" ".join(title), year):
						names.append(" ".join(title))
	# print(names)
	return names

		
	
def find_all_names(text, year): #takes in the raw text of a tweet, returns a list of films identified from the tweet.
	entities = find_entities(text)
	#names = find_names(entities)
	names = find_names(text, entities, year)
	return names


# if __name__ == "__main__":
# 	argoTweets = ['#Congratulations to @BenAffleck for winning the best Director award for Argo at the golden globes!! FANTASTIC MOVIE http://t.co/TZ47heFF',
# 			'RT @CNNshowbiz: Best director motion picture #GoldenGlobe awarded to Ben Affleck for "Argo" #GoldenGlobes',
# 			'@BenAffleck Congratulations‼! Best Director for #Argo! #GoldenGlobes',
# 			'RT @RajeevMasand: GoldenGlobes: Best Film Drama - Argo!  That is the right choice, baby!',
# 			'Golden Globes Best Picture (drama) won by Argo, Best Musical/ Comedy taken by Les Miserables with Hugh Jackman as best Actor for his role.']
# 	find_all_names(argoTweets[0])






