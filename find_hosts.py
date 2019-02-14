#imports from other files
from filter_tweets import filter_tweets
from find_names import find_all_names

def find_hosts(tweets):

	# get matches w host in tweet
	matches = filter_tweets(tweets, 'host', False)

	tallyDict = {} # {'ben affleck': 1, 'john jones': 2, etc.}
	hostList = []

	# find names
	for match in matches:
		listOfNames = find_all_names(match)
		
		if len(listOfNames) = 1:

			#add to hostList if not there
			if listOfNames[0] not in hostList:
				hostList.append(listOfNames[0])

			#add to tallyDict if not there and increment count
			if name in tallyDict:
				tallyDict[name] = tallyDict[name] + 1 #increment count
			else:
				tallyDict[name] = 1 #add new key and value to dictionary

		if len(listOfNames) > 1:
			for host in hostList:
				count = len(i) for i in listOfNames
				count += 5 #account for " and "
				if count != len(host) #means they are not the same
				
				for name in listOfNames: #likely 2 or 3
					if name in host:
						continue
				#host entry contains names of both hosts



	# pick top 2