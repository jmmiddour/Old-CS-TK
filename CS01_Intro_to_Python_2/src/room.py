# Implement a class to hold room information. 
# This should have name and description attributes.

from item import Item


class Room:
    def __init__(self, name, description, inventory=None):
        self.name = name
        self.description = description
        self.inventory = inventory
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def remove_item(self, item):
        self.inventory.pop(item)

    def add_item(self, item):
        self.inventory.append(item)

    def __repr__(self):
        return f'{self.inventory}'
