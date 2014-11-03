#Blue is just hypothetical objects….did not have enough time to do error catching 
#but this code should help us create rooms, connections, verbs, 
#items (still working on adding verbs/items)
f
class Room(object):
    """Here, we are creating one room with items, verbs, and room
    connections maybe..."""

    def __init__(self,name,description,number):
        self.items = []
        self.verbs = []
        self.connections = []
        self.name = name
        self.number = number
        self.description = description

    def __str__(self):
        return self.name

    def get_description():
        return self.description

    def get_number():
        return self.number

    def get_name():
        return self.name

    def get_items():
        return self.items

    def get_verbs():
        return self.verbs

    def add_item(item_name):
        self.items.append(item_name)

    def add_verbs(action):
        self.verbs.append(action)


class GameMap(object):
    """Here we have our game map, which contains a game and
    the various connections in that game"""

    #if -1, then that means you cannot go to room
    #if >0, then that means you connect to that given room

    def __init__(self, game,rooms):
        self.map = []
        self.rooms = []
        self.game = game

    def add_connections(self):
        for r in self.rooms:
            self.map.append(r.connections)

    def get_map():
        return self.map

    def get_game():
        return self.game

class Game(object):

    def __init__(self,name):
        self.name = name
        self.player = None
        self.moves = 0
        self.score = 0
        self.available_verbs = []

    def increment_moves():
        self.moves = self.moves + 1

    def increment_score(points_worth):
        self.score = self.score + points_worth


class Player(object):
    def __init__(self,name):
        self.name = name
        self.inventory = []


class Item(object):

    def __init__(self,name,description):
        self.name = name
        self.description = description

def make_game():
    """Here we will have our user define his/her game"""

    print("""Hey there! We are going to ask you a few questions to
          to create your text-based adventure game. Please be sure to
          have your room connections, items, and actions already
          in mind.""")

    game_name = input("First off, what is your game's name?")
    #here we will create the game...just created a mock game object,
    #we can change it all later
    game = Game(game_name)

    #or should we have you two make this?
    player_name = input("What is your player's name? If none, type 'no name'")
    player = Player(player_name)

    #need to handle errors...
    number_of_rooms = int(input("How many sections/rooms/areas do you have?"))
    all_rooms = make_rooms(number_of_rooms) #we create the rooms
    all_rooms = add_room_connections(all_rooms) #we add connections to the rooms

    map_of_game = GameMap(game, all_rooms)
    map_of_game.add_connections()



def make_rooms(number_of_rooms):
    rooms = []
    for i in range(number_of_rooms):
        fix = True
        while fix==True:
            room_name = input("What is an area's name?")
            room_description = input("""Please write the text you want
                                         your player to see when
                                         he/she enters""")
            print(room_name, room_description)
            correction = input("Is this correct?")
            if handle_human_input(correction) is True:
                fix = False
            rooms.append(Room(room_name, room_description,i))
    return rooms

#obviously need to handle for 'y' or 'yes' etc
def handle_human_input(human_input):
    if human_input=='y':
        return True
    else:
        return False

def add_room_connections(list_of_rooms):
    directions = ["north", "south", "east", "west",
                  "northeast", "northwest", "southeast",
                  "southwest", "up", "down", "in", "out"]
    for room in list_of_rooms:
        for d in directions: #go through all directions
            print("Is there a room connected to", room, "'s", d)
            connection = input("Please type y for yes or n for no")
            if handle_human_input(connection)==False:
                room.connections.append(-1) #-1 means no connection
            else:
                print_list_of_all_rooms(list_of_rooms)
                room_connected = input("Which room is connected to this room?")
                room.connections.append(find_connection(list_of_rooms,room_connected))
    return list_of_rooms

def print_list_of_all_rooms(list_of_rooms):
    for r in list_of_rooms:
        print(r.name)

#need to account for room not included..
def find_connection(list_of_rooms, name):
    for r in list_of_rooms:
        if r.name==name:
            return r.number

make_game()
