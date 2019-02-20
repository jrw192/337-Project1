import json
import sys
import os

def load_data(year):
	tweets = []
	filename = ""
	files = os.listdir('data')
	# print(files)
	for file in files:
		if year in file:
			filename = 'data/' + file
			break

	with open(filename) as f:
		tweets = json.load(f)
	f.close()
	return tweets

if __name__ == "__main__":
	load_data('2015')