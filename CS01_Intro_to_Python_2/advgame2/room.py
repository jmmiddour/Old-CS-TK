# Implement a class to hold room information.
# This should have name and description attributes.

class Room:
    def __init__(self, name, description, inventory=None):
        if inventory is None:
            inventory = []
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.inventory = inventory

    def __repr__(self):
        return f'{self.inventory}'

    def remove_item(self, item):
        self.inventory.pop(item)

    def add_item(self, item):
        self.inventory.append(item)
