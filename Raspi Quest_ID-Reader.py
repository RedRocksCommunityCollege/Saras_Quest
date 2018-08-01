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




def menu():
    while True:
        print("Welcome.")
        print("Jump on your horse to begin a quest!")
        print("Card to run diagnostics")
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
            sleep(2)
            print("A dragon lands in the road before you. Fight the dragon? Sword = yes Horse = no")
            id, text = reader.read()
            sleep(2)
            
            if id == horse_id:
                print("The dragon respects your choice. You and the dragon become friends.")
                print ("The dragon licks your face and hovers in the air above you.")
                print("~")
                sleep(3)
                dragon1()
                sleep (3)
                
            if id == sword_id: 
                print("A risky choice.")
                print ("Your horse trots to a safe distance. Good luck.")
                print("~")
                sleep(2)
                fight1()

def fight1():
    while True:
        print ("Draw your sword or cast a spell?")
        id, text = reader.read()
        print ("~")
        sleep (1)
    
        if id == sword_id:
            print ("You swing at the beast and she roars.")
            print ("She ")
            print ("~")
            sleep (1)
            print ("this is where they should make a choice")
            id, text = reader.read()
            sleep (1)
    
        #if id == spell_id
            #print ("Do you cast sleep or fireball?")
            #print ("Choose book of spells for sleep. Choose sword for fireball.")
            #print("~")
            #id, text = reader.read()
            #sleep (1)
                
        if id == blue_id:
            print ("Blue = cast sleep. Card = cast fireball")
            print("~")
            id, text = reader.read()
            sleep(2)
                    
        if id == blue_id:
            print ("You hold your breath and start to sneak past the dragon. She snorts as you pass, but you manage to squeak by.")
            sleep (1)
            print ("You continue West to the town.")
            print("~")
            sleep(3)
            town_menu()
                    
        if id == card_id:
            print ("Your fireball arcs toward the dragon and she easily dodges. She burns you to a crisp. The end.")
            sleep(2)
            menu()
                    
            if id == card_id:
                print ("Draw your sword? Blue = yes Card = no")
                id, text = reader.read()
                sleep (2)
                    
            if id == blue_id: 
                print("the dragon eats you. The end.")
                print(":(")
                sleep(4)
                menu()





def town_menu():
    while True:
        print("The roadway is soon filled with travelers heading to the market in town.")
        sleep (2)
        print ("The road forks before you.")
        print("~")
        sleep(1)
        print("Horse = take the southern road and avoid the town.")
        print("Book of Spells = continue into town.")
        print("~")
        id, text = reader.read()
    
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
        print ("Horse = stay on the road. Shield = coax the dragon into the woods.")
        print("~")
        id, text = reader.read()
        sleep(2)  
        
        if id == horse_id:
            print("Stanley bellows a bone-chilling roar and leaps into the air.")
            sleep(2)
            print ("She races toward a large wagon full of supplies for the market.")
            print ("Stanley nabs the lead drafthorse and races through the air. Soon she is out of sight. You hope she will return.")
            sleep (2)
            print("~")
            print ("You have enough money in your pouch to pay the driver for Stanley's meal, but that will leave you with little money for the market.")
            print ("Pouch = compensate the driver for the horse. Horse = continue on your way without paying the driver.")
                
            print("~")
            id, text = reader.read()
            sleep(2)
            menu()
                
                
        if id == shield_id:
            forest_thieves()
            sleep(2)

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
        print ("Shield = Raise your hands and await further instructions. Horse = point in the direction of the voice and hope Stanley takes her cue to attack the owner of the voice.")
        print("~")
        
        id, text = reader.read()
        sleep(2)  
                    
        if id == shield_id:
            menu()
                
        if id == horse_id:
            menu()
                
def town():
    while True:
        print ("The crush of people and wagons pushes you toward the market. You can smell the fresh bread and spices from here.")
        sleep (2)
        print("~")
        print ("But wait! You glimpse a darkened alley. For one tantalizing second, you spot the swinging sign of a magic shop peeking out of the shadows.")
        sleep (3)
        print("~")
        print ("Do you wish to continue to the marketplace or fight the crowd and seek out the magic shop?")
        print ("Horse = market. Book of Spells = magic shop")
        sleep (3)
        menu()
            
        print("~")
        id, text = reader.read()
        sleep(2)  
                    
        if id == horse_id:
            market()
                
        if id == spell_id:
            magic_shop()
        
def market():
    while True:
        print ("Before you are stalls for food, clothing, books, and other gear for travelers.")
        print ("If you paid for Stanley's lunch, you have 3 gold left in your pouch. If you didn't pay for her lunch, you have 10 gold to spend at market.") 
        


def magic_shop():
    while True:
        print (".")
        print("~")
        
        id, text = reader.read()
        sleep(2)  
        menu()     
      
        
        
def southern_road():
    while True:
        print (".")
        print("~")
        
        id, text = reader.read()
        sleep(2)  
        menu() 



def test_env():
    while True:
        print("Check tag ID and mood.")
        id, text = reader.read()
        sleep(1)
        print("This tag has id: ", id)
        print('~~~~~~')
        sleep(1)
        
        '''
        if id == blue_id:
            print("Blue Tag. My id is", id, "Leave me alone")
            sleep(2)
        if id == card_id:
            print("Card My id is", id)
            sleep(3)
        '''

GPIO.cleanup()
menu()