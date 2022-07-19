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
# level 1-5 enemies
# -----------------
slime = Enemy("slime", 5, 5, 1, 1)
goblin = Enemy("goblin", 10, 10, 3, 3)
zombie = Enemy("zombie", 15, 15, 5, 5)
ogre = Enemy("ogre", 20, 20, 7, 7)
golem = Enemy("golem", 25, 25, 10, 10)
demon = Enemy("demon", 30, 30, 15, 15)  # mini boss

# level 6-10 enemies
# ------------------
banshee = Enemy("banshee", 35, 35, 17, 17)
ghoul = Enemy("ghoul", 40, 40, 20, 20)
skeleton_warrior = Enemy("skeleton warrior", 45, 45, 23, 23)
bone_bird = Enemy("bone bird", 50, 50, 25, 25)
faceless_entity = Enemy("faceless entity", 55, 55, 26, 26)
splitter = Enemy("splitter", 60, 60, 30, 30)
reaper = Enemy("reaper", 80, 80, 40, 40) # boss
