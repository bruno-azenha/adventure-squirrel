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
        self.complete = False
    
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
    
    def change_name_and_description(self,new_name, new_d):
        self.name = new_name
        self.description = new_d
    
    def change_connections(self, d_list):
        self.connections = d_list
        self.complete= True
    

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
    
    #now we will create rooms
    create_rooms()
    
def create_rooms():
    #create the first room
    print("""Let's create our rooms! You will be able to generate a room and
          its connections. You can also create a room when you are defining
          room connections. However, you will only be able to create that room's
          name and description, and not define its connections. This way you
          cannot get lost while creating rooms.
          """)
    
    rooms = create()
    
    rooms = find_missing_rooms(rooms)
    rooms = final_check(rooms)
    
    print("You created all the rooms!")

def create():
    rooms = []
    name, description = room_name_and_description()
    rooms.append(Room(name, description,0))
    
    rooms = create_connections(rooms,0)
    
    #edit rooms
    cont = True
    while cont==True:
        create_room = input("""Do you want to create a room?
                            Type y for yes and n for no""")
        if handle_human_input(create_room) is True:
            #create a room and its connections
            name, description = room_name_and_description()
            rooms.append(Room(name,description,len(rooms)))
            rooms = create_connections(rooms, len(rooms)-1)
        edit_room = input("""Do you want to edit a room?
                          Type  y for yes and n for no""")
        if handle_human_input(edit_room) is True:
            #edit a room name and its connections...
            print_list_of_all_rooms(rooms)
            room_name = input("Which room do you want to edit?")
            index = find_connection(rooms,room_name)
            room = rooms[index]
            name, description = room_name_and_description()
            room.change_name_and_description(name,description)
            list_of_ds = change_connections(room, rooms)
            room.change_connections(list_of_ds)
            rooms[index] = room
        
        go_on = input("""Do you want to continue with the rooms?
                      Type y for yes and n for no""")
        if handle_human_input(go_on) is False:
            cont = False
    
    return rooms
    

def room_name_and_description():
    fix = True
    while fix ==True:
        room_name = input("What is this area's name?")
        room_description = input("""Please write the text you
                                 want your player to see when he or
                                 she enters this area""")
        print(room_name, room_description)
        correction = input("""Is this correct? Please type y for yes
                           and n for no""")
        if handle_human_input(correction) is True:
            fix = False
    return room_name, room_description

#we do length of the list to make sure room number isn't repeated

def create_connections(rooms,number):
    directions = ["north", "south", "east", "west",
                  "northeast", "northwest", "southeast",
                  "southwest", "up", "down", "in", "out"]
    
    room = rooms[number]
    
    for d in directions:
        print("Is there a room connected to", room, "by the direction",
              d, "?")
        
        cont = input("Type y for yes and n for no")
        if handle_human_input(cont) is False:
            room.connections.append(-1)
        else:
            new = input("Do we need a new room? Type y for yes, n for no")
            if handle_human_input(new) is True:
                name, description = room_name_and_description()
                n = len(rooms)
                rooms.append(Room(name, description,n))
                room.connections.append(n)
            else:
                #print all of the room names, find the room, and add that spot
                print_list_of_all_rooms(rooms)
                room_connected = input("Which room is connected to this room?")
                room.connections.append(find_connection(rooms,room_connected))
    
    room.complete = True
    rooms[number] = room
    
    return rooms

def change_connections(room, rooms):
    directions = ["north", "south", "east", "west",
                  "northeast", "northwest", "southeast",
                  "southwest", "up", "down", "in", "out"]
    
    room_connections = []
    
    for i in range(len(directions)):
        print("Is there a room connected to", room, "by the direction",
              directions[i], "?")
        
        cont = input("Type y for yes and n for no")
        if handle_human_input(cont) is False:
            room_connections.append(-1)
        else:
            room_connected = input("Which room is connected to this room?")
            room_connections.append(find_connection(rooms,room_connected))
    return room_connections
    
    
def handle_human_input(human_input):
    if human_input=='y':
        return True
    else:
        return False

def print_list_of_all_rooms(list_of_rooms):
    for r in list_of_rooms:
        print(r.name)

#need to account for room not included.
def find_connection(list_of_rooms, name):
    for r in list_of_rooms:
        if r.name==name:
            return r.number
    
def find_missing_rooms(rooms):
    for r in rooms:
        if r.complete is False:
            rooms = create_connections(rooms,r.number)
    return rooms

def final_check(rooms):
    for r in rooms:
        print(r.name, r.description, r.connections)
        go = input("Does this look correct? Type y for yes and n for no")
        if handle_human_input(go) is False:
            n, d = room_name_and_description()
            r.change_name_and_description(n,d)
            list_of_ds = change_connections(r, rooms)
            r.change_connections(list_of_ds)
    return rooms

make_game()