# File to save outcome

outcome_file = "adventure_outcome.txt"

def save_outcome(outcome):
    #Save the outcome of the game to a file
    with open(outcome_file, "a") as f:
        f.write(f"{outcome}\n")

def read_outcome():
    #Read and display outcomes
    print("\n----- Past Adventure Outcomes -----")
    with open(outcome_file, "r") as f:
        print(f.read())



# Cave Path (Door 1)

def door_1():
    print("\nYou push open the stone door and descend into a dark cave.\n" \
    "A faint torch flickers in the distance, and a tunnel stretches in the dark.\n")

    choice = input("Do you take the torch or go in the dark?\n\n"\
                "To Grab the torch type 'torch'\n"\
                "To continue in the dark type 'dark'\n\n")
    
    if choice == "torch":
        treasure_chamber()
    elif choice == "dark":
        print("You stumble in the darkness and fall into a deep pit")
        save_outcome("Player fell in a pit and was unable to escape.")
    else:
        print("Confused, you sit in the dark until your adventure fades away")
        save_outcome("Player gave up in the cave")

# Treasure chamber within the cave
def treasure_chamber():

    print("\nThe torch lights the way to a hidden treasure chamber. \n"\
        "A massive chest gleams in the center of the room.\n\n")
    
    choice = input("Do you open the chest or leave it alone?\n\n"\
                "To Grab the torch type 'open'\n"\
                "To continue in the dark type 'leave'\n\n")
    
    if choice == "open":

        print("Inside the chest lies gold and jewls beyond imagination.\n" \
        "But as you touch them, a curse binds you to the chest left to wander the cave forever.")

        save_outcome("The player has been cursed and is forced to wander the cave forever.")
    
    elif choice == "leave":

        print("You resist the urge to open the chest and leave it closed.\n"
            "A hidden exit reveals itself, and you escape safely.")
        
        save_outcome("Play escaped the cursed cave safely.")

    else:
        print("You hesitate too long and the chamber collapses. You barely escape.")
        
        save_outcome("Player barely escaped the collapsing treasure chamber.")




# Meadow Path (Door 2)
def door_2():
    print("\nAs you step into a glowing meadow you begin to see a village appear in the distance.\n" \
    "An old woman appears infront of you and offers you one of two items: a sword or a shield\n\n")

    choice = input("Do you take the sword, shield, or refuse?\n\n"\
                "To grab the sword type 'sword'\n"\
                "To grab the shield type 'shield'\n"\
                "To refuse the offer and continue forward type 'refuse'\n")
    
    if choice == "sword":
        dragon_battle("sword")

    elif choice == "shield":
        dragon_battle("shield")

    elif choice == "refuse":
        print("You refuse the strange ladies gifts. Suddenly, a dragon burns the medow.\n" \
        "You barely escape with your life leaving the medow")

        save_outcome("Player refused item and barely survived the dragon.")

    else:
        print("The woman suddenly vanishes, leaving you alone in the meadow. Nothing happens")

        save_outcome("The player wasted their chance in the meadow")

# Dragon battle
def dragon_battle(weapon):
        if weapon == "sword":
            print("\nThe sword glows in your hand as a dragon swoops down.\n" \
            "You strike true, slaying the beast! The villagers towards you from a distance and hail you as their hero\n")

            choice = input("Do you help the villagers or keep the dragon's treasure and leave.\n\n"\
                    "To help the villagers type 'help'\n"\
                    "To keep the dragons treasure type 'keep'\n")

            if choice == "help":
                print("\nYou help rebuild the village.\n" \
                "Your name is remembered in songs and stories for centuries.")

                save_outcome("Player has become a beloved hero with the sword")
            
            elif choice == "keep":
                print("You hoard the dragon's treasure. Rich and feared, but forever alone.")
                
                save_outcome("Player became a greedy ruler with the sword")
            
            else:
                print("You hesitate, and the treasure vanishes. You return empty handed.")

                save_outcome("Player lost the dragon's treasure by hesitating")

        elif weapon == "shield":
            print("\nThe dragon attacks, but your shield holds strong.\n" \
            "The beast grows tired and flies away. The villagers call you wise")

            save_outcome("Player survived the dragon with the shield.")


# Library Path (Crawl space)
def crawlspace():
    print("\nYou crawl through the narrow passage and enter a vast library.\n" \
    "Books whisper around you, and one glowing book floats in the air.\n")

    choice = input("Do you read the book or ignore it?\n\n"
                "To read the book type 'read'\n"\
                "To ignore the book type 'ignore'\n").lower()

    if choice == "read":
        wizard_path()
    elif choice == "ignore":
        print("You ignore the book. Suddenly, the library colapses!\n" \
        "You barely escape alive.")

        save_outcome("Player hesitated and lost the magic book")
    
    else:
        print("The book fades into dust, leaving you with nothing.")
        save_outcome("Player hesitated and lost the magic book.")


def wizard_path():
    print("\nThe book grants you powerful magic! Two portals appear:\n" \
    "One burns with fire, the other shimmers with water.\n\n")

    choice = input("Do you enter the fire portal or water portal?\n\n" 
    "To enter the portal of fire type 'fire'\n"
    "To enter the portal of water type 'water'\n")

    if choice == "fire":
        print("You enter the realm of flames. A fire demon towers before you.\n" \
        "Despite your magic, it consumes you. Your legend ends in fire.")

        save_outcome("Player was defeated by the fire demon")
    
    elif choice == "water":
        print("You dive into the water portal and emerge in a shining underwater city.\n" \
        "The people crown you as their ruler. You live forever as their king/queen.")

        save_outcome("Player become ruler of the Water Kingdom")
    
    else:
        print("Both portals close, trapping you in a void between worlds.")
        
        save_outcome("Player was trapped between dimensions.")




# Game Loop
def start_adventure():
    print("Welcome to the Lost Kingdom of Avelora!\n")
    name = input("What is your name, adventurer? ")
    print(f"Greetings, {name}! Your journey is about to begin...\n")

    playing = True
    while playing:
        print("You stand at the entrance of the ruins.\n"
            "Before you stand 3 doors:\n\n"
            "1. A dark stone door leading underground.\n"
            "2. A golden archway leading to a meadow.\n"
            "3. A crawlspace leading into darkness.\n")

        choice = input("What door would you like to choose?\n\n"
                    "For door 1 type '1'\n"
                    "For door 2 type '2'\n"
                    "For door 3 type 'crawl'\n\n")
        
        if choice == "1":
            door_1()
        elif choice == "2":
            door_2()
        elif choice == "crawl":
            crawlspace()
        else:
            print("Unable to decide, you wander away form the ruins. Your adventure ends")
            save_outcome("player walked away from Avelora without adventure.")

        again = input("\nWould you like to play again? (yes/no)").lower()
        if again != "yes":
            playing = False

    print("\nThanks for playing!")
    read_outcome()

# main
if __name__ == "__main__":
    start_adventure()