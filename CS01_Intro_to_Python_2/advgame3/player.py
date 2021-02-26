# Write a class to hold player information,
# e.g. what room they are in currently.

class Player:
    def __init__(self, name, curr_room, inventory=None):
        if inventory is None:
            inventory = []
        self.name = name
        self.curr_room = curr_room
        self.inventory = inventory

    def remove_item(self, item):
        self.inventory.pop(item)

    def add_item(self, item):
        self.inventory.append(item)

    def __repr__(self):
        return f'{self.inventory}'