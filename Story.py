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
        self.gameMap = GameMapStory()

    def createRoom(self):
        newRoom = RoomStory()       
        self.rooms = RoomStory.instances
        self.gameMap = newRoom.editConnections(self.gameMap) #need to work with this
        print("Ok so far.") 

    def editRoom(self):
        useful.clearScreen()
        msg = "Which room do you want to edit?"
        opt = self.rooms
        opt.append("Return")
        answer = useful.showMenu(msg, opt)
        print(answer)
        for i in range(len(self.rooms)):
            if answer[1] == opt[i]:
                opt[i].editConnections()
            elif answer[1] == opt[len(self.rooms)]:
                print("need to go back")

    def removeRoom(self):
        #show list of all rooms
        #select room and then go remove it
        useful.clearScreen()
        msg = "Which room do you want to remove?"
        opt = self.rooms
        opt.append("Return")
        answer = useful.showMenu(msg, opt)
        print(answer)
        
        for i in range(len(self.rooms)):
            if answer[1] == opt[i]:
                opt[i].remove_self()
                self.rooms = RoomStory()
                #also need to update game Map
            elif answer[1] == opt[len(self.rooms)]:
                print("need to go back")

    def createItem():
        print("NOT YET IMPLEMENTED")

    def editItem():
        print("NOT YET IMPLEMENTED")

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
    counter = 0
    instances = []

    # Constructor
    def __init__(self):
        self.index = self.counter
        RoomStory.counter+=1
        self.instances.add_to_instances()
        
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
        self.dictOfConnections = {d: None for d in DIRS}
    
    def __str__(self): #string representation
            return self.name
        
    def get_index(): #get room index
        return self.index
        
        
    def add_to_instances(self): #add instance
        RoomStory.instances.append(self)

    # Method to edit the connection list of a room
    # it returns an updated gameMap
    def edit_connections(self, gameMap):
        header = useful.formatHeader(self.name)
        options = get_options()
        options.append("Return")
        print(header)
        msg = header + "\nEdit the connections of this room."
        answer = useful.showMenu(msg, options)
        print(answer)
        
        #see if this is true?
        for i in range(len(DIRS)):
            if answer[1] == options[i]:
                update_connection(i)
                #how to get previous menu back?
        if answer[1] == options[len(DIRS)]:
            gm = GameMapStory()
            return gm
        
    
    def update_connection(self,direction_number):
        direction = DIRS[direction_number]
        roomNames = [room.name for room in RoomStory.instances]
        useful.clearScreen()
        roomNames.append("Return")
        headerHere = useful.formatHeader(self.name)
        msg = headerHere + "\nSelect the room to add in " + direction +
            "\nThe current connection is " + self.dictOfConnections[direction]
        answer = useful.showMenu(msg, roomNames)
        print(answer)
        
        for i in range(len(RoomStory.instances)):
            if answer[1] == opt[i]:
                #if the room connection is index i
                self.connections[direction_number] = i
                self.dictOfConnections[direction] = self.instances[i]
    
    def get_options(self):
        opts = [None]*len(DIRS)
        for i in range(DIRS):
            opts[i] = DIRS[i] + " " + self.dictOfConnections[DIRS[i]]
        return opts
    
    def remove_self(self):
        """We need to remove all connections and the instance
        from our Room Story lis
        """
        for room in RoomStory.instances:
            if self in room.dictOfConnections.values():
                [item = "None" for item in room.dictOfConnections.values()
                 if item==self]
                [index = -1 for index in room.connections
                if index==self.index]
        
        RoomStory.counter-=1 #lower counter
        RoomStory.instances.remove(self)
        
    

# Class to store the information of each item object  
class ItemStory():

    # Constructor
    def __init__(self):
        self.name = ""

# Class to store the room connections
class GameMapStory(list):

    # Constructor that does nothing so far   
    def __init__(self):
        self.matrixOfConnections = []
        
    # This method adds the room, with the 
    # passed connection list to the game map       
    def addRoom(room, connections):
        self.append(connections) 