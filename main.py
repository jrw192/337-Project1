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


def main(year):
	tweets = load_data(year)


	awards=categoriess() #list of awards
	winners=mains() #dictionary, of awards keys with associated winners as values
	
	presenters = find_all_presenters(tweets, awards) #returns dictionary, of awards keys with associated presenters as values

	results = {}
	



	# dicts={}
	# final={"Host":[]} #function for host
	# awardname={}
	# for i in awards:
	# 	awardname[i]={"Presenters":[],
	# 				  "Nominees":[],
	# 				  "Winner": winners[i]}
	

	# print(awardname)
	






if __name__ == "__main__":
	main()