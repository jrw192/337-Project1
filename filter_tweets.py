
import re
import sys
import json


def load_data():
    tweets = []
    with open('data/gg2013.json') as f:
        tweets = json.load(f)
    f.close()
    return tweets



def filter_tweets(tweets, param, caseSensitive=True):
    #if tweet's text contains the regex expression, add it to the match list
    matches =[]
    for tweet in tweets:
        text = tweet['text']
        if(caseSensitive):
            found =  re.search(param, text)
        else:
            found = re.search(param, text, flags=re.IGNORECASE)

        if(found):
                 matches.append(tweet)

    return matches


def main():
    tweets = load_data()
    nameMatches = filter_tweets(tweets, 'ARGO', False);
    print(nameMatches)
    #titleMatches = filter_tweets(nameMatches, 'presenter')
    #print(titleMatches)


if __name__ == "__main__":
    main()