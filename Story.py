import useful
 
DIRS = ["North", "South", "East", "West",
        "Northeast", "Northwest", "Southeast",
        "Southwest", "Up", "Down", "In", "Out", "FINISHED"]

# Master Class to store all the game information
class GameStory():

    # Constructor
    def __init__(self):
        self.name = ""
        self.rooms = []
        self.items = []
        self.gameMap = GameMapStory()

    def createRoom(self):
        newRoom = RoomStory()        
        self.rooms.append(newRoom)
        self.gameMap = newRoom.editConnections(self.gameMap)

    def editRoom():
        print("NOT YET IMPLEMENTED")

    def removeRoom():
        print("NOT YET IMPLEMENTED")

    def createItem(self):
        newItem = ItemStory()
        self.items.append(newItem)

    def editItem(self):
        # Creates a List with the names of each item:
        item_names = []
        for item in self.items:
            item_names.append(item.name)
        item_names.append("GO_BACK")
        msg = "\nChose the item you wish to edit:\n"
        answer = useful.showMenu(msg, item_names)

    def removeItem():
        print("NOT YET IMPLEMENTED")

    def saveStory():
        print("NOT YET IMPLEMENTED")

    def saveStoryAndExit():
        print("NOT YET IMPLEMENTED")

    def exitWithoutSave():
        print("NOT YET IMPLEMENTED")


# Class to store the information of each room object 
class RoomStory():
    
    # Index is a variable shared by all RoomStory objects
    # it helps mantaining unique indexes for the rooms
    index = 0

    # Constructor
    def __init__(self):
        
        # Something like this will be used for the indexing of rooms in the game map
        # self.index = index
        # index += 1
        
        # Gets the name of this room
        print("What is this area's name?")
        self.name = input()
        prettyName = useful.formatHeader(self.name)
       
        # Loop to get the description right 
        while True:
            useful.clearScreen()
            print(prettyName)
            print("""Please write the text you want your player 
to see when he enters this area
""")
            description = input()

            useful.clearScreen()
            msg = prettyName + "\nIs the following description correct?\n";
            msg += useful.formatLinebreak(description)
            if useful.showMenu(msg, ["yes", "no"])[0] == 0:
                break    

        self.connections = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
        # For the connections information: I'm not sure we should have it
        # duplicate, as of now, we have the same information in the Room
        # object and also in the game map object. Which is handy, but not nice.

    # Method to edit the connection list of a room
    # it returns an updated gameMap
    def editConnections(self, gameMap):
        header = useful.formatHeader(self.name)
        print(header)
        msg = header + "\nEdit the connections of this room."
        answer = useful.showMenu(msg, DIRS)
        print(answer)

        # This is just to keep it quiet 
        gm = GameMapStory()
        return gm
        #NOT FINISHED

# Class to store the information of each item object  
class ItemStory():

    # Constructor
    def __init__(self):
        # Gets the name of this item
        print("What is this item's name?")
        self.name = input()
        prettyName = useful.formatHeader(self.name)
       
        # Loop to get the description right 
        while True:
            os.system('clear')
            print(prettyName)
            print("Please write the description of this item.\n")
            description = input()
            os.system('clear')
            msg = prettyName + "\nIs the following description correct?\n";
            msg += useful.formatLinebreak(description)
            if useful.showMenu(msg, ["yes", "no"])[0] == 0:
                self.description = description
                break

        # Placeble in the inventory? 
        msg = prettyName + "\nCan the user pick this item up?\n";
        msg += useful.formatLinebreak(description)
        if useful.showMenu(msg, ["yes", "no"])[0] == 0:
            self.isPickable = True
 
            # Droppable? 
            msg = prettyName + "\nCan the user drop this item from his inventory?\n";
            msg += useful.formatLinebreak(description)
            if useful.showMenu(msg, ["yes", "no"])[0] == 0:
                self.isDroppable = True
            else: self.isDroppable = False
        
        else:
            self.isPickable = False 
            self.isDroppable = False


# Class to store the room connections
class GameMapStory(list):

    # Constructor that does nothing so far   
    #def __init__(self):
        
    # This method adds the room, with the 
    # passed connection list to the game map       
    def addRoom(room, connections):
        self.append(connectikons) 

def room_name_and_description():
    fix = True
    while fix ==True:
        room_description = input("""Please write the text you
                                 want your player to see when he or
                                 she enters this area""")
        print(room_name, room_description)
        correction = input("""Is this correct? Please type y for yes
                           and n for no""")
        if handle_human_input(correction) is True:
            fix = False
    return room_name, room_description
