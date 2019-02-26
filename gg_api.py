'''Version 0.35'''

import string
import json

#imports from other files
from filtercategories_d import filter_tweets
from loaddatscategories_d import load_data
from findwinners_d import findwinner
from findawardcategories_d import mains
from find_categories import categoriess
from load_data import load_data
from find_presenters import find_all_presenters
from find_hosts import find_host
from find_award_time import find_start_time
from filter_tweets import filter_tweets_by_time
from find_nominees import find_all_nominees
from find_best_dressed import find_best_worst_dressed



OFFICIAL_AWARDS_1315 = ['cecil b. demille award', 'best motion picture - drama', 'best performance by an actress in a motion picture - drama', 'best performance by an actor in a motion picture - drama', 'best motion picture - comedy or musical', 'best performance by an actress in a motion picture - comedy or musical', 'best performance by an actor in a motion picture - comedy or musical', 'best animated feature film', 'best foreign language film', 'best performance by an actress in a supporting role in a motion picture', 'best performance by an actor in a supporting role in a motion picture', 'best director - motion picture', 'best screenplay - motion picture', 'best original score - motion picture', 'best original song - motion picture', 'best television series - drama', 'best performance by an actress in a television series - drama', 'best performance by an actor in a television series - drama', 'best television series - comedy or musical', 'best performance by an actress in a television series - comedy or musical', 'best performance by an actor in a television series - comedy or musical', 'best mini-series or motion picture made for television', 'best performance by an actress in a mini-series or motion picture made for television', 'best performance by an actor in a mini-series or motion picture made for television', 'best performance by an actress in a supporting role in a series, mini-series or motion picture made for television', 'best performance by an actor in a supporting role in a series, mini-series or motion picture made for television']
OFFICIAL_AWARDS_1819 = ['best motion picture - drama', 'best motion picture - musical or comedy', 'best performance by an actress in a motion picture - drama', 'best performance by an actor in a motion picture - drama', 'best performance by an actress in a motion picture - musical or comedy', 'best performance by an actor in a motion picture - musical or comedy', 'best performance by an actress in a supporting role in any motion picture', 'best performance by an actor in a supporting role in any motion picture', 'best director - motion picture', 'best screenplay - motion picture', 'best motion picture - animated', 'best motion picture - foreign language', 'best original score - motion picture', 'best original song - motion picture', 'best television series - drama', 'best television series - musical or comedy', 'best television limited series or motion picture made for television', 'best performance by an actress in a limited series or a motion picture made for television', 'best performance by an actor in a limited series or a motion picture made for television', 'best performance by an actress in a television series - drama', 'best performance by an actor in a television series - drama', 'best performance by an actress in a television series - musical or comedy', 'best performance by an actor in a television series - musical or comedy', 'best performance by an actress in a supporting role in a series, limited series or motion picture made for television', 'best performance by an actor in a supporting role in a series, limited series or motion picture made for television', 'cecil b. demille award']

# if we can change parameters, delete this; otherwise, let's find a better option

# awards = {}
# nominees = {}
# winners = {}
# presenters = {}
# hosts = ""

def get_hosts(year):
	'''Hosts is a list of one or more strings. Do NOT change the name
	of this function or what it returns.'''
	# Your code here

	tweets = load_data(year)
	hosts = find_host(tweets)
	return hosts

def get_awards(year):
	'''Awards is a list of strings. Do NOT change the name
	of this function or what it returns.'''
	# Your code here
	tweets = load_data(year)
	awards=categoriess(year)
	return awards

def get_nominees(year):
  '''Nominees is a dictionary with the hard coded award
  names as keys, and each entry a list of strings. Do NOT change
  the name of this function or what it returns.'''
  awards = get_awards(year)
  tweets = load_data(year)
  nominees = find_all_nominees(tweets, awards)
  return nominees

def get_winner(year):
	'''Winners is a dictionary with the hard coded award
	names as keys, and each entry containing a single string.
	Do NOT change the name of this function or what it returns.'''
	# Your code here
	tweets = load_data(year)
	winners=mains(year)
	return winners

def get_presenters(year):
  '''Presenters is a dictionary with the hard coded award
  names as keys, and each entry a list of strings. Do NOT change the
  name of this function or what it returns.'''
  # Your code here
  awards = get_awards(year)
  tweets = load_data(year)
  presenters = find_all_presenters(tweets, awards, awards)
  return presenters

def pre_ceremony():
	'''This function loads/fetches/processes any data your program
	will use, and stores that data in your DB or in a json, csv, or
	plain text file. It is the first thing the TA will run when grading.
	Do NOT change the name of this function or what it returns.'''
	# Your code here
	print("Pre-ceremony processing complete.")
	return


def main():
  '''This function calls your program. Typing "python gg_api.py"
	will run this function. Or, in the interpreter, import gg_api
	and then run gg_api.main(). This is the second thing the TA will
	run when grading. Do NOT change the name of this function or
	what it returns.'''
  year = input("Enter the year, then press enter:\n")
  print("processing data.......give us a few minutes........")
  tweets = load_data(year)
  hosts = get_hosts(year)
  print("host finding completed.")

  awards = get_awards(year)
  print("award finding completed.")
  winners = get_winner(year)	
  all_winners = []
  for key in list(winners.keys()):
    # print(key)
    # print(winners[key])
    all_winners.append(winners[key])

  print("winner finding completed.")
  presenters = get_presenters(year)
  print("presenter finding completed.")
  nominees = get_nominees(year)
  print("nominee finding completed.")
  dressed = find_best_worst_dressed(tweets)
  print("best dressed finding completed.")
  print("\n")
  running= True
  
  # data formatting
  results = {}
  results['Host(s)'] = hosts
  
  for award in awards:
    award_winner = winners[award]
    award_presenter = presenters[award]
    award_nominees = nominees[award]
    award_dict = {}
    award_dict['Winner'] = award_winner
    award_dict['Presenter(s)'] = award_presenter
    award_dict['Nominees'] = award_nominees
    results[award] = award_dict
  
  print("Saving results to results.json file")
  file = open("results.json", "w")
  file.write(json.dumps(results))
  file.close() 

  results = json.dumps(results)

  while running:
    task = input("Enter task: 'hosts', 'awards', 'winners', 'presenters', 'nominees', or 'dressed', or 'all' to see the full list. Type 'end' to end.\n")
    if task == 'hosts':
      print("host(s): %s" % hosts)
      print("\n")

    elif task == 'awards':
      print("the awards are: ")
      for award in awards:
        print(award)
      print("\n")

    elif task == 'winners':
      for award in winners:
        print("winner for %s : %s" % (award, winners[award]))
      print("\n")

    elif task == 'presenters':
      for award in presenters:
        print("presenters for %s are: " % award)
        for person in presenters[award]:
          if person == " ":
            print("Not Found")
          print(person)
        print("\n")
      print("\n")

    elif task == 'nominees':
      for award in nominees:
        print("nominees for %s are: " % award)
        for person in nominees[award]:
          print("\t" + person)

    elif task == 'dressed':
      print("best dressed : ")
      for person in dressed[0]:
        print(person)
      print("\n")
      print("worst dressed : ")
      for person in dressed[1]:
        print(person)
      print("\n")

    elif task == 'all':
      print(results)

    elif task == 'end':
      break

  return results

# helper functions
def get_human_readable_format(results_dict, award_dict, dressed_dict):
	category_types = ["presenters", "nominees", "winners"]
	extra_categories = ["best", "worst"]

	string_formatted = text_formatter_helper("hosts", results_dict['hosts']) + "\n"

	for award in award_dict:
		string_formatted += text_formatter_helper("award", award)

		for category in category_types:
			string_formatted += text_formatter_helper(category, results_dict[award][category])
		string_formatted += "\n"
	for x in range(len(extra_categories)):
		string_formatted += text_formatter_helper(extra_categories[x] + " Dressed", dressed_dict[x])

	return string_formatted

def text_formatter_helper(cat_type, data):
	out_string = cat_type.capitalize() + ": "
	if isinstance(data, str):
		out_string += data + "\n"
	elif isinstance(data, list):
		for elem in data:
			out_string += elem + ", "
		out_string = out_string[:-2] + "\n" # remove comma space from last element
	return out_string


if __name__ == '__main__':
	main()