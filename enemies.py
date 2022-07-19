# This class defines all of the attributes of any given enemy.
# They have a name, health, mana, attack power, and defense.
class Enemy:
    def __init__(self, name, max_health, current_health, attack, defense):
        self.name = name
        self.max_health = max_health
        self.current_health = current_health
        self.attack = attack
        self.defense = defense
        
# ORDER: name, max health, current health, attack, defense
slime = Enemy("slime", 10, 10, 1, 1)