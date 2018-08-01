#import time
waiting_for_input = True
def witch():
    while waiting_for_input:
        print("Poof...Through a thick misterious cloud of smoke a witch stands before you")
        sleep(3)
        print("Witch - 'Hello there traveller it appears that your travels have lead you to me'")
        sleep(3)
        print("Please choose your next decision carefully...")
        sleep(5)
        print("Sword = Draw your trusty sword and attempt to strike down the wicked witch, Spellbook = Ask the witch her name")
        #user_choice= input("Pick...")
        id, text =reader.read()
        sleep(4)
        #if user_choice == '1':
        if id == sword_id:
            witch_attack()
        #if user_choice == '2':
        if id == spell_id:
            witch_spell()
        

def witch_attack():
    print("You have choosen to attack the witch with your trusty sword...")
    print("~")
    sleep(5)
    print("You swipe at the witch's face closing your eyes as you do because youre a coward")
    print("~")
    sleep(5)
    print("As you open your eyes you realize that the witch dodged your attack and you swung yourself to the edge of a cliff...")
    print("~")
    sleep(5)
    print("You stumble off the ledge and as you relaize you arent standing on solid ground you fall to your demise, much like in the cartoons")
    print("~")
    sleep(5)
    print("As you fall the witch uses her magic to speak to you and tell you she was once a beutiful queen who gave up her looks for magic so that she could use her powers to save her village from the evil dragon")
    print("~")
    sleep(5)
    print("You realize that had you simply not judged the witch by her apperance and asked her to tell you her story she could of helped to guide you on your quest.")
    print("~")
    sleep(5)
    waiting_for_input = False
       # user_choice = input("Will you attack the the witch? If so choose sword...")
def witch_spell():
    print("My name is Claire I was once the queen of a small village called Asgard, One day a dragon approched my village in search of gold...")
    print("~")
    sleep(5)
    print("Being a small poor town we did not have much gold and what we did have my people needed, so I pleaded with the dragon and asked if there was another way")
    print("~")
    sleep(8)
    print("Being a clever dragon he decided that he would spare my village if I was forced to walk the world forever more as a hideous witch...")
    print("~")
    sleep(8)
    print("Since then I have dedicated my life to helping others")
    print("~")
    sleep(5)
    print("I am happy to help you on your journey...")
    print("~")
    sleep(5)
    print("Horse = Ask if she will point you in the direction of the next adventure, Potion = Thank her for her time and ask if she can offer any advice for your travels. ")
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
    print("Of course young traveler thank you for speaking with me I am glad to point you on your way, follow the river through the valley, stay close to it as it will guide you through the treacherous land ahead")
    sleep(5)
    waiting_for_input = False
    print("Good luck young one...")
def witch_potion():
    print("Of course young traveler thank you for speaking with me I am glad to offer you some advice, I can offer you meny things I have learned in my travels however perhapse the most important is to be honorable and pay what must be payed...")
    sleep(5)    
    waiting_for_input = False


witch()
print("On to your next adventure...")