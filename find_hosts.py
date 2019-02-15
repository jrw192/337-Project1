# -*- coding: UTF-8 -*-
#imports from other files
from filter_tweets import filter_tweets_temp
from find_names import find_all_names

def find_host(tweets):

	# get matches w host in tweet
	matches = filter_tweets_temp(tweets, 'host', False)

	tallyDict = {} # {'ben affleck': 1, 'john jones': 2, etc.}
	hostList = [] # ['ben affleck', 'john jones'] --> used to identify keys for dictionary

	# find names
	for match in matches:
		listOfNames = find_all_names(match)

		if len(listOfNames) == 0:
			continue
		
		elif len(listOfNames) == 1:

			#add to hostList if not there
			if listOfNames[0] not in hostList:
				hostList.append(listOfNames[0])

			#add to tallyDict if not there and increment count
			if listOfNames[0] in tallyDict:
				tallyDict[listOfNames[0]] += 1 #increment count
			else:
				tallyDict[listOfNames[0]] = 1 #add new key and value to dictionary

		elif len(listOfNames) > 1:
			found = False
			for host in hostList:
				count = sum(len(i) for i in listOfNames) #length of names
				count += 5 #account for " and "
				if count != len(host): #means they are not the same
					continue

				same = True
				# if reach here, then potential same: check actual names
				for name in listOfNames: #likely 2 or 3
					if name in host:
						continue
					else:
						same = False
						break

				if same:
					tallyDict[host] += 1
					found = True
					break
					##need to exit loop if already found a match
				else:
					continue

			# if we reach here, then it doesn't exist in hostList
			if not found:
				temp = listOfNames[0] + ' and ' + listOfNames[1]
				hostList.append(temp)
				tallyDict[temp] = 1

		else:
			print(error)
			return None

	val = max(tallyDict, key=tallyDict.get)
	print(tallyDict)
	print(val)
	return val


if __name__ == "__main__":
	#140 tweets
	text = ["RT @goldenglobes: It's our hosts Tina Fey and Amy Poehler! #goldenglobes #redcarpet http://t.co/8lqC3ocQ", "RT @washingtonpost: Tonight's dual hosting duties represent the culmination of a decade of Amy and Tina partnerships. http://t.co/scSThrn5 #GoldenGlobes", "RT @MovieMayor: My green suede tuxedo pinching a bit here at the Velvet Rope Awards honoring best in crowd control. Topo Gigio + I hosting #GoldenGlobes", "RT @accesshollywood: Tina Fey &amp; Amy Poehler Talk #GoldenGlobes Hosting, Drinking Game  http://t.co/1mIvq362", "@goldenglobes Best choice for host ever.  Nice job GG people.", "We’re going to keep things loose, said Amy Poehler of her and co-host Tina Fey’s plan for the evening. #GoldenGlobes http://t.co/o40g5LGq", "RT @usweekly: #GoldenGlobes hosts Tina Fey, Amy Poehler show off matching husband and wife outfits on red carpet http://t.co/XF3CjRj2", "RT @usweekly: #GoldenGlobes hosts Tina Fey, Amy Poehler show off matching husband and wife outfits on red carpet http://t.co/XF3CjRj2", "RT @washingtonpost: Tonight's dual hosting duties represent the culmination of a decade of Amy and Tina partnerships. http://t.co/scSThrn5 #GoldenGlobes", "RT @afp: #PHOTO: Hosts Tina Fey and Amy Poehler arrive at the #GoldenGlobes ceremony, by Frederic J. Brown http://t.co/1iBh08Tm", "If the Red Carpet hosts asked one more woman what they're wearing i'm going to lose my mind #goldenglobes", "RT @washingtonpost: Tonight's dual hosting duties represent the culmination of a decade of Amy and Tina partnerships. http://t.co/scSThrn5 #GoldenGlobes", "RT @goldenglobes: It's our hosts Tina Fey and Amy Poehler! #goldenglobes #redcarpet http://t.co/8lqC3ocQ", "RT @AFP: #PHOTO: Hosts Tina Fey and Amy Poehler arrive at the #GoldenGlobes ceremony, by Frederic J. Brown http://t.co/2GGtAKBD", "RT @usweekly: #GoldenGlobes hosts Tina Fey, Amy Poehler show off matching husband and wife outfits on red carpet http://t.co/XF3CjRj2", "RT @hall_mk: Like... Who cares about the relative viscosity of substances when Tina Fey and Amy Poehler are hosting the Golden Globes", "RT @RolondaWatts: Listen to The Golden Globes and Red Carpet Fashion hosted by Rolonda Watts on  #BlogTalkRadio  Designer Dalia MacPhee http://t.co/be7Bsiw1", "Excited for the #GoldenGlobes  Thinking Tina and Amy hosting should make for a fun evening!", "Oh no, Jay Leno has just stolen hosting duties from Amy Poehler and Tina Fey. #GoldenGlobes", "The only reason I'm going to watch #GoldenGlobes tonight is to see Tina and Amy host. Love those ladies!", "RT @nbc: Pop the champagne! Tina Fey and Amy Poehler host the #GoldenGlobes TONIGHT at 7ET/4PT!", "The fact that Tina Fey and Amy Poehler are hosting the #GoldenGlobes &gt;&gt;&gt; #myfavoritewomen", "Watching e's red carpet and with my eyes closed Kelly's cohost does not look how he sounds #goldenglobes", "Tina Fey and Amy Poehler hosting #GoldenGlobes is a must see. http://t.co/qcTFVEMk #GetGlue @goldenglobes", "Looking forward to Tina Fey and Amy Poehler's hosting of the #GoldenGlobes", "RT @womensmediacntr: Tonight's 70th @GoldenGlobes are the first ones hosted by a woman or women alone. And Tina &amp; Amy are going to ROCK it. http://t.co/aAYQ5mIh", "That black streak in Jay Leno's hair is from the one time he saw the ghost dick under his belly, right? #GoldenGlobes", "take mc today &gt;&gt;&gt;&gt;&gt; get to roll in bed with tina fey and amy poehler hosting golden globes. SO WORTH IT", "Tina Fey and Amy Poehler are hosting the Golden Globes? Yes. ", "Super excited for Tina Fey and Amy Pohler to host the #goldenglobes !!", "The fact that Tina Fey AND Amy Poehler are teaming up as host for The Golden Globes tonight&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;", "2013 Golden Globes live: Tina Fey and Amy Poehler host Hollywood elite http://t.co/nJaXxLzu", "RT @nbc30rock: Host AND nominee?! We can’t wait to see Tina Fey at the #GoldenGlobes tonight! Join @NBC as we live tweet the entire event.", "t-5 min until @hurricanejac and I make our hosting debut for the Golden Globes", "Tina Fey + Amy Poehler hosting the Golden Globes. You've got my attention. (@ Ingersoll Square Lofts) http://t.co/8ny8AR4h", "#SGS 2013 Golden Globes live: Tina Fey and Amy Poehler host Hollywood elite: Hollywood Foreign Press Association... http://t.co/mpEpxe8x", "2013 Golden Globes live: Tina Fey and Amy Poehler host Hollywood elite: Hollywood Foreign Press Association have... http://t.co/45qWL5Fd", "2013 Golden Globes live: Tina Fey and Amy Poehler host Hollywood elite: Hollywood Foreign Press Association have... http://t.co/TyHqmGK7", "The Golden Globes Red Carpet countdown is hosts by the anchors for the Today Show. So cost cutting? Ryan Seacrest have too much swag now?", "RT @StayPuft: In 1985, Ghostbusters was nominated for three Golden Globes. We won none. Unforgivable.", "Excited to watch Amy and Tina host tonight #GoldenGlobes", "RT @LyricalAlchemy: So excited that the two funniest women on the planet are hosting the #goldenglobes!!! #tinafey #amypoehler 🎥", "Watching the #GoldenGlobes for the simple fact that Amy Poehler is hosting. #topnotchcomedy", "@robsalem So who's looking forward to Amy Poehler and Tina Fey as hosts? #GoldenGlobes", "Moved my desktop computer into the only room with cable in the building so I can live blog my two ladies hosting the Golden Globes.", "so excited for tina &amp; amy! the oscars are my main jam, but this hosting duo has me very hopeful!!  #goldenglobes", "@SPANXinc they could be one of the best hostesses ever #SpanxRedCarpet #GoldenGlobes", "#goldenglobes looking forward to Tina and Amy hosting!! 😂😆", "What an awesome weekend of #NFLPlayoffs!!  Now time to watch my heroes, #TinaFey and #AmyPoehler host the #GoldenGlobes!!", "RT @TVMcGee: Let's hope the #GoldenGlobes don't bury Tina/Amy tonight. They have two brilliant comedians/writers/actresses hosting. USE THEM.", "RT @thetimes: Tonight's Golden Globes will be hosted Tina Fey and Amy Poehler. Full nominations here: http://t.co/xEjTpufI http://t.co/NQy5itil", "Tune in: Live Chat: Golden Globes 2013: From the red carpet to the hosts to the show - http://t.co/5LG1H9Bo http://t.co/qto6gQqV", "i am just too excited for this. if there are two women who should be hosting the golden globes, it's tiny fey and amy poehler #gonnabegood", "RT @eonline: OM #GoldenGlobes watch the #FashionSquad host a trunk show from the back of a @VW Jetta in this fab YouTube VIDEO: http://t.co/AmcL9ul0", "My #GoldenGlobes predictions: People will agree or disagree with the choices. The hosts will be above or below expectations.", "RT @TheAwesomeator: Tina Fey &amp; Amy Poehler are hosting the #GoldenGlobes tonight and are going to destroy.", "The #GoldenGlobes are starting! Who do you think will give the audience more chuckles as a host: #AmyPoehler or #TinaFey? Let us know!", "Super-excited for @NotTinaFey and Amy Poehler hosting the #goldenglobes!!", "Actually excited for the Golden Globes this year because Tine Fey and Amy Poehler are hosting. :D I love them. #SecondCity", "tina fey and amy pohler are hosting the golden globes?! MY ENTERTAINMENT FOR THE NIGHT", "Only my two heroes hosting the Golden Globes at the same time right now, whatever.", "Got my wine, so I'm settled in to watch Tina Fey and Amy Poehler host the #GoldenGlobes", "I actually do give a shit about the golden globes this year only because of the hosts.", "No puede haber mejor host para los golden globes que tina fey!", "So excited to see Amy Poehler host the Golden Globes tonight", "Golden Globes hosted by my comedic idols", "So excited for @amypoehler and @NotTinaFey to host the Golden Globes!!! Best. Duo. Ever. #GoldenGlobes", "#TheHeat worships funny women, so we can't wait to see Amy Poehler and Tina Fey host the #GoldenGlobes. Kill it, ladies! #amyandtinarock!", "So happy that Tina &amp; Amy are hosting! #GoldenGlobes", "RT @MojaveFoneBooth: I enjoyed Giuliana Rancic's work better when she hosted Tales from the Crypt. #GoldenGlobes", "Whats going on? I thought honey booboo was hosting. ( warm up joke. Doesnt count. Its like shadow boxing). #GoldenGlobes", "About to watch these Golden Globes&gt;&gt;&gt; Just for the hosts:D", "It's on! #GoldenGlobes time! Can't wait to see hosts Tina Fey and Amy Poehler kill it.", "Golden Globes are starting. Best hosts possible. #ilovetinafey #iloveamypoehler", "Hosts Tina Fey &amp; Amy Poehler take the stage. 70th annual #GoldenGlobes starting now! http://t.co/7vmcmUOO", "There was honestly no better decision made than choosing these two to host. #GoldenGlobes", "Is Glenn Close's hair made of ghosts? #GoldenGlobes", "HOLY HOST HOTNESS #GoldenGlobes", "Amy Poehler and Tina Fey hosting the #GoldenGlobes! perfection!", "Me encantan las hosts de los #GoldenGlobes Tina Fey y Amy Polher", "Best hosts ever! #GoldenGlobes", "RT @jaqico: Only my two heroes hosting the Golden Globes at the same time right now, whatever.", "This is gonna be a funny golden globes with these two hosts", "Watching the Golden Globes because Tina Fey and Amy Poehler are hosting.", "Tina and Amy co-hosting is a glimpse into what my personal heaven will be like. #GoldenGlobes", "I am so excited for them to host :3 #GoldenGlobes", "RT @DavidSpade: Whats going on? I thought honey booboo was hosting. ( warm up joke. Doesnt count. Its like shadow boxing). #GoldenGlobes", "Tina &amp; Amy hosting the golden globes is going to be hilarious 😢", "OMG Miss Norberry is hosting The Golden Globes! That is so fetch!", "No pudieron escoger a mejores hosts que Tina y Amy. Son unos genios los de los Golden Globes.", "Tina Fey and Amy Poehler hosting the Golden Globes is genius.", "Love how the hosts are talking and you hear the TV crew counting them out. #GoldenGlobes", "The #GoldenGlobes hasn't even started yet and I'm already wishing @toddbarry was hosting, not these #lesbians", "Love Tina Fey's dress! &amp; I love that her &amp; Amy Poehler are hosting. #goldenglobes", "Love NBC for picking these wonderful people to host. #GoldenGlobes", "#goldenglobes liking the dresses of the hosts!", "Love that Tina and Amy are hosting #GoldenGlobes #amazing", "Tina Fey &amp; Amy Poehler host the 70th Annual #GoldenGlobes! Starting now! Tweet us your favorite moments of the show!", "Why are the Little Mermaid and Princess Jasmine hosting the Golden Globes?", "So happy Tina Fey and Amy Poehler are hosting the Golden Globes! Love them", "RT @aldoughty: #ACC Represent at the #GoldenGlobes with Tina Fey @UVA grad and Amy Poehler - @BostonCollege grad co-hosting", "Sickest fucking host duo #comedicgold #goldenglobes", "My two girl crushes hosting! http://t.co/VEFMFfnT #GetGlue @goldenglobes", "Tina Fey's hosting? Sweet! #goldenglobes #whynot", "RT @DavidSpade: Whats going on? I thought honey booboo was hosting. ( warm up joke. Doesnt count. Its like shadow boxing). #GoldenGlobes", "OMG Tina &amp; Amy are absolutely stunning hosts!!! #GoldenGlobes", "Tina &amp; Amy hosting. The actors better watch out for the jokes :D #GoldenGlobes", "Love that two smart and funny women are hosting the #GoldenGlobes! Well done TV and film!!!", "Great 2 women are hosting the #GoldenGlobes *turns off TV*", "RT @DavidSpade: Whats going on? I thought honey booboo was hosting. ( warm up joke. Doesnt count. Its like shadow boxing). #GoldenGlobes", "2 hot chicas hosting the #goldenglobes. #girlpower!", "I know the #GoldenGlobes are going To be fantastic by the fact that Tina fey and Amy poehler are hosting 😂", "RT @DavidSpade: Whats going on? I thought honey booboo was hosting. ( warm up joke. Doesnt count. Its like shadow boxing). #GoldenGlobes", "RT @TIME: Hosts Tina Fey and Amy Poehler have graciously provided a Golden Globes drinking game. Bottoms up! | http://t.co/33nnrrsQ", "RT @mariskreizman: First and only Golden Globes where I don't care about reaction shots. Just keep showing me the hosts.", "Amy Poehler -- Parks &amp; RACK!: Park and Recreation funny lady Amy Poehler arrived to the Golden Globes with her two lovely hosting s...", "Super stoked for Tina Fey and Amy Poeler hosting the Golden Globes. Love them.", "Ahh, I love Tina Fey and Amy Poehler! They could not of chosen a better pair to host The Golden Globes", "Watching the Golden Globes hosted by Amy Pholer &amp; Tiny Fay", "Having Tina Fey and Amy Poehler host the golden globes has to be the greatest choice ever", "Tina fey and Amy poehler hosting the golden globes...ummm yes", "RT @MaddySchon19: Tina and Amy hostin golden globes ahhhhh let the humor begin", "RT @rubyjnkie: RT @TIME: Hosts Tina Fey and Amy Poehler have graciously provided a Golden Globes drinking game. Bottoms up! | http://t.co/UT5AUlJj", "omg tina fey and amy poehler hosting the golden globes &gt;&gt;&gt; #lovethem", "Lololol look who's hosting the golden globes @megan_lindley @robynanne24 HERE COMES YO BABY MOMMAAAA", "How come Tina Fey decided to look like a tranny hooker to host the golden globes?", "I love watching the Golden Globes especially cause Tina and Amy are hosting omg", "Ready for Tina and Amy to be hilarious hosts at the Golden Globes. its gunna be great", "Was gonna watch The Golden Globes until I realized Tina Fey &amp; Any Poehler are hosting. They are NOT funny.", "Tina Fey and Amy Poehler hosting the Golden Globes #gold", "I love how they have the two funniest women in the world hosting the Golden Globes #smart", "THE ONLY THING THAT MATTERS RIGHT NOW IS THAT TINA FEY AND AMY POEHLER ARE HOSTING THE GOLDEN GLOBES!!! #GoldenGlobes", "Tina and Amy are host perfection :) #GoldenGlobes", "RT @DavidSpade: Whats going on? I thought honey booboo was hosting. ( warm up joke. Doesnt count. Its like shadow boxing). #GoldenGlobes", "Jamas me ah gustado tina fey!, como la ponen de host? WTF #GoldenGlobes", "Bill Murray is looking OOOOLD.  They better hurry and make that Ghostbusters movie before they have to cast him as a ghost #GoldenGlobes", "So stoked Tina and Amy are hosting the #goldenglobes", "I am so excited my heroes Tina Fey &amp; Amy Poehler are hosting the Golden Globes tonight. I truly adore them.", "@Bama_Bitches our girls are hosting the golden globes!"]

	find_host(text)








