import re
import sys
from load_data import load_data



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


def main():
    tweets = load_data()
    nameMatches = filter_tweets(tweets, 'mychael danna', False);
    #titleMatches = filter_tweets(nameMatches, 'presenter')
    #print(titleMatches)
    print(nameMatches)
    return nameMatches


if __name__ == "__main__":
    main()