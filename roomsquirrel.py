import useful
 
DIRS = ["North", "South", "East", "West",
        "Northeast", "Northwest", "Southeast",
        "Southwest", "Up", "Down", "In", "Out", "FINISHED"]

# Class to store the information of each room object 
class RoomStory():
    
    # Index is a variable shared by all RoomStory objects
    # it helps mantaining unique indexes for the rooms
    counter = 0
    instances = []

    # Constructor
    def __init__(self,name,description):
        self.index = self.counter
        RoomStory.counter+=1
        self.instances.add_to_instances()
        self.name = name
        self.description = description
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
    def edit_connections(self, direction_number):
        direction = DIRS[direction_number]
        self.connections[direction_number] = i
        self.dictOfConnections[direction] = self.instances[i]

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