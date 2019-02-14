from imdb import IMDb
from imdb.Person import Person
import nltk
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
import string
import re

tt = TweetTokenizer()
ia = IMDb()
ps = PorterStemmer()
stop_words = list(stopwords.words("english")) + list(string.punctuation)


def clean_tweet(tweet):
	#print("cleaning tweet....")
	cleaned = re.sub(r'[#@][\w]+', '',tweet) #remove all hashtags and tagged users
	cleaned = re.sub(r'[^\w\s]','',cleaned) #remove all punctuation (non alphanumeric) characters
	return cleaned

def lemmatize_tweet(tweet):
	lem = WordNetLemmatizer()
	lemmatized = []

	for token in tweet:
		lemmatized.append(lem.lemmatize(token,"v"))
	return lemmatized

#usually, award is either at the end of the tweet, or is followed by "is", or sometimes followed by "award/awarded to", or "goes to"
#e.g. "she won best actress" or "winner of best actress is amy adams"
#therefore we do not want to remove all stop words since they tell us when we reach the end of the award name
#so let's find the word "best", and then add all words from the string until we get to a stopword or the end of the cleaned tweet
def find_award(text):
	#print("finding award name....")
	text = clean_tweet(text).lower()
	text = tt.tokenize(text)
	#print(text)
	lemmatized = lemmatize_tweet(text)
	awardName = []
	bestIndex = lemmatized.index("best")
	if not bestIndex:
		return None
	else:
		common_following_words = ['award', 'win', 'go', 'buy'] #some common words following the award name, not covered by stop words "best buy"
		stop_words = list(stopwords.words("english")) + list(string.punctuation)
		for i in range(bestIndex, len(lemmatized)):
			test = ps.stem(lemmatized[i]) #stem individual test words, stemming entire text fucks literally everything up
			if test not in stop_words and test not in common_following_words:
				awardName.append(lemmatized[i])
				continue
			break
	if len(awardName) == 1:
		return None

	awardName = " ".join(awardName)
	print(awardName)
	return awardName


	

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
			]
	for tweet in tweets:
		find_award(tweet)









