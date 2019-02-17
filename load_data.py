import json
import sys
def load_data(filename='data/gg2013.json'):
	tweets = []
	with open(filename) as f:
		tweets = json.load(f)
	f.close()
	return tweets

if __name__ == "__main__":
	load_data('data/gg2013.json')