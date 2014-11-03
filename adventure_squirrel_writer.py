import useful


def make_game():

    # Prompts the writer for his name
    print("Hello, what is your name?")
    writer_name = input()

    # Asks what he wants to do
    msg = "Hi " + writer_name + ", what would you like to do?"
    opt = ["CREATE a new game", "EDIT a saved game", 
           "PREVIEW a saved game", "EXIT this program"]
    answer = useful.showMenu(msg, opt)

    # Writer chose to CREATE a new game
    if answer[0] == 0:
        createNewGame(writer_name)
        create_item()
    # Writer chose to EDIT a saved game
    elif answer[0] == 1:
        editSavedGame()

    # Writer chose to PREVIEW a saved game
    elif answer[0] == 2:
        previewSavedGame()
    
    # Writer chose to EXIT this program
    elif answer[0] == 3:
        print(writer_name + ", it was great to have you around.")
   
    # Something strange happened
    else:
        print("What kind of sorcery is this?")
        print(answer)

# Drives the user through the pipeline of game making
def createNewGame(writer_name):
    
    # Here we create a mock game object - although Bruno believes it would be 
    # better to make that the last thing to do.
    game = Game()

    # Here we will have our user create his/her game
    print(
"""Hey there {0}! We are going to ask you a few questions to help
you creating your own text-based adventure game. Please be sure to
have your room connections, items, and actions already in mind."""
.format(writer_name)
    )
     
    # Prompts the user for the name of the game
    print("First off, what is your game's name?")
    game_name = input()
    game.name = game_name
    
    # Or should we have you two make this?
    print("What is your player's name?")
    player_name = input()
    player = Player(player_name)
    game.player = player    

    # Add stuff to the game:
    game = writeGame(game)

    # create_item()
    
    #now we will create rooms
    #create_rooms()

# Loads a story file and puts the user back on the pipeline of game making
# THIS IS NOT YET IMPLEMENTED
def editSavedGame():    
    print("THIS IS NOT YET IMPLEMENTED")

# The idea is that a user can play his unfinished game through here and
# still retain his editing skills.
# THIS IS NOT YET IMPLEMENTED - PROBABLY WILL NEVER BE
def previewSavedGame():
    print("THIS IS NOT YET IMPLEMENTED")

    
#This function keeps prompting the user for additions for his game
def writeGame(game):
   
    msg = useful.formatHeader("What do you want to do?")
    opt = ["CREATE a ROOM", "EDIT a ROOM", "REMOVE a ROOM",
           "CREATE an ITEM", "EDIT an ITEM", "REMOVE an ITEM",
           "SAVE STORY FILE", "EXIT WITHOUT SAVING"]
    
    answer = useful.showMenu(msg, opt)
    
    # User selected CREATE a ROOM
    if answer[1] == opt[1]:
        

    # User selected EDIT a ROOM
    if answer[1] == opt[1]:
    
    # User selected REMOVE a ROOM
    if answer[1] == opt[1]:
    
    # User selected CREATE an
    if answer[1] == opt[1]:
    
    # User selected CREATE an ROOM
    if answer[1] == opt[1]:
    
    # User selected CREATE an ROOM
    if answer[1] == opt[1]:
    
    # User selected CREATE a
    if answer[1] == opt[1]:
    
     
    print("Ok so far.")

    #returns the modified game
    return game
    

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
    
    def __init__(self):
        self.name = ""
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
    

# Items are objects that the player can interact with,  
# to the most varied outcomes.
class Item(object):
    
    def __init__(self, name, description):
        self.name = name
        self.description = description 

    
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

def create_item():
    
    #Name of the item: (Step 1)
    print("What is the name of the item you are creating?")
    item_name = input()

    #Description of the item: (Step 2)
    print("What is the description of the item you are creating?")
    item_description = input()

    #Placeble in inventory: (Step 3)
    msg = useful.formatHeader("Is this item placeble on the player's inventory?")
    
    if (useful.showMenu(msg, ['yes', 'no'])[0] == 0):
        item_inv = True
        
        #Droppable after picked up: 
        msg = useful.formatHeader("Can the player drop this item after picking it up?") 
        if (useful.showMenu(msg, ['yes', 'no'])[0] == 0):
            item_drop = True
        else:
            item_drop = False
        
    else: 
        item_inv =  False
        item_drop = False

    #Usable item: (Step 4)
    use_effects = ["NOTHING - But display a message anyway", 
                   "The player dies",
                   "The player gets transported to another room",
                   "Light up the room"]

    msg = useful.formatHeader("Can the player USE this object")
    if (useful.showMenu(msg, ['yes', 'no'])[0] == 0):
        item_use = True
        answer = useful.showMenu(msg, use_effects)
    else :
        item_use = False
        answer = (-1, 'NO')
     
    #Now I have all the information i need to create the item
    print('Name: ' + str(item_name))
    print('Description: ' + str(item_description))
    print('item_inv: ' + str(item_inv))
    print('item_drop: ' + str(item_drop))
    print('item_use: ' + str(item_use))
    print('index: ' + str(answer[0]) + ' -- Option: ' + answer[1])
    

#In here we are calling the method used to start the game making process.
make_game()
