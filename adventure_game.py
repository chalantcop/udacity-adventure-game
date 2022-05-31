import time
import random

def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)

def intro():
    print_pause("You are an adventurer on a quest to slay the fearsome " 
    + monster + " of legend.")
    print_pause("After travelling for many days and nights, you find yourself "
    "in an open field.")

def valid_input(prompt, options):
    while True:
        try:
            response = str(input(prompt))
        except NameError:
            print_pause("Please choose 1 or 2.")
            continue
        if response in options:
            return response
        else:
            print_pause("Please choose 1 or 2.")
    
def field(items):
    print_pause("In front of you is a dilapidated tower.")
    print_pause("To your right is a dark cave.")
    if weapon in items:
        print_pause("You are now armed with a " + weapon + ".")
    else:
        print_pause("The only item in your possession is a rusty lantern.")
    print_pause("Enter 1 to investigate the tower.")
    print_pause("Enter 2 to investigate the cave.")
    response = valid_input("What would you like to do? "
    "Please enter 1 or 2. \n", ['1', '2'])
    if response == '1':
        tower(items)
    if response == '2':
        cave(items)

def tower(items):
    print_pause("You climb the crumbling steps...")
    print_pause("And find the " + monster + " at the top of the tower!")
    if weapon not in items:
        print_pause("The only thing you have to defend yourself with is "
        "your lantern...")
    print_pause("Enter 1 to fight!")
    print_pause("Enter 2 to run away!")
    response = valid_input("What would you like to do? "
    "Please enter 1 or 2. \n", ['1','2'])
    if response == "1":
        fight(items)
    if response == "2":
        print_pause("You bravely turned your tail and fled down the stairs...")
        print_pause("Thankfully you weren't followed!")
        print_pause("You are back in the field.")
        field(items)

def cave(items):
    print_pause("You peer into the dark cave...")
    print_pause("It is pitch black. You are likely to be eaten by a grue.")
    print_pause("Enter 1 to turn on your lantern.")
    print_pause("Enter 2 to leave the cave.")
    response = valid_input("What would you like to do? "
    "Please enter 1 or 2. \n", ['1','2'])
    if response == "1":
        if weapon in items:
            print_pause("All you can see is the now-empty treasure chest.")
            print_pause("You return to the field.")
            field(items)
        else:
            get_weapon(items)
            field(items)
    if response == "2":
        field(items)

def fight(items):
    if weapon in items:
        print_pause("You use your mighty " + weapon + "...")
        print_pause("And defeat the " + monster + "!")
        print_pause("Congratulations, you've won the game!")
        play_again()
    else:
        print_pause("You have no weapons and are powerless against the fearsome " + monster + ".")
        print_pause("It strikes you down easily.")
        print_pause("You have been defeated.")
        play_again()

def get_weapon(items):
    print_pause("By the light of the lantern, you see a treasure chest!")
    print_pause("You open the treasure chest...")
    print_pause("And find a shining " + weapon + " inside!")
    print_pause("You add it to your inventory and return to the field.")
    items.append(weapon)

def play_again():
    print_pause("Would you like to play again?")
    print_pause("Enter 1 for yes.")
    print_pause("Enter 2 for no.")
    response = valid_input("Please enter 1 or 2.\n",['1','2'])
    if response == "1":
        items = []
        intro()
        field(items)
    if response == "2":
        print("Goodbye.")
        exit()

monsters = ["troll", "dragon", "goblin", "demon", "warlock"]
monster = random.choice(monsters)
weapons = ["broadsword", "battle axe", "scythe", "flail", "spear"]
weapon = random.choice(weapons)
items = []

def play_game():
    intro()
    field(items)
    play_again()

play_game()