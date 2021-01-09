# Import classes from other files
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

# Declare all the rooms in the game
room = {
    'outside':  Room('Outside Cave Entrance',
                     'North of you, the cave mount beckons',
                     [loot['knife'], loot['potion'], loot['lumens']]),
    'foyer':    Room('Foyer', '''Dim light filters in from the south. \n
                     Dusty passages run north and east.''',
                     [loot['plant'], loot['amulet']]),
    'overlook': Room('Grand Overlook',
                     '''A steep cliff appears before you, falling into the darkness. \n
                     Ahead to the north, a light flickers in the distance, \n
                     but there is no way across the chasm.''',
                     [loot['flagon'], loot['staff']]),
    'narrow':   Room('Narrow Passage',
                     '''The narrow passage bends here from west to north.\n 
                     The smell of gold permeates the air.''',
                     [loot['bomb'], loot['food']]),
    'treasure': Room('Treasure Chamber',
                     """You’ve found the long-lost treasure chamber! \n
                     Sadly, it has already been completely emptied by earlier adventurers. \n
                     The only exit is to the south.""",
                     [loot['gold'], loot['plant'], loot['flagon']]),
}
# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# ######### Main ######## #
# Make a new player object that is currently in the ‘outside’ room.
name = str(input('Player name: ').title())
player_name = Player(name, room['outside'])
player_movement = None
current_room = None

# Write a loop that:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# # * Waits for user input and decides what to do.
while player_movement != 'q':

    if current_room == player_name.curr_room:
        pass

    else:
        current_room = player_name.curr_room

    print(f'{player_name.name} has arrived at: {current_room.name}. {current_room.description}')

    player_movement = input('There are doors in the cardinal directions. Which do you choose? ')

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn’t allowed.
    if player_movement.lower() in ['n', 's', 'e', 'w', 'a', 'q']:

        if player_movement.lower() == 'n':
            current_room = current_room.n_to

        elif player_movement.lower() == 's':
            current_room = current_room.s_to

        elif player_movement.lower() == 'e':
            current_room = current_room.e_to

        elif player_movement.lower() == 'w':
            current_room = current_room.w_to

        elif player_movement.lower() == 'a':
            look_drop = input('What would you like to do? l (look around) or d (drop item): ')

            if look_drop.lower() == 'l':
                print(f'{name} sees {player_name.curr_room.inventory}')
                pickup = input('Would you like to pick up an item? y or n: ')

                if pickup.lower() == 'y':
                    item_pu = int(input('Which item would you like? type the number: '))
                    # current_room.remove_item(item_pu - 1)
                    # player_name.add_item(item_pu)
                    player_name.add_item(current_room.remove_item(item_pu - 1))

        elif player_movement.lower() == 'q':
            quit()

        if current_room is None:
            print('You cannot pass!!')

        elif current_room == player_name.curr_room:
            print('You are already there...')

        else:
            player_name.curr_room = current_room

    else:
        print('You have chosen poorly...')
# If the user enters “q”, quit the game.
