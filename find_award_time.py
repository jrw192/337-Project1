# -*- coding: UTF-8 -*-
import datetime
import re
from load_data import load_data
import nltk
from nltk.tokenize import TweetTokenizer
import time

from filter_tweets import filter_tweets_by_time

tt = TweetTokenizer()

### rid tweet of hashtags, links, punctuations
# @param: tweet - string
# @return: string
###
def clean_tweet(tweet):
	cleaned = re.sub(r'[#@][\w]+', '',tweet) #remove all hashtags 
	cleaned = re.sub(r'http://.+', '', cleaned) #remove all links
	cleaned = re.sub(r'[^\w\s]', '', cleaned) #remove all punctuation characters
	
	return cleaned


### find the start time given all tweet data and award name
# @param: full tweets - dictionary, award name - string
# @return: start_time - int (ms representation)
###
def find_start_time(full_tweets, award_name):
  target_words = ['starting', 'beginning', 'opening']
  all_times = []
  all_tweets = []
  for tweet in full_tweets:
    tweet_text = tweet['text']
    cleaned_tweet = clean_tweet(tweet_text)
    tokenized = tt.tokenize(cleaned_tweet)
    check = False

    # check for hashtagged version of award name
    alt_name = award_name.replace(' ', '').lower()

    # check if award name and one of target words are in tweet
    if award_name in cleaned_tweet or alt_name in cleaned_tweet:
      for word in tokenized:
        if word in target_words:
          check = True
          break

    if check:
      all_times.append(tweet['timestamp_ms'])
      all_tweets.append(tweet['text'])

  # sort and get rid of largest times (rewatching, late posts, etc)
  all_times.sort()
  try:
    all_times = all_times[:-4]
  except:
    all_times = all_times

  # average out the times
  avg_time = 0
  if len(all_times) > 0:
    sum = 0
    for time in all_times:
      sum += time
    avg_time = sum / len(all_times)

  # round to nearest hour
  # start_dt = datetime.datetime.fromtimestamp(avg_time/1000.0)
  # start_dt = round_to_nearest_hour(start_dt)

  # convert back
  # start_time = int(datetime.datetime.timestamp(start_dt))

  start_time = avg_time
  return start_time

### round time to nearest hour
# @param: time - datetime 
# @return: time - datetime
###
def round_to_nearest_hour(time):
  start_hour = time.replace(minute=0, second=0, microsecond=0)
  half_hour = time.replace(minute=30, second=0, microsecond=0)

  # round up
  if time >= half_hour:
      time = start_hour + datetime.timedelta(hours=1)
  # round down
  else:
      time = start_hour

  return time

if __name__ == "__main__":
  tweets = load_data()
  time = find_start_time(tweets, "golden globes")
  print(datetime.datetime.fromtimestamp(time/1000.0))
  rel_tweets = filter_tweets_by_time(tweets, time)
  for tweet in rel_tweets:
    print(datetime.datetime.fromtimestamp(tweet['timestamp_ms']/1000.0))
  # print (rel_tweets)
