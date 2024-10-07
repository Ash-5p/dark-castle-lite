import random

class Character:
    """
    Character class
    """
    def __init__(self, name, health, might, wisdom, cunning, item, mirror):
        #properties
        self.name = name
        self.health = health
        self.might = might
        self.wisdom = wisdom
        self.cunning = cunning
        self.item = item
        self.mirror = mirror # Becomes true if player selects (n) on chapter_3a

    def description(self):
        """
        Display character stats
        """
        return f"Might: {self.might} | Wisdom: {self.wisdom} | Cunning: {self.cunning}"
    
    def return_highest_stat(self):
        """
        Returns the name of the highest stat out of Might, Wisdom & Cunning
        """
        highest_value = max(self.might, self.wisdom, self.cunning)
        if self.might == highest_value:
            return "Might"
        elif self.wisdom == highest_value:
            return "Wisdom"
        else:
            return "Cunning"


fighter = Character("Fighter", 60, 9, 6, 3, "None", False)
scholar = Character("Scholar", 60, 3, 9, 6, "None", False)
thief = Character("Thief", 60, 6, 3, 9, "None", False)

characters = [fighter, scholar, thief]

class Enemy:
    """
    Enemy class
    """
    def __init__(self, name, health, nature, min_damage, max_damage, boss):
        #properties
        self.name = name
        self.health = health
        self.nature = nature
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.boss = boss

    def get_random_damage(self):
        """
        Returns a randomized damage value between the set min and max damage.
        """
        return random.randrange(self.min_damage, self.max_damage + 1)

    def description(self):
        """
        Display enemy stats
        """
        return f"HP: {self.health} / Nature: {self.nature}"

guard = Enemy("Guard", 30, "Might", 3, 5, False)
spirit = Enemy("Enraged Spirit", 36, "Wisdom", 3, 7, False)
sludge_creature = Enemy("Sludge Creature", 42, "Cunning", 3, 6, False)
beast = Enemy("Beast Man", 42, "Might", 5, 10, False)


ITEMS = {
    "Chainmail": "Reduces damage taken by 2 while held",
    "Spiked Gloves": "Increases Might by 3 while held", 
    "Hooded Cloak": "Increases Cunning by 3 while held", 
    "Lexicon": "Increases Wisdom by 3 while held", 
    "Apple": "Use in battle to restore +25hp (Consumed when used)", 
    "Focusing Crystal": "Increase accuracy of attacks by 10%", 
    "Throwing Knife": "Use in battle to inflict 15 damage to current enemy (Consumed when used)",
    "Mirror Film": "Allows the guaranteed escape from combat (Consumed when used)"
    }
