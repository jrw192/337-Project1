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
from find_award_time import find_start_time
from filter_tweets import filter_tweets_by_time
from find_nominees import find_all_nominees
from find_best_dressed import find_best_worst_dressed


def main(year):
	tweets = load_data(year)

	print('GETTING AWARDS')
	awards=categoriess(year) #list of awards
	print('GETTING WINNERS')
	winners=mains(year) #dictionary, of awards keys with associated winners as values
	
	print('GETTING PRESENTERS')
	presenters = find_all_presenters(tweets, awards) #returns dictionary, of awards keys with associated presenters as values

	print('GETTING HOSTS')
	hosts = find_host(tweets)

	print('GETTING NOMINEES')
	nominees = find_all_nominees(tweets, awards)

	#find best and worst dressed
	print('GETTING BEST/WORST DRESSED')
	temp_tuple = find_best_worst_dressed(tweets) # returns a tuple (best_dressed, worst_dressed)
	best_dressed = temp_tuple[0]
	worst_dressed = temp_tuple[1]

	dressed = {}
	dressed['best'] = best_dressed
	dressed['worst'] = worst_dressed

	print('FORMATTING DATA')
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
	
	# print(results)
	print (get_human_readable_format(results, awards, dressed))
	return results

def get_human_readable_format(results_dict, award_dict, dressed_dict):
	category_types = ["presenters", "nominees", "winners"]
	extra_categories = ["best", "worst"]

	string_formatted = text_formatter_helper("hosts", results_dict['hosts']) + "\n"

	for award in award_dict:
		string_formatted += text_formatter_helper("award", award)

		for category in category_types:
			string_formatted += text_formatter_helper(category, results_dict[award][category])
		string_formatted += "\n"
	for category in extra_categories:
		string_formatted += text_formatter_helper(category + " Dressed", dressed_dict[category])

	return string_formatted

def text_formatter_helper(cat_type, data):
	out_string = cat_type.capitalize() + ": "
	if isinstance(data, str):
		out_string += data + "\n"
	elif isinstance(data, list):
		for elem in data:
			out_string += elem + ", "
		out_string = out_string[:-2] + "\n" # remove comma space from last element
	return out_string

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