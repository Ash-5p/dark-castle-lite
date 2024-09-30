class Character:
    """
    Character class
    """
    def __init__(self, might, wisdom, cunning, item):
        #properties
        self.might = might
        self.wisdom = wisdom
        self.cunning = cunning
        self.item = item

    def description(self):
        """
        Display character stats
        """
        return f"Might: {self.might} / Wisdom: {self.wisdom} / Cunning: {self.cunning}"

fighter = Character(3, 1, 2, "none")
scholar = Character(1, 3, 2, "none")
thief = Character(2, 1, 3, "none")
