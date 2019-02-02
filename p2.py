import re
import sys
import json

data = []

def load_data():
	global data
	f = open('data/gg2013.json', "r", encoding="utf8")
	data = f.readlines()
	f.close()
	train(data)
	


def train(lines):
	x=[]
	lines = json.dumps(lines)
	line= lines.split('text')
	#
	for i in line:
		line=json.dumps(i)
		line.split("\\\":")
		x.append(line)
	#print((x[2]))
	for i in x:
		rest= i.split(',')[0]
		print(rest)




if __name__ == "__main__":
	load_data()
	
