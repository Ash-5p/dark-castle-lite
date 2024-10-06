import random

class Character:
    """
    Character class
    """
    def __init__(self, name, health, might, wisdom, cunning, item):
        #properties
        self.name = name
        self.health = health
        self.might = might
        self.wisdom = wisdom
        self.cunning = cunning
        self.item = item

    def description(self):
        """
        Display character stats
        """
        return f"Might: {self.might} / Wisdom: {self.wisdom} / Cunning: {self.cunning}"

fighter = Character("Fighter", 20, 3, 2, 1, "None")
scholar = Character("Scholar", 20, 1, 3, 2, "None")
thief = Character("Thief", 20, 2, 1, 3, "None")

class Enemy:
    """
    Enemy class
    """
    def __init__(self, name, health, nature, damage):
        #properties
        self.name = name
        self.health = health
        self.nature = nature
        self.damage = damage

    def description(self):
        """
        Display enemy stats
        """
        return f"HP: {self.health} / Nature: {self.nature}"

guard = Enemy("Guard", 10, "Might", 2)
spirit = Enemy("Spirit", 12, "Wisdom", random.randrange(1,3))
sludge_creature = Enemy("Sludge Creature", 14, "Cunning", random.randrange(1,2))

ITEMS = {
    """
    Dictionary of items and their descriptions
    """
    "Chainmail": "Reduces damage taken by 1 while held",
    "Spiked Gloves": "Increases Might by 1 while held", 
    "Hooded Cloak": "Increases Cunning by 1 while held", 
    "Lexicon": "Increases Wisdom by 1 while held", 
    "Apple": "Use in battle to restore +10hp", 
    "Focusing Crystal": "Increase accuracy of attacks by 10%", 
    "Throwing Knife": "Use in battle to inflict 10 damage to current enemy"
    }