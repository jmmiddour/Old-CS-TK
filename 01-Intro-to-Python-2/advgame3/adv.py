from room import Room
from player import Player
from loot import Loot

# Declare all the loot in the game
loot = {
    'knife': Loot('Mac the Knife', 'A rusty blade.'),
    'flagon': Loot('Magnificent Drinking Vessel',
                   'Alas, it appears to be empty.'),
    'gold': Loot('The One Piece', 'Mysterious pirate gold.'),
    'staff': Loot('The Staff of Egypt',
                  'A beautiful work of art, this wooden staff has a carving of Anubis at the top.'),
    'lumens': Loot('Bioluminescence',
                   'The reflection of shiny faces.'),
    'bomb': Loot('Remote Bomb', 'Can be activated two at a time.'),
    'plant': Loot('Strange Leafy Green Plant',
                  'Perhaps it can be smoked?'),
    'food': Loot('Gluten-Free', 'Too bad, it is just granola.'),
    'potion': Loot('Healing Potion', 'This potion will restore your health to 100%.'),
    'amulet': Loot('Amulet of Kvasir', 'Dodge oncoming enemies.'),
}

# Declare all the rooms
room = {
    'outside':  Room('Outside Cave Entrance',
                     '  North of you, the cave mount beckons.',
                     [loot['knife'], loot['potion'], loot['lumens']]),
    'foyer':    Room('Foyer', '''  Dim light filters in from the south.
  Dusty passages run north and east.''',
                     [loot['plant'], loot['amulet']]),
    'overlook': Room('Grand Overlook',
                     '''  A steep cliff appears before you, falling into the darkness.
  Ahead to the north, a light flickers in the distance,
    but there is no way across the chasm.''',
                     [loot['flagon'], loot['staff']]),
    'narrow':   Room('Narrow Passage',
                     '''  The narrow passage bends here from west to north.
  The smell of gold permeates the air.''',
                     [loot['bomb'], loot['food']]),
    'treasure': Room('Treasure Chamber',
                     '''  You’ve found the long-lost treasure chamber!
  Sadly, it has already been completely emptied by earlier adventurers.
  The only exit is to the south.''',
                     [loot['gold'], loot['plant'], loot['flagon']]),
}

# Link rooms together
room['outside'].n_to= room['foyer']
room['foyer'].s_to= room['outside']
room['foyer'].n_to= room['overlook']
room['foyer'].e_to= room['narrow']
room['overlook'].s_to= room['foyer']
room['narrow'].w_to= room['foyer']
room['narrow'].n_to= room['treasure']
room['treasure'].s_to= room['narrow']

# ######### Main ######## #

# Make a new player object that is currently in the 'outside' room.
name = input("Player name: ").title()
player = Player(name, room['outside'])
movement = None
current_room = None

# Welcome the user to the game
print(f'''
\nHello, {name}!\nWelcome to a fun-filled game of adventure.
  Valid Inputs:\n    To go North: type "n"\n    To go South: type "s"
    To go East: type "e"\n    To go West: type "w"
    To preform an action while in a location: type "a"\n    If Yes: type "y"
    If No: type "n"\n    If you want to quit the game: type "q"
''')

# Write a loop that:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
while movement != "q":
    if current_room == player.curr_room:
        pass

    else:
        current_room= player.curr_room

    print(f"{player.name} is has arrived: {current_room.name}. {current_room.description}")

    movement = input('''What would you like to do now?
Go North (n), Go South (s), Go East (e), Go West (w), Action (a) or Quit (q): ''')

    # If the user enters a cardinal direction,
    #   attempt to move to the room there.
    if movement.lower() in ["n", "s", "e", "w", "q", "a"]:

        if movement.lower() == "n":
            current_room= current_room.n_to

        elif movement.lower() == "s":
            current_room= current_room.s_to

        elif movement.lower() == "e":
            current_room= current_room.e_to

        elif movement.lower() == "w":
            current_room= current_room.w_to

        elif movement.lower() == "a":
            look_drop = input("what would you like to do: l or d ")

            if look_drop.lower() == 'l':
                print(f"{player.name} sees {player.curr_room.inventory}")
                pick_up = input("would you like to pick up an item? y or n ")

                if pick_up.lower() == 'y':
                    item_pu = input('Which item would you like? type the number: ')
                    current_room.remove_item(item_pu)
                    player.add_item(item_pu)
                    # player.add_item(current_room.remove_item(item_pu - 1))

        # If the user enters "q", quit the game.
        elif movement.lower() == "q":
            quit()

        # Print an error message if the movement isn't allowed.
        if current_room is None:
            print("You cannot pass!")
        elif current_room == player.curr_room:
            print("You are already where you want to be")
        else:
            player.curr_room = current_room

    else:
        print("You have chosen poorly...")

#

#
