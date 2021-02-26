# Write a class for all the loot in the game.

class Loot:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.name}'