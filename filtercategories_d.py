import re
import sys
from loaddatscategories_d import load_data


def filter_tweets(tweets, param, caseSensitive=True):
    matches =[]
    for tweet in tweets:
        text = tweet['text']
        matches.append(tweet["text"])

    return matches


def main():
    tweets = load_data(year)
    return nameMatches


if __name__ == "__main__":
    main()