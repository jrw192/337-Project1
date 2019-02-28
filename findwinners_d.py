import nltk
import string
import re
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords



#imports from other files
from filter_tweets import *

tt = TweetTokenizer()



def findwinner(awards_list, tweet_list):
	wins={}
	tweet_list_text = [tweet['text'] for tweet in tweet_list]

	# for each category
	for i in awards_list:
		# set strings to award name
		# original_award_name = i
		# if "–" in i:
		# 	gemp= i.replace("– ", "")
		# 	award_name=gemp
		# else:
		# 	award_name=original_award_name

		# tokens=[] 
		# splits=[]
		# splits2=[]
		# splits3=[]

		# print ("award name: " + award_name)
		# # clean award name formatting
		# # award_name = 
		# splits=award_name.split()
		# for word in splits:
		#  	splits2.append(word.lower())
		# splits3=" ".join(splits2)

		# # filter tweets for relevant tweet
		# for token in tweet_list:
		# 	# first check if award name in tweet
		# 	if (award_name in " ".join(token)):
		# 		# set each word to lowercase
		# 		for j in token:
		# 			j=j.lower()
		# 		print ("tweet: " + token)
		# 		# check if "goes" "to" "wins" or "won" is in it and add tweet to tokens list
		# 		if "goes" in token and "to" in token and len(token)>2:
		# 			tokens.append(token)				
		# 		elif not tokens:
		# 			for j in token:
		# 				if j.lower() == "wins" or j.lower() == "won":
		# 					tokens.append(token)
		# 	elif (splits3 in " ".join(token)):
		# 		for j in token:
		# 			j=j.lower()
		# 		if "goes" in token and "to" in token and len(token)>2:
		# 			tokens.append(j)		
		# 		elif not tokens:
		# 			for j in token:
		# 				if j.lower() == "wins" or j.lower() == "won":
		# 					tokens.append(j)
		# 		elif "tv" in splits3:
		# 			if "goes" in token and "to" in token and len(token)>2:
		# 				for j in token:
		# 					if "tv" == j or "television" ==j:
		# 						tokens.append(token)
				#textss=textss.append(token)

		# print (tweet_list_text)
		tweets = find_tweets_of_award(tweet_list_text, i)

		wins[i]=goesto(tweets)
			#uncomment below to see for other functions, 
			# "Nominees" : find_nominees(ptextss)
			# "Presenters":associate_presenters_awards(ptextss)
			# "Hosts": find_hosts(ptextss)
		
	return wins



# texts - tweet list
# category - award names
def goesto(texts): # category never used
	winn=[]
	winn_bigrams=[]
	index3=0
	index4=0

	stop_wordss=list(string.punctuation) + [" , ", "..." ,"…", "for", "RT", "go", "way", "SURPRISE", 'NOT',"A", "FUCK"]+list(stopwords.words("english"))
	# news=["BBC","FOX","ABC"]
	news=[]

	for text in texts:
		text = tt.tokenize(text)
		for low in text:
			low=low.lower()
		
		if "goes" in text and "to" in text:
			index3=text.index("goes")
			if text[index3+1] == "to" and text[index3+2] not in stop_wordss:
				index4 = text.index("to")

				for i in text[(index4+1):]:
					if "#"  in i or "http" in i or i in stop_wordss:
						pass
					elif "@" in i:
						if "_" in i:
							pass
						# else:
						# 	for j in news:
						# 		if j.upper() in i.upper():
						# 			pass
						# 		else:
						# 			winn.append(i)
					else:
						winn.append(i)
						first_index = text.index(i) + 1
						if first_index == len(text):
							continue
						winn_bigrams.append(i + " " + text[first_index])
		else:
			if "wins" in text:
				index3=text.index("wins")
				for i in text[:(index3)]:
					if "#"  in i or "http" in i or i in stop_wordss:
						pass
					elif "@" in i:
						if "_" in i:
							pass
						# else:
						# 	for j in news:
						# 		if j.upper() in i.upper():
						# 			pass
						# 		else:
						# 			winn.append(i)
					else:
						winn.append(i)
						first_index = text.index(i) + 1
						if first_index == len(text):
							continue
						winn_bigrams.append(i + " " + text[first_index])
			if "won" in text:
				index3=text.index("won")
				for i in text[:(index3)]:
					if "#"  in i  or"http" in i or i in stop_wordss:
						pass
					elif "@" in i:
						if "_" in i:
							pass
						# else:
						# 	for j in news:
						# 		if j.upper() in i.upper():
						# 			pass
						# 		else:
						# 			winn.append(i)
					else:
						winn.append(i)
						first_index = text.index(i) + 1
						if first_index == len(text):
							continue
						winn_bigrams.append(i + " " + text[first_index])

	winnerss={}
	winn_bigramss={}
	if not winn:
		return "Winner not found"
	for i in winn:
		if i in winnerss:
			winnerss[i]+=1
		else:
			winnerss[i]=0

	maximum= max(winnerss.values())
	winner_names = (" ".join([k for k, v in winnerss.items() if v == maximum])).replace("@","")

	##########
	### Bigram stuff. Comment out if too slow ###
	if winn_bigrams:

		count = 0
		only_one = True
		max_word = ""
		for i in winnerss:
			if winnerss[i] == maximum:
				count = count + 1
				max_word = i
			if count > 1:
				only_one = False
				break

		if only_one:
			for i in winn_bigrams:
				if i in winn_bigramss:
					winn_bigramss[i]+=1
				else:
					winn_bigramss[i]=0
			# print(winn_bigramss)

			# get 2nd most popular word
			del winnerss[max_word]

			# maximum now 2nd most popular word
			maximum= max(winnerss.values())

			maximum_bigram = max(winn_bigramss.values())

			count = 0
			only_one = True
			for i in winn_bigramss:
				if winn_bigramss[i] == maximum_bigram:
					count = count + 1
					max_word = i
				if count > 1:
					only_one = False
					break

			if only_one:
				if maximum_bigram == maximum:
					# print(max_word)
					return max_word

	### Bigram stuff
	##########
	
	return winner_names


def find_tweets_of_award(tweet_list, award):
	stop_words = list(stopwords.words("english"))+ ['performance',] #'golden', 'globes', 'best', 'wow', 'excellent', 'great', 'whoo', 'yay', 'winner', 'actor', 'actress' ]

	award_stripped = award
	for word in stop_words:
		award_stripped = award_stripped.replace(" " + word + " ", ' ')
	award_no_punct = re.sub(r'[^\w\s]', '', award_stripped)

	award_tokenized = tt.tokenize(award_no_punct)
	tweets = tweet_list
	for token in award_tokenized:
		filtered = filter_tweets_text(tweets, token, caseSensitive=False)
		if len(filtered) > 0:
			tweets = filtered

	return tweets
