import useful
 
DIRS = ["NORTH", "NORTHEAST", "EAST", "SOUTHEAST", "SOUTH", "SOUTHWEST"
        "WEST", "NORTHWEST", "UP", "DOWN", "IN", "OUT", "-- BACK --"]

# Class to store the information of each room object 
class RoomSquirrel():
    
    # Index is a variable shared by all RoomSquirrel objects
    # it helps mantaining unique indexes for the rooms

    # Constructor
    def __init__(self,name,description):
        self.name = name
        self.description = description
        self.connections = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
        self.items = []
        #self.dictOfConnections = {d: None for d in DIRS}
    
    def __str__(self): #string representation
            return self.name
        
    # Method to edit the connection list of a room
    # it returns an updated gameMap
    def edit_connection(self, direction_number, room_number):
        direction = DIRS[direction_number]
        self.connections[direction_number] = room_number
        #self.dictOfConnections[direction] = self.instances[room_number]

    # Method to add an item to a room
    # item is an index to the item in GAME.items  list
    def AddItem(self, item):
        self.items.append(item)
    
    def RemoveItem(self, item):
        self.items.remove(item)

    # Method to remove an item to a room
    # item is an index to the item in GAME.items  list
    def RemoveItem(self, item):
        self.items.remove(item)    

    #def remove_self(self):
        #for room in RoomSquirrel.instances:
        #    if self in room.dictOfConnections.values():
        #        [item = None for item in room.dictOfConnections.values()
        #        if item==self]
        #       [index = -1 for index in room.connections
        #       if index==self.index]
        
       # RoomSquirrel.instances.remove(self)
