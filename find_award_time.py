# -*- coding: UTF-8 -*-
import datetime
import re
from load_data import load_data

def clean_tweet(tweet):
	print("cleaning tweet....")
	cleaned = re.sub(r'#[\w]+', '',tweet) #remove all hashtags 

	#1: if @ preceded by RT, remove word
	if "RT" in tweet:
		cleaned = re.sub(r'^RT\s@\S+\s', '', cleaned) #remove 'RT @sometwitterhandle: ' (i.e. RT format)

	#2: if @ not preceeded by RT, remove @ and split word into 2 parts based on capitalization
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

def find_start_time(full_tweets, award_name):
  target_words = ['begins', 'begin', 'start', 'opening']
  all_times = []
  for tweet in full_tweets:
    tweet_text = tweet['text']
    cleaned_tweet = clean_tweet(tweet_text)
    if award_name in cleaned_tweet:
      check = False
      for word in cleaned_tweet:
        if word in target_words:
          check = True
          break

    if check:
      all_times.append(tweet['timestamp_ms'])

  avg_time = reduce(lambda x, y: x+y, all_times)/ len(all_times)
  return convert_time(ms)


def convert_time(ms):
  base_datetime = datetime.datetime( 1970, 1, 1 )
  delta = datetime.timedelta( 0, 0, 0, ms )
  return base_datetime + delta

if __name__ == "__main__":
  tweets = load_data()
  time = find_start_time(tweets, "golden globes")
  print (time)
