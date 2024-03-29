import items
import enemies

# CLASSES
# --------------------
# This class defines all of the attributes of the player.
# They have a name, health, mana, attack power, and defense.
class Player:
    def __init__(self, name, max_health, current_health, attack, defense, level, experience, armor, weapon, gold, next_level):
        self.name = name
        self.max_health = max_health
        self.current_health = current_health
        self.attack = attack
        self.defense = defense
        self.level = level
        self.experience = experience
        self.armor = armor
        self.weapon = weapon
        self.gold = gold
        self.next_level = next_level


# GLOBAL PLAYER INVENTORY SEX
inventory = []



# GAME LOOP
# --------------------
def game_loop(): # Defines what's inside of the game loop.
    player = get_player() # Global variables are usually a no-no butt-fuck-it.

    while(1):
        # This is the game loop. The game will always be running in this infinite loop.
        load_town()


# FUNCTION SPANK BANK
# --------------------
def get_player(): # Defines an introductory function to get the player's name and set up an object for them
    global player
    name = input("Welcome to the game. Please enter your name: ") # Gets the user's input
    player = Player(name, 10, 10, 2, 2, 1, 0, "Rags", "Stick", 10, 20)
    return player

def load_town():
    print("Welcome to the town, " + player.name + "!")
    user_input = input("What would you like to do?\n")
    add_item(items.iron_sword)


# This function will let you add an item to a player's inventory
def add_item(item):
    inventory.append(item)

# main post battle function
def post_battle():
    def level_up():  # function to specifically level up after battle
        while player.experience >= player.next_level:
            player.attack += 2
            player.max_health += 5
            player.defense += 2
            player.level += 1
            player.experience = player.experience - player.next_level
            player.next_level = round(player.next_level * 1.5)

        print("You are now level", player.level)
        print("Current exp:", player.experience)
        print("Next level at", player.next_level, "exp.")
        print("Your attack and defense are now:", player.attack, "and", player.defense)

    level_up()

    
        
game_loop() # Calls the game loop function in order to start the program.
