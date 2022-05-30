import time
import random

def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)

def intro(monster):
    print_pause("You find yourself standing in an open field, "
    "filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a wicked " + monster + " is somewhere "
    "around here, and has been terrorizing the nearby village.")

def valid_input(prompt, option1, option2):
    while True:
        response = str(input(prompt))
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_pause("Please choose 1 or 2")
    return response

def field(items, weapon, monster):
    print_pause("In front of you is a small house.")
    print_pause("To your right is a dark cave.")
    if weapon in items:
        print_pause("You are now armed with a " + weapon + ".")
    else:
        print_pause("The only item in your possession is a rusty lantern.")
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to enter the cave.")
    response = valid_input("What would you like to do? "
    "Please enter 1 or 2. \n", '1', '2')
    if response == '1':
        house(items, weapon, monster)
    if response == '2':
        cave(items, weapon, monster)

def house(items, weapon, monster):
    print_pause("You knock on the door...")
    print_pause("And the " + monster + " pops out!")
    if weapon not in items:
        print_pause("The only thing you have to defend yourself with is "
        "your lantern...")
    print_pause("Enter 1 to fight!")
    print_pause("Enter 2 to run away!")
    response = valid_input("What would you like to do? "
    "Please enter 1 or 2. \n", "1", "2")
    if response == "1":
        fight(items, weapon, monster)
    if response == "2":
        print_pause("You bravely turned your tail and fled...")
        print_pause("Thankfully you weren't followed!")
        print_pause("You are back in the field.")
        field(items, weapon, monster)

def cave(items, weapon, monster):
    print_pause("You peer into the dark cave...")
    print_pause("It is pitch black. You are likely to be eaten by a grue.")
    print_pause("Enter 1 to turn on your lantern.")
    print_pause("Enter 2 to leave the cave.")
    response = valid_input("What would you like to do? "
    "Please enter 1 or 2. \n", "1", "2")
    if response == "1":
        if weapon in items:
            print_pause("All you can see is the now-empty treasure chest.")
            print_pause("You return to the field.")
            field(items, weapon, monster)
        else:
            get_weapon(items, weapon)
            field(items, weapon, monster)
    if response == "2":
        field(items, weapon, monster)

def fight(items, weapon, monster):
    if weapon in items:
        print_pause("You use your mighty " + weapon + "...")
        print_pause("And defeat the " + monster + "!")
        print_pause("Congratulations, you've won the game!")
        play_again(items, weapon, monster)
    else:
        print_pause("You have no weapons and are powerless against the fearsome " + monster + ".")
        print_pause("It strikes you down easily.")
        print_pause("You have been defeated.")
        play_again(items, weapon, monster)

def get_weapon(items, weapon):
    print_pause("By the light of the lantern, you see a treasure chest!")
    print_pause("You open the treasure chest...")
    print_pause("And find a shining " + weapon + " inside!")
    print_pause("You add it to your inventory and return to the field.")
    items.append(weapon)

def play_again(items, weapon, monster):
    print_pause("Would you like to play again?")
    print_pause("Enter 1 for yes.")
    print_pause("Enter 2 for no.")
    response = valid_input("Please enter 1 or 2.\n", "1", "2")
    if response == "1":
        intro(monster)
        field(items, weapon, monster)
    if response == "2":
        print("Goodbye.")
    
def play_game():
    monsters = ["troll", "dragon", "goblin", "demon", "warlock"]
    monster = random.choice(monsters)

    weapons = ["broadsword", "battle axe", "scythe", "flail", "spear"]
    weapon = random.choice(weapons)

    items = []
    intro(monster)
    field(items, weapon, monster)
    play_again()

play_game()