import useful
import sys
import playersquirrel
 
DIRS = ["North", "South", "East", "West",
        "Northeast", "Northwest", "Southeast",
        "Southwest", "Up", "Down", "In", "Out", "FINISHED"]

EDIT_ITEM = ["NAME", "DESCRIPTION", "INVENTORY BEHAVIOR",
             "AVAILABLE ACTIONS"]
# Master Class to store all the game information
class GameStory():

    # Constructor
    def __init__(self):
        self.name = ""
        self.instructions = ""
        self.credits = ""
        self.rooms = []
        self.items = []
        self.gameMap = GameMapStory()
        self.player = playersquirrel.Player()
        

    def createRoom(self):
        newRoom = RoomStory()        
        self.rooms.append(newRoom)
        self.gameMap = newRoom.editConnections(self.gameMap)

    def editRoom(self, room):
        print("NOT YET IMPLEMENTED")

    def removeRoom(self, room):
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
        useful.clearScreen()

        if answer[1] == "GO_BACK":
            return 0

        i = answer[0] # Item index

        # Gives the options of editing the item
        msg = "\nWhat would you like to EDIT?\n"
        self.items[i]

        answer = useful.showMenu(msg, EDIT_ITEM)
        if answer[1] == "NAME": # Edit Name
            name = input("What is the new name?\n")
            self.items[i].setName(name)

        elif answer[1] == "DESCRIPTION": # Edit description
            description = input("What is the new description?\n")
            self.items[i].setDescription(description)

        elif answer[1] == "INVENTORY BEHAVIOR": # Edit inv behavior
            # Placeble in the inventory? 
            msg = "\nCan the user pick this item up?\n";
            if useful.showMenu(msg, ["yes", "no"])[0] == 0:
                isPickable = True
     
                # Droppable? 
                msg = "\nCan the user drop this item from his inventory?\n";
                if useful.showMenu(msg, ["yes", "no"])[0] == 0:
                    isDroppable = True
                else: isDroppable = False
            
            else:
                isPickable = False 
                isDroppable = False
            
            self.items[i].setInventory(isPickable, isDroppable)

        elif answer[1] == "AVAILABLE ACTIONS": #Edit available actions
            print("NOT YET IMPLEMENTED")

    def removeItem(self):
        
        item_names = []
        for item in self.items:
            item_names.append(item.name)
        item_names.append("GO_BACK")
        msg = "\nChose the item you wish to remove:\n"
        answer = useful.showMenu(msg, item_names)
        useful.clearScreen()

        if answer[1] == "GO_BACK":
            return 0

        i = answer[0] # Item index
        
        msg = "\nAre you sure you want to REMOVE this item?\n";
        if useful.showMenu(msg, ["yes", "no"])[0] == 0:
            item = self.items.pop(i)
        

    def saveStory(self):
        while True:

            intro = useful.formatLinebreak("What will be the name of the pickle file that contains the game information? (e.g. \"Game_Info.pickle\")",50)

            filename = input(intro + "\n"*2)
            if filename.endswith(".pickle"):
                break
            else:
                print("The file must be a pickle file.\n")

        # create a game obejct as exactly the same as "self"
        tmp = GameStory()
        tmp.name = self.name
        tmp.rooms = self.rooms
        tmp.items = self.items
        tmp.gameMap = self.gameMap
        tmp.player = self.player

        with open(filename,'wb') as f:
            pickle.dump(tmp, f)

        print("\nThe game has been saved.")

    def saveStoryAndExit(self):
        
        self.saveStory()
        sys.exit()

    def exitWithoutSave():
        #print("NOT YET IMPLEMENTED")
        sys.exit()


# Class to store the information of each room object 
class RoomStory():
    
    # Index is a variable shared by all RoomStory objects
    # it helps mantaining unique indexes for the rooms
    index = 0

    # Constructor
    def __init__(self):
        self.name = ""        
        # Something like this will be used for the indexing of rooms in the game map
        # self.index = index
        # index += 1
        
        # Gets the name of this room
#        print("What is this area's name?")
#        self.name = input()
#        prettyName = useful.formatHeader(self.name)
       
        # Loop to get the description right 
#        while True:
#            useful.clearScreen()
#            print(prettyName)
#            print("""Please write the text you want your player 
#to see when he enters this area
#""")
#            description = input()
#
#            useful.clearScreen()
#            msg = prettyName + "\nIs the following description correct?\n";
#            msg += useful.formatLinebreak(description)
#            if useful.showMenu(msg, ["yes", "no"])[0] == 0:
#                break    

#        self.connections = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
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
    def __init__(self, name, desc, pick, drop):
        self.name = name
        self.description = desc
        self.isPickable = pick
        self.isDroppable = drop

    def setName(self, name):
        self.name = name

    def setDescription(self, description):
        self.description = description

    def setInventory(self, isPickable, isDroppable):
        self.isPickable = isPickable
        self.isDroppable = isDroppable

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
