import nltk
from nltk.tokenize import TweetTokenizer
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.util import bigrams
from filter_tweets import main

#test some tokenization with different nltk methods
def tokenize_text(text):
	tokens = nltk.word_tokenize(text)
	return [tokens];
	

if __name__ == "__main__":
	argo = main()[0]["text"]
	print(argo)
	tokens = tokenize_text(argo)
	tt = TweetTokenizer()
	ttokens = tt.tokenize(argo)
	btokens = list(bigrams(tokens))
	print(tokens)
