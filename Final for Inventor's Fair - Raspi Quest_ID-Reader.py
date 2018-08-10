import RPi.GPIO as GPIO
import SimpleMFRC522
from time  import sleep

reader = SimpleMFRC522.SimpleMFRC522()
file = open("ID.txt", "a")

card_id = 438780305160
blue_id = 437200323334

horse_id = 855570181099
spell_id = 443253320523
shield_id = 30936460075
dragon_id = 512174058320
potion_id = 99857197872
sword_id = 237950397256
pouch_id = 375187958551
fire_id = 31775189883
frost_id = 168928865129
heart_id = 718953180122




def menu():
    while True:
        print("Welcome.")
        print("Jump on your horse to begin a quest!")
        print("Swipe the card to run diagnostics")
        id, text = reader.read()
        sleep (1)

        if id == card_id:
            test_env()
    
        if id == horse_id:
            quest()

def quest():
    while True:
            print("We went west!")
            print ("~")
            sleep(3)
            print("A dragon lands in the road before you. Fight the dragon? Choose your sword to fight the dragon. Choose your horse to avoid the fight.")
            id, text = reader.read()
            sleep(2)
            
            if id == horse_id:
                print("The dragon respects your choice. You and the dragon become friends.")
                print ("The dragon licks your face and hovers in the air above you.")
                print("~")
                sleep(3)
                dragon1()
                sleep(2)
                
            if id == sword_id: 
                print("A risky choice.")
                print ("Your horse trots to a safe distance. Good luck.")
                print("~")
                sleep(2)
                fight1()


def fight1():
    while True:
        print("Will you choose your book of spells to cast magic? Or will you draw your sword?")
        print("Choose wisely.")
        print("~")
        
        id, text = reader.read()
        sleep(2)
        
        if id == spell_id:
            
            print("Do you choose to cast fireball? Or cast a frost spell?")
            print("Choose the flames to cast a fire bolt. Choose the crystal to throw an ice bolt.")
            print("~")
              
            id, text = reader.read()
            sleep(2)
            
            if id == fire_id:
                print("You heave a fireball at the dragon. She opens her mouth and the fireball disappears into her toothy maw.")
                print("The dragon appears strengthened by the fiery snack.")
                sleep(3)
                print("Her mouth begins to open and your short life flashes before you.")
                print("You chose poorly.")
                print("...")
                sleep(3)
                print("~~The End~~")
                print("This game is a collaborative project developed in the Red Rocks Community College IDEA Lab.") 
                print("To find out more, and to keep adding to this story, drop in and write with us!")
                sleep(6)
                print("~~~~~")
                menu()
                
            
            if id == frost_id:
                print("Your ice bolt shoots toward the dragon! Your frost power is depleted.")
                print("One of the dragon's scales freezes and brakes off as she staggers back from the impact.")
                print("~")
                sleep(3)
                print("Do you continue to fight the dragon or run past her to continue your travels?")
                print("Choose your sword to continue the fight. Choose your horse to continue past the dragon.")
                    
                id, text = reader.read()
                sleep(2)
                
                if id == horse_id:
                    sleep(2)
                    town_menu()
                if id == sword_id:
                    print("Will you use your sword or cast a spell?")
                    print("(Fireball is the only spell you have left.)")
                    print ("~")
                    print("Choose the flames to cast fire. Or choose your sword.")
                    sleep(3)
                    print("~")
                    
                    id, text = reader.read()
                    sleep(2)
                    
                    if id == sword_id:
                        print("Your sword pierces the dragon through her weakened scales.")
                        print("The dragon roars, collapses, and dies.")
                        print("~")
                        sleep(3)
                        print("You make a fancy set of dragon-scale armor.")
                        sleep(3)
                        print("Your horse returns. You resume your quest.")
                        print("~")
                        town_menu()
                        
                    if id == fire_id:
                        print("You heave a fireball at the dragon. She opens her mouth and the fireball disappears into her toothy maw.")
                        print("The dragon appears strengthened by the fiery snack.")
                        sleep(3)
                        print("Her mouth begins to open and your short life flashes before you.")
                        print("You chose poorly.")
                        print("...")
                        sleep(3)
                        print("~~The End~~")
                        print("This game is a collaborative project developed in the Red Rocks Community College IDEA Lab.") 
                        print("To find out more, and to keep adding to this story, drop in and write with us!")
                        print("~~~~~")
                        sleep(6)
                        menu()
     
            
            
        
        if id == sword_id:
            print("You swing at the dragon. The dragon doesn't even try to move.")
            print("Your sword bounces off the dragon's scales and she rumbles at you in laughter.")
            print("~")
            sleep(3)
            print("Do you continue to fight the dragon?")
            print("~")
            print("Choose the book of spells to cast magic. Choose the sword to risk more laughter at your expense. Or choose the potion bottle to swallow an invisibility potion and sneak past the dragon.")
            
            id, text = reader.read()
            sleep(2)

            if id == sword_id:
                print("The dragon's laughter causes a rockslide that buries you. The end is nigh.")
                print("You chose poorly")
                print("~~The End~~")
                print("This game is a collaborative project developed in the Red Rocks Community College IDEA Lab.") 
                print("To find out more, and to keep adding to this story, drop in and write with us!")
                sleep(6)
                print("~~~~~")
                menu()
                
            if id == potion_id:
                print("You swallow the potion and your skin begins to tingle.")
                print("You are amazed as you watch your hand and then your arm disappear.")
                print("~")
                sleep(3)
                print("The dragon snorts in surprise as you poof into thin air. You hold your breath and tiptoe toward the dragon.")
                print("...")
                sleep(3)
                print("You made it past the dragon!")
                town_menu()
            
            if id == spell_id:
                print("Choose the flames to cast a fireball. Choose the crystal to cast a frost spell.")
                print("~")
                
                id, text = reader.read()
                sleep(2)
                
                if id == fire_id:
                    print("You heave a fireball at the dragon. She opens her mouth and the fireball disappears into her toothy maw.")
                    print("The dragon appears strengthened by the fiery snack.")
                    sleep(3)
                    print("Her mouth begins to open and your short life flashes before you.")
                    print("You chose poorly.")
                    print("...")
                    sleep(3)
                    print("~~The End~~")
                    print("This game is a collaborative project developed in the Red Rocks Community College IDEA Lab.") 
                    print("To find out more, and to keep adding to this story, drop in and write with us!")
                    print("~~~~~")
                    sleep(6)
                    menu()
                if id == frost_id:
                    print("Your ice bolt shoots toward the dragon! Your frost power is depleted.")
                    print("One of the dragon's scales freezes and brakes off as she staggers back from the impact.")
                    print("~")
                    sleep(3)
                    print("Do you continue to fight the dragon? Or run past her to continue your travels?")
                    print("~")
                    print("Choose your sword to continue the fight. Choose your horse to continue past the dragon.")
                    
                    id, text = reader.read()
                    sleep(2)
                    
                
                 
                    if id == horse_id:
                        print("...")
                        sleep(2)
                        print("You made it past the dragon!")
                        sleep(2)
                        town_menu()
                    
                    if id == sword_id:
                        print("Your sword pierces the dragon through her weakened scales.")
                        print("The dragon roars, collapses, and dies.")
                        sleep(3)
                        print("~")
                        print("You make a fancy set of dragon-scale armor.")
                        sleep(2)
                        print("Your horse returns. You resume your quest.")
                        print("~")
                        town_menu()
                
        
                

def town_menu():
    while True:
        print("The roadway is soon filled with travelers heading to the market in town.")
        sleep (2)
        print ("The road forks before you.")
        print("~")
        sleep(3)
        print("Choose your horse to take the southern road and avoid the town.")
        print("Choose your book of spells to continue into town.")
        print("~")
        
        id, text = reader.read()
        sleep(2)
    
        if id == horse_id:
            southern_road()
    
        if id == spell_id:
            town()

def dragon1():
    while True:
        print ("You decide to name the dragon Stanley after your favorite hut steamer.")
        sleep (2)
        print ("You travel for most of the morning. The road begins to fill with more and more travelers.")
        sleep (2)
        print ("Stanley's belly rumbles in hunger as she eyes the travelers around you. You are worried.")
        print("~")
        sleep (3)
        print ("Will you risk keeping the dragon on the road and feed her from the market in town, or will you coax her into the woods to search for wild beasts?") 
        print ("Choose your horse to stay on the road. Choose your shield to coax the dragon into the woods.")
        print("~")
        id, text = reader.read()
        sleep(2)  
        
        if id == horse_id:
            print("Stanley bellows a bone-chilling roar and leaps into the air.")
            sleep(3)
            print ("She races toward a large wagon full of supplies for the market.")
            print ("Stanley nabs the lead drafthorse and races away. Soon she is out of sight. You hope she will return.")
            sleep (2)
            print("~")
            print ("You have enough money in your pouch to pay the driver, but that will leave you with little money for the market.")
            print ("Choose your money pouch to compensate the driver. Choose your horse to continue on your way without paying the driver.")
                
            print("~")
            id, text = reader.read()
            sleep(2)
            
            if id == pouch_id:
                print("The merchant thanks you profusely and encourages you to stop by his stall in the market")
                print("You and your neighboring travelers share stories on the way into town.")
                town_menu()
            if id == horse_id:
                print("A huge group of travelers are pointing at you and shouting on behalf of the merchant whose horse became the dragon's lunch.")
                print("You apologize to the merchant and offer compensation to appease your conscience and the angry crowd surrounding you, paying double what the horse was worth.")
                print("~")
                sleep(3)
                print("You are out of money for now, and decide to avoid the town altogether.")
                print("~")
                sleep(3)
                southern_road()
                
                
        if id == shield_id:
            forest_thieves()
            sleep(2)

def forest_thieves():
    while True:
        print("You make chicken noises and dance around to get Stanley to follow you into the woods.")
        print("~")
        print("She follows you, but her tummy continues to rumble. You don't have much time left before you become lunch.")
        sleep(3)
        print("~")
        print("Suddenly, an arrow zips past your face and sinks into a tree trunk right in front of you.")
        print("A voice calls out telling you to halt!")
        print("~")
        print("Do you listen?")
        sleep(1)
        print("Choose your shield to raise your hands and await further instructions. Choose your sword to point in the direction of the voice and hope Stanley takes her cue to attack the owner of the voice.")
        print("~")
        
        id, text = reader.read()
		
        sleep(2)  
                    
        if id == shield_id:
            print("You calm Stanley down, and yell to the unknown assailant that you're going to cooperate.")
            print("An archer emerges from the bush in front of you. He intrduces himself as Robin Hood.")
            print("~")
            sleep(3)
            print("Robin Hood draws his sword, aims it toward you, and asks if you are a knight to the town king.")
            print("You quickly reply that you are simply a commoner, wandering the land seeking adventure and love.")
            print("Robin Hood inspects your gear, looks over to stanley, and back at you.")
            print("~")
            sleep(3)
            print("The sword is lowered.")
            sleep(2)
            print("Robin Hood explains that he recently stole gold coins from the local king.")
            print("He thought you might be a knight in disguise, but after looking at your gear and hearing your story...")
            sleep(2)
            print("He believes you.")
            print("~")
            print("You calm down after being interrogated and check on Stanley.")
            print("You hear a mighty rumble, and remember that Stanley is hungry")
            print("~")
            sleep(3)
            print("Robin Hood presents you with some meat for Stanley, in exchange that you don't rat him out to the town.")
            print("~")
            print("Scan your sword to remember that a very large reward is given if you find Robin Hood, take the meat, and rat out Robin Hood.")
            print("Or scan your money pouch to gladly accept his gift, and promise to keep his secret.")
    		
            id, text = reader.read()
            sleep(2)
			
            if id == sword_id:
                print("You get back to town, and rat out the location of Robin Hood")
                print("Robin Hood is caught, little Jon finds you and eliminates you. Maybe you should have kept Robin Hood's secret.")
                print("You chose poorly.")
                print("~~The End~~")
                print("This game is a collaborative project developed in the Red Rocks Community College IDEA Lab.") 
                print("To find out more, and to keep adding to this story, drop in and write with us!")
                print("~~~~~")
                sleep(6)
                menu()
                
            if id == pouch_id:
                print("As you are walking away, Robin Hood yells, and asks if you would like to join his crew and help him on his adventure.")
                print("~")
                print("Choose your horse to continue on with your adventure and head to the town. Or choose your sword to join Robin Hood on his adventure.")
		
                id, text = reader.read()
                sleep(2)
                
                if id == horse_id:
                    dragon_2()
                    
                if id == sword_id:
                    print("Robin Hood and the rest of the Merry Men and Women come to accept you and your dragon as their own.")
                    print("The rest of your days are a delightful mixture of adventure, romance, risk, and reward.")
                    print("~")
                    sleep(3)
                    print("~~The End~~")
                    print("This game is a collaborative project developed in the Red Rocks Community College IDEA Lab.") 
                    print("To find out more, and to keep adding to this story, drop in and write with us!")
                    print("~~~~~")
                    sleep(6)
                    menu()
                
        if id == sword_id:
            print("Stanley lets out a massive roar and leaps onto the unknown assailant.")
            print("~")
            sleep(3)
            print("Scan money pouch to get up and inpsect the damage. Or choose your horse to get up and continue on your quest.")
			
            id, text = reader.read()
            sleep(2)
			
            if id == pouch_id:
                print("You approach the downed enemy and find lots of gold coin, some food, a green hood, and a bow.")
                print("You pause and think to yourself, did I just kill Robin Hood?")
                print("~")
                sleep(3)
                print("A noise in the bushes breaks your train of thought")
                print("You peak around the bush and find Little Jon, badly injured.")
                print("~")
                print("Choose your horse to ignore Little Jon and move on with your quest. Or choose your shield to help Little Jon and talk to him.")
				
                id, text = reader.read()
                sleep(2)
				
                if id == horse_id:
                    print("You ignore Little Jon and continue on your adventure")
                    print("~")
                    sleep(3)
                    print("~")
                    rint("Stanley droops. You try to liven her up a bit with songs and stories of long ago quests. But it is clear she has a heavy conscience.")
                    print("~")
                    sleep(3)
                    print("Stanley leaps into the air and flaps a wing in goodbye.")
                    print("You continue your journey without a dragon.")
                    sleep(2)
                    town_menu()
					
                if id == shield_id:
                    print("You quickly run to Little Jon.")
                    print("He's hurt pretty badly, but he'll live.")
                    sleep(3)
                    print("Little Jon sees that you didn't mean to hurt them and asks if you would join his crew in place of Robin Hood.")
                    print("~")
                    sleep(3)
                    print("Choose your horse to refuse Little Jon's request and move on. Or choose your shield to help Little Jon and join him on his quest.")
                    
                    id, text = reader.read()
                    sleep(2)
                
                    if id == horse_id:
                        dragon_2()
                        
                    if id == shield_id:
                        Little_Jon()
		    
            if id == horse_id:
                print("You calm down Stanley, raid the defeated enemy's loot for food, and feed it to the dragon.")
                print("~")
                print("Stanley droops. You try to liven her up a bit with songs and stories of long ago quests. But it is clear she has a heavy conscience.")
                print("~")
                sleep(3)
                print("Stanley leaps into the air and flaps a wing in goodbye.")
                print("You continue your journey without a dragon.")
                sleep(2)
                southern_road()

def Little_Jon():
    while True:
        print("Little Jon and the rest of the Merry Men and Women come to accept you as one of their own.")
        print("The rest of your days are a delightful mixture of adventure, romance, risk, and reward.")
        print("~")
        sleep(3)
        print("~~The End~~")
        print("This game is a collaborative project developed in the Red Rocks Community College IDEA Lab.") 
        print("To find out more, and to keep adding to this story, drop in and write with us!")
        print("~~~~~")
        sleep(6)
        menu()


def dragon_2():
    while True:
        print("You and Stanley walk deeper into the woods, searching for a path that will bring you back to the main road.")
        print("But no road is in sight, and as you turn back the way you came you realize that the path has overgrown where you were walking.")
        print("An enchanted wood!")
        print("~")
        sleep(3)
        print("The forest grows darker and more crowded, so crowded Stanley can't even spread her wings to fly.")
        print("The only way through is straight ahead.")
        print("~")
        sleep(3)
        print("You and the dragon are tired. So you are tremendously relieved to see a cave up ahead.")
        print("At last, some respite.")
        print("~")
        sleep(3)
        print("As you approach the cave, however, a low growl rumbles from behind.")
        print("You were followed by a huge bear!")
        print("Choose the dragon to tell Stanley to attack. Choose your horse to run into the cave.")
        
        id, text = reader.read()
        sleep(2)
        if id == dragon_id:
            print("Stanley roars, herself, and tries to leap upon the giant bear.")
            print("Oh, no! Her wings are tripping her up in the tight space!")
            print("~")
            sleep(2)
            print("You draw your sword and charge, but the bear is far too mighty.")
            print("You and the dragon and your trusty steed become a healthy meal for the sorcerer bear.")
            print("~")
            sleep(3)
            print("~~The End~~")
            print("This game is a collaborative project developed in the Red Rocks Community College IDEA Lab.") 
            print("To find out more, and to keep adding to this story, drop in and write with us!")
            print("~~~~~")
            sleep(6)
            menu()   
                
            
        if id == horse_id:
            print("The cave is deep and full of bones.")
            print("But you do feel a soft breeze of chill air from the back.")
            print("~")
            sleep(3)
            print("Will you stay at the front of the cave and risk a bear attack or flash flood? Or will you drive deeper into the cave?")
            print("Choose your book of spells to cast a fireball to light your way deeper into the cave. Choose your shield to stay.")
                
            id, text = reader.read()
            sleep(2)
                
            if id == spell_id:
                print("Your fireball illuminates a deep cavern tunnel off to your right, but no other exits. The bear and dragon are growling at one another at the lip of the cave. There is little time left.")
                print("~")
                sleep(3)
                print("Choose your sword to call the dragon and your horse and try to escape down the tunnel. Choose your shield to stay and hold off the giant bear.")
                    
                id, text = reader.read()
                sleep(2)
                    
                if id == shield_id:
                    print("You draw your sword and stand beside Stanley as the bear rages.")
                    print("Stanley and you are both able to get in some good hits, but you are soon overcome.")
                    print("~")
                    sleep(3)
                    print("The bear is too mighty, and you fall.")
                    print("~~The End~~")
                    print("This game is a collaborative project developed in the Red Rocks Community College IDEA Lab.") 
                    print("To find out more, and to keep adding to this story, drop in and write with us!")
                    print("~~~~~")
                    sleep(6)
                    menu()
                if id == sword_id:
                    print("You and your horse scramble down the tunnel while rocks fall around your heads.")
                    print("The dragon stands at the lip of the tunnel and defends you from the bear.")
                    print("~")
                    sleep(3)
                    print("You hear a dreadful moan and thud. The dragon is badly hurt!")
                    print("~")
                    sleep(3)
                    print("But you have no time for sadness, as you hear the bear attempting to drag Stanley out of the way.")
                    print("Your horse is finally at the end of the tunnel and has miraculously escaped injury.")
                    print("~")
                    sleep(3)
                    print("Choose the dragon to rush up and check on Stanley. Choose the horse to continue on.")
                        
                    id, text = reader.read()
                    sleep(2)
                        
                    if id == dragon_id:
                        print("You dash up the tunnel and leap to put your hand on Stanley as she takes her last breath.")
                        print("All of a sudden, you are in a swirling vortex.")
                        print("~")
                        sleep(2)
                        print("A gentle mist falls, and you stand on a mossy hill surrounded by gentle woodland animals. Music and spring's sweetness float through the air.")
                        print("You are approached by a friendly gnome who explains that only those humans who are beloved by dragons are welcomed to this realm.")
                        print("~")
                        sleep(3)
                        print("You live out your days surrounded by friends among the enchanted realm of the gnomes.")
                        print("~")
                        print("~~The End~~")
                        print("This game is a collaborative project developed in the Red Rocks Community College IDEA Lab.") 
                        print("To find out more, and to keep adding to this story, drop in and write with us!")
                        sleep(4)
                        menu()
                    if id == horse_id:
                        print("You leap upon your horse and the two of you charge off down the hill to safety.")
                        print("You come to a crossroads.")
                        print("Choose the book of spells to continue onto the Southern Road. Choose your horse to continue into town.")
                            
                        id, text = reader.read()
                        sleep(2)
                            
                        if id == spell_id:
                            southern_road()
                                
                        if id == horse_id:
                            town()
                            
                            
                                                
            if id == shield_id:
                print("You draw your sword and stand beside Stanley as the bear rages.")
                print("Stanley and you are both able to get in some good hits, but you are soon overcome.")
                print("~")
                sleep(3)
                print("The bear is too mighty, and you fall.")
                print("~~The End~~")
                print("This game is a collaborative project developed in the Red Rocks Community College IDEA Lab.") 
                print("To find out more, and to keep adding to this story, drop in and write with us!")
                print("~~~~~")
                sleep(6)
                menu()
                
                
                
def town():
    while True:
        print ("The crush of people and wagons pushes you toward the market. You can smell the fresh bread and spices from here.")
        sleep (2)
        print("~")
        print ("But wait! You glimpse a darkened alley. For one tantalizing second, you spot the swinging sign of a magic shop peeking out of the shadows.")
        sleep (3)
        print("~")
        print ("Do you wish to continue to the marketplace? Or fight the crowd and seek out the magic shop?")
        print ("Choose your horse to go to the market. Choose your book of spells to seek out the magic shop")
        
        print("~")
        id, text = reader.read()
        sleep(2)  
                    
        if id == horse_id:
            market()
                
        if id == spell_id:
            magic_shop()
        
def market():
    while True:
        print("A row of stalls stretches before you.")
        print("So many sights and smells tickle your senses that you don't notice a group of masked jugglers start to fall in step behind you.")
        print("~")
        sleep(3)
        print("A pair of hands pulls a hood over your head. Your own hands are bound behind you.")
        print("You are dragged away from the market and through the maze of zig-zagging cobbled paths.")
        print("You can't imagine where you are.")
        print("~")
        sleep(3)
        print("Before long, you are roughly plopped onto a dust floor and the hood is yanked from your head.")
        print("You can feel the binds around your wrists loosen as your captors release you.")
        print("One of the masked strangers demands to know who you are. . .")
        print("What will you do?")
        print("~")
        print("Choose the heart to tell them your name and plead for your release. Choose the sword to attack.")
        
        id, text = reader.read()
        sleep(2)
        
        if id == heart_id:
            print("You speak your name.")
            print("Your captors visibly sigh with relief. They explain they were looking for some other traveller.")
            print("They apologize for scaring you and remove their masks.")
            print("~")
            sleep(3)
            print("They explain that they are truth-telling minstrels who were seeking revenge against a thief.")
            print("If you had done anything other than tell the truth, their magic could tear you to pieces.")
            print("~")
            sleep(3)
            print("The minstrels are impressed with your calm. They whisper together in consultation, then offer you a choice.")
            print("Do you wish to take a sack full of food, money, and supplies--all of the things you were hoping to buy at the market?")
            print("Or do you wish to join them and learn their magic?")
            print("~")
            print("Choose your money pouch to accept the minstrels' gifts and continue on your journey. Or choose the horse to join them.")
            
            id, text = reader.read()
            sleep(2)
            
            if id == horse_id:
                print("The magicians raise you up off the floor and pat you on the back, singing your name with praises.")
                print("Small sparks innocently flit about the room in joy.")
                print("~")
                sleep(3)
                print("You live out your days working hard as a juggler and a magician.")
                print("It's a happy life, indeed.")
                print("~~The End~~")
                sleep(3)
                print("This game is a collaborative project developed in the Red Rocks Community College IDEA Lab.") 
                print("To find out more, and to keep adding to this story, drop in and write with us!")
                sleep(4)
                menu()
            
            if id == pouch_id:
                print("You thank the minstrels. They return your horse.")
                print("You ask for directions and the minstrels point you in the direction of the main road.")
                print("Choose your horse to ride out of town")
                print("Choose your book of spells to seek out the magic shop.")
                
                id, text = reader.read()
                sleep(2)
                
                if id == horse_id:
                    print("You have clearly had enough of this town.")
                    print("You are at a crossroads.")
                    sleep(3)
                    print("Choose your shield to travel the River Road.")
                    print("Choose your horse to go to the Southern Road.")
            
                    id, text = reader.read()
                    sleep(2)
              
                    if id == shield_id:
                        print("Whoosh...")
                        sleep(2)
                        river_road()
                    if id == horse_id:
                        print("Whoosh...")
                        sleep(2)
                        southern_road()
                        
                if id == spell_id:
                    print("You wander the cobbled streets until you find the dark alley of the magic shop")
                    sleep(3)
                    magic_shop()


def magic_shop():
    while True:
        print("The bell rings above your head as you enter the smoky, dimly lit shop. Immediately you are overcome by the aroma of exotic spices that make your head swim. All around you are strange and mysterious objects.")
        print("~")
        print("You see the elderly shop keeper near the front of the shop...you aren't sure if they are asleep or possibly deceased. Towards the back of the shop you notice a faint pulsing red light that fills you with curiosity.")
        print("~")
        sleep(3)
        print("Choose the Money Pouch to make your way towards the front of the shop. Choose the Dragon to sneak toward the pulsing light.")
        print("~")
        
        id, text = reader.read()
        sleep(2)
        
        if id == pouch_id:
            print("As you make your way toward the front of the shop you knock into a table of small glass bottles filled with shimmering colors. You catch one bottle as it is about fall to the floor.")
            print("The shopkeeper is startled awake and looks you over with an overtly disapproving gaze.")
            print("~")
            sleep(3)
            print("What do you want?")
            sleep(3)
            print("The shopkeeper sees the bottle in your hand and narrows their eyes.")
            print("I'm not sure what that does, I just...acquired it. It's yours for a gold. But no returns!")
            print("~")
            sleep(3)
            print("Choose the Money Pouch to buy the potion. Choose the horse to leave the shop empty-handed and make your way to the market.")
            print("~")
            
            id, text = reader.read()
            sleep(2)
                
            if id == pouch_id:
                print("Do you drink the potion now? Or save it for later?")
                print("~")
                sleep(3)
                print("Choose the potion to test your luck and drink the potion now. Or choose the shield to play it safe and wait.")
                 
                id, text = reader.read()
                sleep(2)
                        
                if id == potion_id:
                    print("You look down at the glowing potion and decide to take a chance.")
                    print("The potion is slowly glowing red, then blue, then green.")
                    print("~")
                    print("To drink the potion while it's glowing red choose the heart, for green choose the dragon, or for blue choose the shield.")
                    print("~")
                    sleep(3)
                                                
                    id, text = reader.read()
                    sleep(2)
                            
                    if id == heart_id:
                        print("Whoosh!")
                        print("A rush of air and sweeping colors runs past your eyes as you find yourself in a mystical tunnel.")
                        print("Thank goodness your horse and pack are somehow still beside you.")
                        print("~")
                        witch()
                            
                    if id == dragon_id:
                        print("Whoosh!")
                        print("A rush of air and sweeping colors runs past your eyes as you find yourself in a mystical tunnel.")
                        print("Thank goodness your horse and pack are somehow still beside you.")
                        print("~")
                        river_road()
                            
                    if id == shield_id:
                        print("Whoosh!")
                        print("A rush of air and sweeping colors runs past your eyes as you find yourself in a mystical tunnel.")
                        print("Thank goodness your horse and pack are somehow still beside you.")
                        print("~")
                        giant()
                            
                        
                if id == shield_id:
                    print("You give the shopkeeper a gold piece from your dwindling supply, pocket the potion and make your way out into the fresh air and towards the market.")
                    print("~")
                    sleep(2)
                    market()
               
            if id== horse-id:
                print("You decide to play it safe and leave empty handed into the crowds moving towards the market.")
                print("~")
                sleep(2)
                market()
                  
            
        if id == dragon_id:
            print("The shop seems to grow colder as you move towards the back.")
            print("The pulsing light is coming from a large jewel shaped like a heart.")
            print("~")
            sleep(3)
            print("As you are staring at the jewel, you hear a faint voice.")
            print("'Steal Me! And I will give you unimaginable rewards.'")
            sleep(3)
            print("Choose the heart to steal the jewel and reap your reward. Choose the money pouch to leave the jewel where it is and make your way back to the front of the shop.")
            print("~")
            
            id, text = reader.read()
            sleep(2)
                
            if id == heart_id:
                print("As you reach out to steal the jewel, the world suddenly begins to fade and turn red. As the world around you is replaced by a red faceted kaleidescope you hear the  same voice laughing.")
                print("~")
                sleep(1)
                print("Now you can wait a hundred years for someone to try and steal YOU from that prison!")
                print("~")
                sleep(3)
                print("Game Over")
                sleep(3)
                print("This game is a collaborative project developed in the Red Rocks Community College IDEA Lab.") 
                print("To find out more, and to keep adding to this story, drop in and write with us!")
                sleep(4)
                menu()
                    
            if id == pouch_id:
                print("As you make your way toward the front of the shop you knock into a table of small glass bottles filled with shimmering colors. You catch one bottle as it's about fall to the floor, the shopkeeper is startled awake and looks you over with an overtly disapproving gaze.")
                print("~")
                sleep(3)
                print("What do you want?")
                sleep(3)
                print("The shopkeeper sees the bottle in your hand and narrows their eyes.")
                print("I'm not sure what that does, I just...acquired it. It's yours for a gold. But no returns!")
                print("~")
                sleep(3)
                print("Choose the Money Pouch to buy the potion. Choose the horse to leave the shop empty handed and make your way to the market.")
                print("~")
            
                id, text = reader.read()
                sleep(2)
                
                
                
                if id == pouch_id:
                    print("Do you drink the potion now? Or save it for later?")
                    print("~")
                    sleep(2)
                    print("Choose the potion to test your luck and drink the potion now. Or choose the shield to play it safe and wait.")
                 
                    id, text = reader.read()
                    sleep(2)
                        
                    if id == potion_id:
                        print("You look down at the glowing potion and decide to take a chance.")
                        print("The potion is slowly glowing red, then blue, then green.")
                        print("~")
                        print("To drink the potion while it's glowing red choose the heart, for green choose the dragon, or for blue choose the shield.")
                        print("~")
                        sleep(3)
                                                
                        id, text = reader.read()
                        sleep(2)
                            
                        if id == heart_id:
                            print("....")
                            print("Whoosh!")
                            print("A rush of air and sweeping colors runs past your eyes as you find yourself in a mystical tunnel.")
                            print("Thank goodness your horse and pack are somehow still beside you.")
                            print("~")
                            witch()
                            
                        if id == dragon_id:
                            print("....")
                            print("Whoosh!")
                            print("A rush of air and sweeping colors runs past your eyes as you find yourself in a mystical tunnel.")
                            print("Thank goodness your horse and pack are somehow still beside you.")
                            print("~")
                            castle()
                            
                        if id == shield_id:
                            print("....")
                            print("Whoosh!")
                            print("A rush of air and sweeping colors runs past your eyes as you find yourself in a mystical tunnel.")
                            print("Thank goodness your horse and pack are somehow still beside you.")
                            print("~")
                            giant()
                            
                    if id== horse-id:
                        print("You decide to play it safe and leave empty handed into the crowds moving towards the market.")
                        print("~")
                        sleep(3)
                        market()
      
        
        
def southern_road():
    while True:
        sleep(2)
        print("Overhead, a storm brews. Fewer and fewer travelers remain on the road.")        
        print("Soon, you are alone.")
        print("~")
        sleep(3)
        print("Darkness falls.")
        sleep(3)
        print("~")
        print("You spot a small fire twinkling ahead. But the flames glow pink and green and blue.")        
        print("Sorcery....")
        print("Do you wish to go near?")
        print("~")
        print("Choose the book of spells to go closer. Choose your horse to continue on.")
        
        id, text = reader.read()
        sleep(2)
        
        if id == spell_id:
            witch()
            
        if id == horse_id:
            river_road()

def witch():
    while True:
        print("As you approach the twinkling fire, mysterious smoke curls around you.")
        sleep(3)
        print("All of a sudden, POOF...through a thick cloud of smoke, a witch stands before you.")
        sleep(3)
        print("Witch - 'It appears that your travels have led you to me'")
        sleep(3)
        print("'Choose your next action carefully...'")
        sleep(3)
        print("Will you draw your trusty sword and attempt to strike down the wicked witch? Or grab your book of spells to ask the witch her name?")
        #user_choice= input("Pick...")
        id, text = reader.read()
        sleep(3)
        #if user_choice == '1':
        if id == sword_id:
            witch_attack()
        #if user_choice == '2':
        if id == spell_id:
            witch_spell()
        

def witch_attack():
    while True:
        print("You have choosen to attack the witch with your trusty sword...")
        print("~")
        sleep(3)
        print("You swipe at the witch's face, closing your eyes as you do because you're scared.")
        print("~")
        sleep(3)
        print("As you open your eyes, you realize that the witch dodged your attack and you swung yourself to the edge of a cliff...")
        print("~")
        sleep(3)
        print("You stumble off the ledge. You quickly realize you aren't standing on solid ground and you fall to your demise (much like in the cartoons).")
        print("...")
        sleep(3)
        print("But wait... as you fall the witch uses her magic to speak to you and tell you she was once a beutiful queen who gave up her looks for magic so that she could use her powers to save her village from the evil dragon")
        print("~")
        sleep(5)
        print("You realize that had you simply been brave and approached her with kindness, she could have helped you on your quest.")
        print("~~~~~")
        print("You chose poorly.")
        sleep(3)
        print("~~The End~~")
        print("This game is a collaborative project developed in the Red Rocks Community College IDEA Lab.") 
        print("To find out more, and to keep adding to this story, drop in and write with us!")
        sleep(3)
        menu()
    
    
def witch_spell():
    while True:
        print("My name is Claire. I was once the queen of a small village called Asgard. One day a dragon approched my village in search of gold...")
        print("~")
        sleep(3)
        print("Being a small poor town we did not have much gold and what we did have my people needed.")
        print("So I pleaded with the dragon and asked if there was another way.")
        print("~")
        sleep(3)
        print("Being a clever dragon, he decided that he would spare my village if I was forced to walk the world forever more as a hideous witch...")
        print("~")
        sleep(3)
        print("Since then I have dedicated my life to helping others.")
        print("~")
        sleep(3)
        print("I am happy to help you on your journey...")
        print("~")
        sleep(5)
        print("Choose your horse to ask if she will point you in the direction of the next adventure. Choose the potion to thank her for her time and ask if she can offer any advice for your travels. ")
    #user_choice = input("pick...")
        id, text =reader.read()
        sleep(4)
    #if user_choice == '1':
        if id == potion_id:
            witch_potion()
    #if user_choice =='2':
        if id == horse_id:
            witch_horse()

def witch_horse():
    while True:
        print("'Of course, young traveler. Thank you for speaking with me.'")
        print("'I am glad to point you on your way. Follow the river through the valley, stay close to it as it will guide you through the treacherous land ahead.'")
        sleep(3)
        waiting_for_input = False
        print("'Good luck, young one...'")
        sleep(3)
        river_road()

def witch_potion():
    while True:
        print("'Of course, young traveler. Thank you for speaking with me. I am glad to offer you some advice.'")
        print("'I can offer you much advice from my travels. However, perhapse the most important is to be honorable and pay what must be payed...'")
        sleep(3)
        print("She dissolves in a puff of brilliant fire that releases a few whisps of smoke.")
        print("~")
        sleep(3)
        print("You continue your journey")
        sleep(2)
        giant()


def river_road():
    while True:
        sleep(2)
        print("A river winds before you through a shallow valley, reaching as far as you can see, surrounded on both sides by a dense wood.")
        sleep(3)
        print("As you make your way through the valley, you are careful to stick as close to the river as possible, for you hear distant howls and you fear what might lurk in the shadows.")
        print("The river's current is a comforting rumble beside you.")
        print("~")
        print("...")
        print("Before long, the river drops suddenly into a waterfall.")
        print("You look down and are astonished to spy a ship with black sails nestled in a cove close to the falls. You can see and smell the ocean beyond.")
        sleep(3)
        print("Will you follow the river road down to the water's edge? Or will you go back the way you came?")
        print("~")
        print("Choose your horse to continue down to the water and the pirate ship below. Choose your shield to turn back.")
        
        id, text = reader.read()
        sleep(2)
        
        if id == horse_id:
            print("You attempt a stealthy advance.")
            print("The loose stones of the river path deny any measure of quiet, as they dance down the path and PLUNK into the water below.")
            print("...")
            sleep(3)
            print("You are unsurprised as you hear a voice telling you to halt and state your business.")
            print("Decision time: Do you draw your sword? Grab your book of spells? Or hold up your money pouch to show that you are harmless?")
                  
            id, text = reader.read()
            sleep(2)
            
            if id == sword_id:
                print("You take your sword in hand and bravely charge forward at the nearest pirate. She feints. The two behind you skewer your body with their cutlasses--cutlassi (?)--anyway, you're dead.")
                print("~")
                print("As you take your last breath, you are disturbed to hear the distinct sound of a horse eating a carrot out of a pirate's hand, and the tinkling of your money pouch as it hits the ground.")
                sleep(3)
                print("~~The End~~")
                print("This game is a collaborative project developed in the Red Rocks Community College IDEA Lab.") 
                print("To find out more, and to keep adding to this story, drop in and write with us!")
                sleep(4)
                menu()
            if id == spell_id:
                print("You grab your book of spells")
                print("Will you grab the flames to cast fire? Or will you grab the crystal to cast frost?")
                print("~")
                
                id, text = reader.read()
                sleep(2)
                
                if id == fire_id:
                    print("A firebolt warms your fingers. You hurl it toward the awaiting pirates.")
                    print("As you cast your spell, the quick-footed swashbucklers dance out of danger.")
                    print("Obviously, you aren't the first magician these pirates have encountered.")
                    print("~")
                    sleep(3)
                    print("The last thing you hear is a loud THUD as your vision fades to black")
                    print("...")
                    sleep(2)
                    pirate_ship()
                    
                if id == frost_id:
                    print("A bolt of ice chills your fingers. You hurl it toward the awaiting pirates.")
                    print("As you cast your spell, the quick-footed swashbucklers dance out of danger.")
                    print("Obviously, you aren't the first magician these pirates have encountered.")
                    print("~")
                    sleep(2)
                    print("The last thing you hear is a loud THUD as your vision fades to black")
                    print("...")
                    sleep(3)
                    pirate_ship()
                
                
            if id == pouch_id:
                print("The pirate captain steps forward and she takes your money pouch.")
                print("She digs through your meager horde and takes pity on you.")
                print("~")
                sleep(2)
                print("She takes all but the last two pieces of gold and sends you on your way.")
                print("The horse whinnies along with the rest of her crew... She tosses your horse a carrot.")
                print("~")
                sleep(3)
                print("You carry along and eventually find yourself along a new path.")
                sleep(1)
                giant()
                
                
                  
                  
        if id == shield_id:
            print("You nudge your horse to turn around and go back.")
            print("As you turn, a shadowy figure steps from the trees, followed by more.")
            print("Soon, you are surrounded. Your horse whinnies at your expense.")
            print("~")
            sleep(3)
            print("A voice calls out demanding your business.")
            print("Decision time: Do you draw your sword? Grab your book of spells? Or hold up your money pouch to show that you are harmless?")
            print("~")
            
            id, text = reader.read()
            sleep(2)
            
            if id == pouch_id:
                print("The pirate captain steps forward and she takes your money pouch.")
                print("She digs through your meager horde and takes pity on you.")
                print("~")
                sleep(3)
                print("She takes all but the last two pieces of gold and sends you on your way.")
                print("The horse whinnies along with the rest of her crew... She tosses your horse a carrot.")
                print("~")
                sleep(3)
                print("You carry along and eventually find yourself along a new path.")
                sleep(1)
                giant()
            
            if id == sword_id:
                print("You take your sword in hand and bravely charge forward at the nearest pirate. She feints. The two behind you skewer your body with their cutlasses--cutlassi (?)--anyway, you're dead.")
                print("~")
                print("As you take your last breath, you are disturbed to hear the distinct sound of a horse eating a carrot out of a pirate's hand, and the tinkling of your money pouch as it hits the ground.")
                sleep(3)
                print("~~The End~~")
                print("This game is a collaborative project developed in the Red Rocks Community College IDEA Lab.") 
                print("To find out more, and to keep adding to this story, drop in and write with us!")
                sleep(4)
                menu()
            if id == spell_id:
                print("You grab your book of spells")
                print("Will you grab the flames to cast fire? Or will you grab the crystal to cast frost?")
                print("~")
                
                id, text = reader.read()
                sleep(2)
                
                if id == fire_id:
                    print("A firebolt warms your fingers. You hurl it toward the awaiting pirates.")
                    print("As you cast your spell, the quick-footed swashbucklers dance out of danger.")
                    print("Obviously, you aren't the first magician these pirates have encountered.")
                    print("~")
                    sleep(3)
                    print("The last thing you hear is a loud THUD as your vision fades to black")
                    print("...")
                    sleep(3)
                    pirate_ship()
                    
                if id == frost_id:
                    print("A bolt of ice chills your fingers. You hurl it toward the awaiting pirates.")
                    print("As you cast your spell, the quick-footed swashbucklers dance out of danger.")
                    print("Obviously, you aren't the first magician these pirates have encountered.")
                    print("~")
                    sleep(3)
                    print("The last thing you hear is a loud THUD as your vision fades to black")
                    print("...")
                    sleep(3)
                    pirate_ship()
            
            

def tournament():
    while True:
        print("You find yourself among a crowd next to a tournament ring.")
        print("The mix of smells and sounds from the crowd and horses and minstrels nearly overwhelms you. But your blood sings for sport.")
        print("~")
        sleep(3)
        print("You hear a voice call out over the roar of the crowd")
        print("Impossible! The Black Knight has insulted the Queen!")
        print("~")
        sleep(3)
        print("Will you defend the honor of your monarch and challenge The Black Knight in a joust?")
        print("Draw your sword to state your challenge. Choose the horse to continue on your journey.")
        print("~")
        
        id, text = reader.read()
        sleep(2)
        
        if id == sword_id:
            print("The Black Knight giggles maniacally and accepts your challenge.")
            print("~")
            print("This is your first joust. Good luck!")
            sleep(3)
            print("A warlock approaches...")
            print("...")
            sleep(3)
            print("He offers to curse your opponent and guarantee you a victory.")
            print("~")
            print("Will you accept the warlock's help?")
            print("Choose your sword to deny help and risk losing to the Black Knight. Choose the potion bottle to accept the warlock's help and curse your opponent.")
            print("~")
            
            id, text = reader.read()
            sleep(2)
            
            if id == sword_id:
                print("You set your pack on the ground and select a borrowed lance and some ill-fitting armor from the Lost and Found.")
                print("You guide your horse to your place across the lists from The Black Knight, who continues to think this whole situation is very funny.")
                print("Your horse charges. You level your borrowed lance in the direction of The Black Knight and hit a glancing blow.")
                print("~")
                sleep(3)
                print("You and your opponent line up to face each other once again.")
                print("He is taunting you, though it looks like he might be getting worried.")
                sleep(3)
                print("You charge at each other again!")
                print("But this time, The Black Knight connects with some filigree on your borrowed armor and sends you flying off your horse.")
                print("~")
                sleep(3)
                print("Before you have a chance to grab your sword, he is running at you with his.")
                print("Do you surrender?")
                print("Choose your shield to surrender and continue on your journey.")
                print("Choose your sword to attack.")
                
                id, text = reader.read()
                sleep(2)
                
                if id == shield_id:
                    print("You lay down your sword and accept defeat.")
                    print("The villagers boo you, but not too harshly.")
                    print("The Black Knight pats you heavily on the back and sends you on your way, alive.")
                    print("~")
                    sleep(2)
                    river_road()
                if id == sword_id:
                    print("You ninja roll, dodging The Black Knight's attack. Stretching your arm out and using 'Ye Force,' you pull your sword back to your hand.")
                    sleep(2)
                    print("You knock The Black Knight off-balance and kick his sword out of his hand.")
                    print("The Black Knight yields and reveals that he is actually ... your father.")
                    print("'Noooooooooooooooo,' you cry to the universe.")
                    print("~")
                    print("The crowd roars and wants you to throw him in the river, a death sentence in all of his heavy armor.")
                    print("~")
                    sleep(3)
                    print("Choose your sword to throw The Black Knight in the river. Choose your shield to take mercy on him. Choose your horse to leave The Black Knight where he stands and continue on your journey.")
                    
                    id, text = reader.read()
                    sleep(2)
                    
                    if id == sword_id:
                        print("The Queen appreciates you. She invites you to celebrate in the castle.")
                        print("You return your borrowed gear and head to the castle.")
                        sleep(3)
                        castle()
                    if id == shield_id:
                        print("The Queen rewards your mercy. She invites you to celebrate in the castle.")
                        print("You return your borrowed gear and head to the castle.")
                        sleep(3)
                        castle()
                    if id == horse_id:
                        print("The villagers chant your name as you head out of town and seek a path to explore.")
                        sleep(2)
                        river_road()
                
            if id == potion_id:
                print("The Black Knight trips over his feet. Your sorcery is easily detected.")
                print("The village brands you a coward and tosses you into the river.")
                print("Your armor weighs you down, and you quickly sink to the bottom of the river and drown.")
                print("~")
                sleep(3)
                print("You chose poorly.")
                sleep(3)
                print("~~The End~~")
                print("This game is a collaborative project developed in the Red Rocks Community College IDEA Lab.") 
                print("To find out more, and to keep adding to this story, drop in and write with us!")
                sleep(4)
                menu()
        
        if id == horse_id:
            print("Your horse refuses to obey.")
            print("You draw the notice of the crowd as you try in vain to persuade your horse to move along. The horse throws you to the ground and whinnies at your expense, then saunters to the railing to munch on flowers.")
            sleep(3)
            print("The Black Knight adds insult to injury by throwing a gauntlet in your general direction.")
            print("~")
            sleep(3)
            print("Will you meet the Black Knight's challenge? Or will you continue your retreat?")
            print("Draw your sword to accept the challenge. Or choose your horse to avoid the Black Knight and attempt to move your horse away from lunch.")
            print("~")
            
            id, text = reader.read()
            sleep(2)
            
            if id == sword_id:
                print("The Black Knight giggles maniacally and accepts your challenge.")
                print("You guide your horse to the west end of the ring and prepare for battle.")
                print("~")
                print("This is your first joust.")
                sleep(3)
                print("A warlock approaches...")
                print("...")
                leep(2)
                print("He offers to curse your opponent and guarantee you a victory.")
                print("~")
                print("Will you accept the warlock's help?")
                print("Choose your sword to deny help and risk losing to the Black Knight. Choose the potion bottle to accept the warlock's help and curse your opponent.")
                print("~")
            
                id, text = reader.read()
                sleep(2)
            
                if id == sword_id:
                    print("You set your pack on the ground and select a borrowed lance and some ill-fitting armor from the Lost and Found.")
                    print("You guide your horse to your place across the lists from The Black Knight, who continues to think this whole situation is very funny.")
                    print("Your horse charges. You level your borrowed lance in the direction of The Black Knight and hit a glancing blow.")
                    print("~")
                    sleep(3)
                    print("You and your opponent reach the edges of the arena and line up to face each other once again.")
                    print("He is taunting you, though it looks like he might be getting worried.")
                    sleep(3)
                    print("You charge at each other again!")
                    print("But this time, The Black Knight connects with some filigree on your borrowed armor and sends you flying off your horse.")
                    print("~")
                    sleep(3)
                    print("Before you have a chance to grab your sword, he is running at you with his.")
                    print("Do you surrender?")
                    print("Choose your shield to surrender and continue on your journey.")
                    print("Choose your sword to attack.")
                
                    id, text = reader.read()
                    sleep(2)
                
                    if id == shield_id:
                        print("You lay down your sword and accept defeat.")
                        print("The villagers boo you, but not too harshly.")
                        print("The Black Knight pats you heavily on the back and sends you on your way, alive.")
                        print("~")
                        sleep(3)
                        river_road()
                    if id == sword_id:
                        print("You ninja roll, dodging The Black Knight's attack. Stretching your arm out and using 'Ye Force,' you pull your sword back to your hand.")
                        sleep(3)
                        print("You knock The Black Knight off-balance and kick his sword out of his hand.")
                        print("The Black Knight yields and reveals that he is actually ... your father.")
                        print("'Noooooooooooooooo,' you cry to the universe.")
                        print("~")
                        rint("The crowd roars and wants you to throw him in the river, a death sentence in all of his heavy armor.")
                        print("~")
                        sleep(3)
                        print("Choose your sword to throw The Black Knight in the river. Choose your shield to take mercy on him. Choose your horse to leave The Black Knight where he stands and continue on your journey.")
                    
                        id, text = reader.read()
                        sleep(2)
                    
                        if id == sword_id:
                            print("The Queen appreciates you. She invites you to celebrate in the castle.")
                            print("You return your borrowed gear and head to the castle.")
                            sleep(3)
                            castle()
                        if id == shield_id:
                            print("The Queen rewards your mercy. She invites you to celebrate in the castle.")
                            print("You return your borrowed gear and head to the castle.")
                            sleep(3)
                            castle()
                        if id == horse_id:
                            print("The villagers chant your name as you head out of town and seek a path to explore.")
                            sleep(3)
                            river_road()
                
                if id == potion_id:
                    print("The Black Knight trips over his feet. Your sorcery is easily detected.")
                    print("The village brands you a coward and tosses you into the river.")
                    print("Your armor weighs you down, and you quickly sink to the bottom of the river and drown.")
                    print("~")
                    sleep(3)
                    print("You chose poorly.")
                    sleep(3)
                    print("~~The End~~")
                    print("This game is a collaborative project developed in the Red Rocks Community College IDEA Lab.") 
                    print("To find out more, and to keep adding to this story, drop in and write with us!")
                    print("~~~~~")
                    sleep(6)
                    menu()
            
            if id == horse_id:
                print("The village brands you a coward and tosses you into the river.")
                print("Your armor weighs you down, and you quickly sink to the bottom of the river and drown.")
                print("~")
                sleep(3)
                print("You chose poorly.")
                sleep(3)
                print("~~The End~~")
                print("This game is a collaborative project developed in the Red Rocks Community College IDEA Lab.") 
                print("To find out more, and to keep adding to this story, drop in and write with us!")
                sleep(4)
                menu()
                
def castle():
    while True:
        print("You arrive at Castle Greyskull to find that it has fallen under an evil curse.")
        print("Will you fight an unknown enemy to break the curse?")
        print("~")
        print("Choose your horse to leave the castle and return to your journey.")
        print("Choose your sword to enter the castle and challenge the unknown enemy.")
        print("~")
        sleep(3)
        print("Choose wisely.")
        
        id, text = reader.read()
        sleep(2)
        
        if id == horse_id:
            print("You are at a crossroads.")
            sleep(2)
            print("Choose your money pouch to travel to the Market.")
            print("Choose your horse to go to the Southern Road.")
            
            id, text = reader.read()
            sleep(2)
              
            if id == pouch_id:
              print("Whoosh...")
              sleep(2)
              market()
            if id == horse_id:
              print("Whoosh...")
              sleep(2)
              southern_road()
        
        if id == sword_id:
            print("The castle looms before you. You hear distant cries and your nose tingles with the smell of burnt toast.")
            sleep(3)
            print("As you cross the draw bridge, you encounter a headless skeleton armed with a sword gnashing a piece of toast.")
            print("Will you draw your own sword? Reach for your invisibility potion to sneak past? Or open your book of spells?")
            print("The skeleton awaits your choice with an unnerving, unblinking stare. Still chewing.")
            Print("~")
            id, text = reader.read()
            sleep(2)
            
            if id == sword_id:
                print("You attack with your sword!")
                print("You let out a brave howl and charge toward the skeleton.")
                print("~")
                sleep(3)
                print("Your thrust slides right through the rib cage and is twisted from your grasp.")
                print("Oh, no.")
                sleep(3)
                print("The skeleton counters, skewering your torso.")
                sleep(3)
                print("You die cursing your decision to to stab an organless opponent.")
                print("...")
                sleep(3)
                print("You chose poorly.")
                sleep(3)
                print("~~The End~~")
                print("This game is a collaborative project developed in the Red Rocks Community College IDEA Lab.") 
                print("To find out more, and to keep adding to this story, drop in and write with us!")
                sleep(4)
                menu()
            
            if id == potion_id:
                print("You swig from your invisibility potion and feel your skin tingle as it takes effect.")
                print("You attempt to sneak past the skeleton, but as you pass, it thrusts its sword and skewers your torso.")
                print("~")
                sleep(3)
                print("You die realizing the skeleton had no eyes to be fooled by your invisibility.")
                print("...")
                sleep(3)
                print("You chose poorly.")
                sleep(3)
                print("~~The End~~")
                print("This game is a collaborative project developed in the Red Rocks Community College IDEA Lab.") 
                print("To find out more, and to keep adding to this story, drop in and write with us!")
                sleep(4)
                menu()
            
            if id == spell_id:
                print("You flip open your book of spells and a fireball blossoms in the palm of your hand.")
                print("You toss the fireball at the skeleton!")
                print("...")
                sleep(3)
                print("The skeleton is engulfed in flames and is quickly reduced to a pile of dust.")
                print("~")
                print("You step over the pile and continue into the castle, turning ever inward toward the throne room.")
                print("~")
                sleep(3)
                print("In the throne room, you see the Queen.")
                print("She smiles at you and congratulates you on defeating the skeleton.")
                sleep(3)
                print("She surprises you as she asks if you would like to join her and conquer the world, enslaving everyone under her tyranny.")
                print("Do you choose to join her?")
                print("~")
                print("Choose your sword to join the Queen and conquer the world.")
                print("Choose your shield to brace yourself as you tell her no.")
                
                id, text = reader.read()
                sleep(2)
                
                if id == sword_id:
                    print("You declare your fealty to the Queen.")
                    print("She immediately transforms into her true identity, a hungry dragon.")
                    print("She gobbles you in a single bite.")
                    print("~")
                    sleep(3)
                    print("You chose poorly.")
                    sleep(3)
                    print("~~The End~~")
                    print("This game is a collaborative project developed in the Red Rocks Community College IDEA Lab.") 
                    print("To find out more, and to keep adding to this story, drop in and write with us!")
                    print("~~~~~")
                    sleep(6)
                    menu()
                if id == shield_id:
                    print("The Queen immediately transforms into her true identity, a hungry dragon.")
                    print("She lets out a bout of flame that licks the edges of your shield as you brace for impact.")
                    print("~")
                    sleep(3)
                    print("Will you attack with your Sword? Will you drink from your invisibility potion? Or will you grab your book of spells?")
                    
                    id, text = reader.read()
                    sleep(2)
                    
                    if id == sword_id:
                        print("You draw your sword and charge toward the dragon.")
                        print("You thrust, and your blow glances off her armor.")
                        print("She rumbles at you in laughter.")
                        sleep(3)
                        print("She gobbles you in a single bite.")
                        print("~")
                        sleep(3)
                        print("You chose poorly.")
                        sleep(3)
                        print("~~The End~~")
                        print("This game is a collaborative project developed in the Red Rocks Community College IDEA Lab.") 
                        print("To find out more, and to keep adding to this story, drop in and write with us!")
                        sleep(4)
                        menu()
                    if id == potion_id:
                        print("You take a swig from your invisibility potion.")
                        print("Your skin tingles as it takes effect.")
                        print("~")
                        print("The dragon grunts in surprise as you disappear. You feel her breath against your armor and freeze in terror, afraid to move and draw attention to your position.")
                        print("You can hear your heartbeat, and hope the dragon can't... > ... > ... >")
                        sleep(3)
                        print("She grumbles and wanders off to find some other snack.")
                        print("You are safe for now.")
                        print("~")
                        print("What will you do next? Will you choose your horse to leave the castle? Or will you choose your sword to take use your strategic advantage and attack the dragon while she doesn't expect it?")
                        
                        id, text = reader.read()
                        sleep(2)
                        
                        if id == horse_id:
                            print("You are at a crossroads.")
                            sleep(2)
                            print("Choose your money pouch to travel to the Market.")
                            print("Choose your horse to go to the Southern Road.")
            
                            id, text = reader.read()
                            sleep(2)
              
                            if id == pouch_id:
                                print("Whoosh...")
                                sleep(2)
                                market()
                            if id == horse_id:
                                print("Whoosh...")
                                sleep(2)
                                southern_road()
                        
                        if id == sword_id:
                            print("You draw your sword and charge toward the dragon.")
                            print("Unfortunately, the dragon is clever. She was waiting for you to give up your position.")
                            print("She rumbles at you in laughter.")
                            sleep(3)
                            print("She gobbles you in a single bite.")
                            print("~")
                            sleep(3)
                            print("You chose poorly.")
                            sleep(3)
                            print("~~The End~~")
                            print("This game is a collaborative project developed in the Red Rocks Community College IDEA Lab.") 
                            print("To find out more, and to keep adding to this story, drop in and write with us!")
                            sleep(4)
                            menu()
                        
                    if id == spell_id:
                        print("You flip through your book of spells.")
                        print("Will you choose the flame to cast a fireball?")
                        print("Or will you choose the crystal to throw an ice bolt?")
                        print("~")
                              
                        id, text = reader.read()
                        sleep(2)
                        
                        if id == fire_id:
                            print("You toss a fireball at the dragon.")
                            print("She roars and opens her mouth to swallow the flames and spit them right back at you.")
                            print("You sigh and remember that dragons love fire as you are rapidly engulfed by your own spell.")
                            print("...")
                            print("You chose poorly.")
                            sleep(3)
                            print("~~The End~~")
                            print("This game is a collaborative project developed in the Red Rocks Community College IDEA Lab.") 
                            print("To find out more, and to keep adding to this story, drop in and write with us!")
                            sleep(4)
                            menu()
                        if id == frost_id:
                            print("You hurtle a bolt of ice at the dragon, freezing a section of her plates and sending her reeling backward from the impact.")
                            print("...")
                            sleep(3)
                            print("You see your chance. You charge at the dragon with your sword, piercing the broken plates where your ice bolt landed.")
                            print("~")
                            print("The dragon roars and disintegrates into dust.")
                            sleep(3)
                            print("The ground beneath you trembles and a tree bursts from the floor.")
                            print("~")
                            sleep(3)
                            print("A mystical voice thanks you for releasing her spirit from the dragon, where she was trapped for a hundred years.")
                            print("The voice grants you the castle and the surrounding land.")
                            print("~")
                            print("You live out your days helping the villagers rebuild their town and fields from the damage done by the bewitched dragon queen.")
                            sleep(3)
                            print("You chose wisely")
                            sleep(3)
                            print("~~The End~~")
                            print("This game is a collaborative project developed in the Red Rocks Community College IDEA Lab.") 
                            print("To find out more, and to keep adding to this story, drop in and write with us!")
                            sleep(3)
                            menu()
                            
                        
                    
        

def giant():
    while True:
        print("The path before you is tangled with weeds. You fight them as you make your way forward. Your horse isn't very happy about it.")
        print("You come to a glade with odd-shaped mounds overgrown with vines and more of the tangled, grasping weeds you encountered on the path.")
        print("~")
        sleep(3)
        print("Magic tingles in the air, raising the little hairs on the back of your neck.")
        print("Something here is not what it seems.")
        print("~")
        sleep(3)
        print("Choose your book of spells to investigate the magical glade. Choose your sword to continue hacking through weeds and past the glade.")
        print("~")
        
        id, text = reader.read()
        sleep(2)
        
        if id == spell_id:
            print("As you approach one of the mounds closest to you, a mighty sneeze explodes from the other side of the glade.")
            print("The other mounds jump and then relax, as a booming voice yells 'Ouch!'")
            print("~")
            sleep(3)
            print("What will you do? Choose your sword to step closer. Choose your horse to beat a path out of the glade to safety.")
            
            id, text = reader.read()
            sleep(2)
            
            if id == sword_id:
                print("You step closer and demand to know the meaning of this!")
                print("A bellow of jovial laughter ripples through the glade.")
                print("~")
                sleep(2)
                print("A giant voice speaks: 'You are very tiny! I've been waiting here for one such as yourself to release me.'")
                print("Will you hack away at the enchanted vines and save the giant? Or will you run away?")
                print("~")
                print("Choose your sword to cut the vines. Choose your horse to run away.")
                
                id, text = reader.read()
                sleep(2)
                
                if id == sword_id:
                    print("You slash and hack and fireball your way through the enchanted vines, slowly but surely releasing the giant.")
                    print("He is impressed with your work ethic and you are impressed with his puns.")
                    print("~")
                    sleep(2)
                    print("He offers you a choice: He will pick you up and place you on a safe road away from the enchanted vines. Or you can choose to join him on his travels.")
                    print("Choose the heart to join the giant. Or choose your horse to have the giant place you on a safe road.")
                    
                    id, text = reader.read()
                    sleep(2)
                    
                    if id == heart_id:
                        print("The giant plucks you and your horse up from the glade, gingerly makes his way through the vines, and your merry band carries on across this land and many others.")
                        print("~~The End~~")
                        print("This game is a collaborative project developed in the Red Rocks Community College IDEA Lab.") 
                        print("To find out more, and to keep adding to this story, drop in and write with us!")
                        sleep(3)
                        menu()
                    if id == horse_id:
                        print("The giant plucks you and your horse up from the glade and tucks you in his pockets.")
                        print("He gingerly makes his way through the vines and is out of the woods at a steady clip.")
                        print("~")
                        sleep(3)
                        print("You, your horse, and your belongings are all atumble in the giant's pockets.")
                        print("Before long, the giant picks you out of his pockets like a piece of lint and stares at you on the flat of his palm.")
                        print("~")
                        sleep(3)
                        print("'You have impressed me with your bravery, tiny traveler,' he says before placing you down in the road.")
                        print("Then he wanders off, leaving you to dust yourself off, soothe your horse, and wander around looking for entertainment.")
                        print("~")
                        sleep(2)
                        tournament()
                        
                            
                
                if id == horse_id:
                    print("You run back to your horse and jump into the saddle.")
                    print("You urge your horse to run out of the glade at a gallop.")
                    print("~")
                    sleep(3)
                    print("One of the grasping vines tangles your horse's legs and drags you both to the ground.")
                    print("You hear a mighty bellow of laughter.")
                    print("~")
                    sleep(3)
                    print("A giant explains that he has been trapped in this glade for years, and he is so happy you're here to listen to his terrible jokes.")
                    print("You wait with the giant and suffer through his bad puns for another traveler to wander down this path and free the lot of you.")
                    print("~")
                    sleep(3)
                    print("~~The End~~")
                    print("This game is a collaborative project developed in the Red Rocks Community College IDEA Lab.") 
                    print("To find out more, and to keep adding to this story, drop in and write with us!")
                    sleep(3)
                    menu()
                    
            
            if id == horse_id:
                print("You run back to your horse and jump into the saddle.")
                print("You urge your horse to run out of the glade at a gallop.")
                print("~")
                sleep(3)
                print("One of the grasping vines tangles your horse's legs and drags you both to the ground.")
                print("You hear a mighty bellow of laughter.")
                print("~")
                sleep(3)
                print("A giant explains that he has been trapped in this glade for years, and he is so happy you're here to listen to his terrible jokes.")
                print("You wait with the giant and suffer through his bad puns for another traveler to wander down this path and free the lot of you.")
                print("~")
                sleep(3)
                print("~~The End~~")
                print("This game is a collaborative project developed in the Red Rocks Community College IDEA Lab.") 
                print("To find out more, and to keep adding to this story, drop in and write with us!")
                sleep(3)
                menu()
                  
            
            
        if id == sword_id:
            print("You hack your way onto a smooth path that winds down into a valley.")
            print("At the bottom of the valley is an arena surrounded by chanting fans.")
            print("Above the valley, upon a steep hill, you glimpse the towers of a castle peeking through what appears to be a mystical fog.")
            print("~")
            sleep(3)
            print("Where will you go, traveler?")
            print("Choose your book of spells to investigate the castle. Choose your horse to see what's happening at the arena.")
            
            id, text = reader.read()
            sleep(2)
            
            if id == spell_id:
                sleep(1)
                castle()
            if id == horse_id:
                sleep(1)
                tournament()
        
       
        
def pirate_ship():
    while True:
        print("You wake to find the Captain of the pirates sitting across an unusually fine table.")
        print("She offers you a deal: 'Play me a game of Liar's Dice. Or go for a swim with the Screeching Eels.'")
        print("'If you win, you can have this sackful of gold and your freedom.")
        print("If you lose, you will stay on my ship and swab the deck until I decide you've paid your way.'")
        print("~")
        sleep(3)
        print("Which is it? Will you choose your money pouch to gamble, risking your freedom? Or will you choose your horse to make a swim for it?")
        print("~")
        
        id, text = reader.read()
        sleep(2)
        
        if id == horse_id:
            print("You nicker for your horse, who is less than happy to discover your plan to jump off the ship into eel-infested waters.")
            print("But you've kept each other alive so far and so the horse agrees to take the leap.")
            print("~")
            sleep(3)
            print("It comes as no surprise from the watching pirates that you aand your horse are quickly made into an eel-meal.")
            print("~~The End~~")
            print("This game is a collaborative project developed in the Red Rocks Community College IDEA Lab.") 
            print("To find out more, and to keep adding to this story, drop in and write with us!")
            sleep(3)
            menu()
        
        if id == pouch_id:
            print("The Captain hands you a handful of dice under a cup.")
            print("You both roll, and you peer under your cup to see the result. You end up with a pair of threes.")
            print("The Captain claims a hand of four sixes.")
            print("~")
            sleep(3)
            print("Choose your strategy. Will you try and bluff to beat the Captain's hand? Or will you call her out?")
            print("Draw your sword to try and bluff the Captain. Draw your shield to call the Captain's bluff.")
            print("~")
            
            id, text = reader.read()
            sleep(2)
            
            if id == shield_id:
                print("She reveals her dice, and all she had was a pair.")
                print("Against all odds, you end up winning.")
                print("~")
                sleep(3)
                print("She makes good on her deal. She hands you a sack of gold and drops you and your seasick horse at the nearest port.")
                print("As you climb the inland road, you can't help glancing behind as the black sails disappear over the horizon.")
                print("~")
                sleep(3)
                print("You wonder what your life could have been aboard a pirate ship.")
                sleep(3)
                print("The path curves before you, and your horse whinnies to be back on solid ground.")
                sleep(3)
                giant()
                
            
            if id == sword_id:
                print("You claim you can beat her hand.")
                print("The Captain calls your bluff.")
                print("~")
                sleep(3)
                print("Will you show her your low hand? Or will you fight?")
                print("Choose your money pouch to surrender and agree to work for the Captain. Choose your sword to fight.")
                
                id, text = reader.read()
                sleep(2)
                
                if id == sword_id:
                    print("Before you are able to fully draw your sword or your book of spells, you are struck down by the Captain and her crew.")
                    print("You chose poorly.")
                    print("~~The End~~")
                    print("This game is a collaborative project developed in the Red Rocks Community College IDEA Lab.") 
                    print("To find out more, and to keep adding to this story, drop in and write with us!")
                    sleep(3)
                    menu()
                    
                
                if id == pouch_id:
                    print("The Captain takes your weapons and hands you a mop.")
                    print("'I hope you clean better than you gamble, matey.'")
                    print("~")
                    sleep(3)
                    print("You live out your remaining years swabbing decks and singing shanties with a very fine group of pirates.")
                    print("You get better at gambling.")
                    print("But not much.")
                    print("~~The End~~")
                    print("This game is a collaborative project developed in the Red Rocks Community College IDEA Lab.") 
                    print("To find out more, and to keep adding to this story, drop in and write with us!")
                    sleep(3)
                    menu()
                
            
            
            
        
        


def test_env():
    while True:
        print("Check tag ID and mood.")
        id, text = reader.read()
        sleep(1)
        print("This tag has id: ", id)
        print('~~~~~~')
        sleep(1)
        
        
##        '''
##        if id == blue_id:
##            print("Blue Tag. My id is", id, "Leave me alone")
##            sleep(2)
##        if id == card_id:
##            print("Card My id is", id)
##            sleep(3)
##        '''

GPIO.cleanup()
menu()