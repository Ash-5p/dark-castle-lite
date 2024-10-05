import random

class Character:
    """
    Character class
    """
    def __init__(self, name, might, wisdom, cunning, item):
        #properties
        self.name = name
        self.might = might
        self.wisdom = wisdom
        self.cunning = cunning
        self.item = item

    def description(self):
        """
        Display character stats
        """
        return f"Might: {self.might} / Wisdom: {self.wisdom} / Cunning: {self.cunning}"

fighter = Character("Fighter", 3, 2, 1, "None")
scholar = Character("Scholar",1, 3, 2, "None")
thief = Character("Thief",2, 1, 3, "None")

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

ITEMS = ["Chainmail", "Spiked Gloves", "Hooded Cloak", "Lexicon", "Apple", "Focusing Crystal"]