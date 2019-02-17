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

###
# @param: list of strings, date
# @return: list of strings (maybe just text)
###
def filter_tweets_by_date(tweets, time):
    matches = []
    for tweet in tweets:
        time = tweet['timestamp']
        if int(time) < time:
            matches.append(tweet['text'])
    return matches


# Temporary to test find_hosts
def filter_tweets_temp(tweets, param, caseSensitive=True):
    #if tweet's text contains the regex expression, add the text of the tweet to the match list
    matches =[]
    for tweet in tweets:
        if(caseSensitive):
            found =  re.search(param, tweet)
        else:
            found = re.search(param, tweet, flags=re.IGNORECASE)

        if(found):
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
