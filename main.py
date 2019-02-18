#main 
import nltk
import string
from nltk.tokenize import TweetTokenizer
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
#from imdb import IMDb
#from imdb.Person import Person
#import re

#imports from other files
from filtercategories_d import filter_tweets
from loaddatscategories_d import load_data
from findwinners_d import findwinner
from findawardcategories_d import mains
from find_categories import categoriess
from load_data import load_data
from find_presenters import find_all_presenters
from find_hosts import find_host


def main(year):
	tweets = load_data(year)


	awards=categoriess() #list of awards
	winners=mains() #dictionary, of awards keys with associated winners as values
	
	presenters = find_all_presenters(tweets, awards) #returns dictionary, of awards keys with associated presenters as values


	time = find_start_time(tweets, "golden globes")
	rel_tweets = filter_tweets_by_time(tweets, time)
	nominees = find_all_nominees(rel_tweets, awards)
	hosts = find_host(tweets)



	#find best and worst dressed
	temp_tuple = find_best_worst_dressed(tweets) # returns a tuple (best_dressed, worst_dressed)
	best_dressed = temp_tuple[0]
	worst_dressed = temp_tuple[1]

	dressed = {}
	dressed['best'] = best_dressed
	dressed['worst'] = worst_dressed

	results = {}
	results['hosts'] = hosts

	for award in awards:
		award_winner = winners[award]
		award_presenter = presenters[award]
		award_nominees = nominees[award]

		award_dict = {}
		award_dict['winners'] = award_winner
		award_dict['presenters'] = award_presenter
		award_dict['nominees'] = award_nominees


		results[award] = award_dict
	
	print(results)
	return results




def best_worst_to_string(lst):
	count = 0
	result = ''
	for item in lst:
		if count == 0:
			result = item
		elif count == 1:
			result = result + ', ' + item
		else:
			result = result + ' and ' + item
		count += 1
	return result






if __name__ == "__main__":
	main('2013')