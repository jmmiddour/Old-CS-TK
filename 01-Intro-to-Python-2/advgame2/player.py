# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def _init_(self, name, curr_room, inventory=[]):
        # if inventory is None:
        #     inventory = []
        self.name = name
        self.curr_room = curr_room
        self.inventory = inventory

    def remove_item(self, item):
        self.inventory.remove(item)

    def add_item(self, item):
        self.inventory.append(item)