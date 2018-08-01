def forest_thieves():

	while True:
		
		print("You make chicken noises and dance around to get Stanley to follow you into the woods.")
        print("~")
        print ("She follows you, but her tummy continues to rumble. You don't have much time left before you become lunch.")
        sleep (2)
        print("~")
        print ("Suddenly, an arrow zips past your face and sinks into a tree trunk right in front of you.")
        print ("A voice calls out telling you to halt!")
        print("~")
        print ("Do you listen?")
        sleep (1)
        print ("Shield = Raise your hands and await further instructions. \
			Sword = point in the direction of the voice and hope Stanley takes her cue to attack the owner of the voice.")
        print("~")
        
        id, text = reader.read()
		
        sleep(2)  
                    
        if id == shield_id:
            print("You calm Stanley down, and yell to the unknown assailant that your going to cooperate.")
			print("An archer emerges from the bush in front of you, he intrduces himself as Robin Hood.")
			print("Robin Hood draws his sword, aims it toward you, and aks if you are a knight to the town king.")
			print("You quickly reply that you are simply a commoner, wandering the land seeking adventure and love.")
			print("Robin Hood inspects your gear, looks over to stanley, and back at you.")
			sleep(2)
			print("The sword is lowered".)
			print("Robin Hood explains that he recently stole gold coins from the local king.")
			print("He thought you might be a knight in desgise, but after looking at your gear and hearing your story")
			print("He believes you.")
			print("You calm down after being interrogated and check on Stanley.")
			print("You hear a mighty rumble, and remember that Stanley is hungry")
			print("~")
			print("Robin Hood presents you with some meat for Stanley, in exchange that you dont rat him out to the town")
			print("Scan Sword to remember that a very large reward is givin if you find Robin Hood, take the meat, and rat out Robin Hood")
			print("Or Money Pouch to gladly accept his gift, and promise to keep his secret")
			
			id, text = reader.read()
			sleep(2)
			
			if id == sword_id:
				print("You get back to town, and rat out the location of Robin Hood")
				print("Robin Hood is caught, little Jon finds you and eliminates you, maybe you should of kept Robin Hoods secret")
				menu()
			
			if id == pouch_id:
				print("As you walking away, Robin Hood yells, he asks if you would like to join his crew and help him on his adventure")
				print("Scan Horse to continue on with your adventure,and head to the town. Or Sword to join Robin Hood on his adventure")
			
                
        if id == sword_id:
            print("Stanley let out a massive roar and leapt onto the unkown assailant.")
			print("Scan Money Pouch to get up and inpsect the damage. Or Horse to get up and continue on your quest")
			
			id, text = reader.read()
			sleep(2)
			
			if id == pouch_id:
				print("You approach the downed enemy and find lots of gold coin, some food, a green hood, and a bow")
				print("You pause and think to yourself, did i just kill Robin Hood?")
				print("A noise in the bushes breaks your train of thought")
				print("You peak around the bush and find Little Jon, badly injured")
				print("Scan Horse to ignore Little Jon and move on with your quest. Or Shield to help Little Jon and talk to him.")
				
				id, text = reader.read()
				sleep(2)
				
				if id == horse_id:
					print("You ignore Little Jon and continue on you adventure")
					
				if id == shield_id:
					print("You quickly run to Little Jon")
					print("Hes hurt pretty bad but hell live")
					print("Little Jon sees that you didnt mean to hurt them and asks if you would join his crew in place of Robin Hood")
					print(Scan Horse to ignore Little Jons request and move on with yours. Or Shield to help Little Jon and join him on his quest")
			
			if id == horse_id:
				print("You calm down Stanley, raid the defeated enemys loot for food, and feed it to Stanley")
				print("You and Stanley continue on your quest")
				
				
			
			
			
			
	