import re
import sys
from load_data import load_data
# from langdetect import detect, DetectorFactory


###
# @param: list of strings
# @return: list of strings of just tweet text 
###
def filter_tweets(tweets, param, caseSensitive=True):
    #if tweet's text contains the regex expression, add the text of the tweet to the match list
    matches =[]
    for tweet in tweets:
        text = tweet['text']
        if(caseSensitive):
            found =  re.search(param, text)
        else:
            found = re.search(param, text, flags=re.IGNORECASE)

        if(found):
                 matches.append(tweet["text"])

    return matches

def filter_tweets_text(tweets, param, caseSensitive=True):
    matches =[]
    for text in tweets:
        if(caseSensitive):
            found =  re.search(param, text)
        else:
            found = re.search(param, text, flags=re.IGNORECASE)

        if(found):
                 matches.append(text)

    return matches


###
# @param: list of strings
# @return: list of strings of just tweet text 
###
def filter_tweets_remove(tweets, param, caseSensitive=True):
    #if tweet's text contains the regex expression, add the text of the tweet to the match list
    matches =[]
    for tweet in tweets:
        text = tweet['text']
        if(caseSensitive):
            found =  re.search(param, text)
        else:
            found = re.search(param, text, flags=re.IGNORECASE)

        if(not found):
                 matches.append(tweet["text"])

    return matches

def filter_tweets_strings_remove(tweets, param, caseSensitive=True):
    #if tweet's text contains the regex expression, add the text of the tweet to the match list
    matches =[]
    for tweet in tweets:
        if(caseSensitive):
            found =  re.search(param, tweet)
        else:
            found = re.search(param, tweet, flags=re.IGNORECASE)

        if(not found):
                 matches.append(tweet)

    return matches

###
# @param: tweets - list of dictionaries, time - int
# @return: list of strings
###
def filter_tweets_by_time(tweets, time):
    matches = []
    for tweet in tweets:
        tweet_time = tweet['timestamp_ms']
        if time > tweet_time:
            matches.append(tweet)
    return matches


## Takes too long to filter all tweets out
# def filter_tweets_by_language(tweets):
#     DetectorFactory.seed = 0 #enforce consistent results
#     # matches = []
#     # for tweet in tweets:
#     #     if(detect(tweet['text']) == 'en'):
#     #         matches.append(tweet["text"])

#     # return matches

#     count = {}
#     for tweet in tweets:
#         try:
#             tweet = detect(tweet['text'])
#         except:
#             continue

#     return Counter(count)


def main():
    tweets = load_data()
    nameMatches = filter_tweets(tweets, 'mychael danna', False);
    #titleMatches = filter_tweets(nameMatches, 'presenter')
    #print(titleMatches)
    print(nameMatches)
    return nameMatches


if __name__ == "__main__":
    main()
    # DetectorFactory.seed = 0
    # print(detect("fantastic http://t.co/TZ47heFF"))
    # print(detect("No pudieron escoger a mejores hosts que Tina y Amy. Son unos genios los de los Golden Globes."))
