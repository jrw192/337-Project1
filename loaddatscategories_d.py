import json
import sys
#load_data
def load_data(year):
    tweets = []
    with open('data/gg' + year + '.json') as f:
        tweets = json.load(f)
    f.close()
    
    if (len(tweets))>800000:
        #print(tweets[:180000])
        return (tweets[200000:800000])

    else:
        return tweets

if __name__ == "__main__":
    load_data()