class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class Armor:
    def __init__(self, name, armor):
        self.name = name
        self.armor = armor

class Potion:
    def __init__(self, name, healing):
        self.name = name
        self.healing = healing

# WEAPONS LIST
bronze_sword = Weapon("Bronze sword", 2)
iron_sword = Weapon("Iron sword", 4)
gods_fork = Weapon("Gods Fork", 999)
