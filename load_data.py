import json
import sys
def load_data():
    tweets = []
    with open('data/gg2013.json') as f:
        tweets = json.load(f)
    f.close()
    return tweets