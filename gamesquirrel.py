import useful

import playersquirrel
import roomsquirrel
import itemsquirrel
 

# Master Class to store all the game information
class GameSquirrel():

    # Constructor
    def __init__(self):
        self.name = ""
        self.instructions = ""
        self.credits = ""
        self.rooms = []
        self.items = []
        self.player = playersquirrel.Player()
        
    def EditConnection(self, fromRoom, toRoom, direction):
        self.rooms[fromRoom].edit_connection(direction, toRoom)

    def removeRoom(self, room_index):
        for r in self.rooms: #remove connections
            if room_index in r.connections:
                indices = [i for i,val in enumerate(r.connections)
                           if val==room_index]
                for ind in indicies:
                    r.connections[ind] = -1
        
        for item in self.items: #remove item info from room
            if room_index == item.location:
                item.location = None
        
        self.rooms.remove(self.rooms[room_index])
    
    def AddItem(self, item):
        self.items.append(item)

    def PlaceItem(self, itemIndex, where):
        self.items[itemIndex].PlaceAt(where)
        if where == -2: # PLAYER INVENTORY
            self.player.AddToInventory(itemIndex)
        elif where >= 0: # IN A ROOM
            self.rooms[where].AddItem(itemIndex)
          
    def UnplaceItem(self, itemIndex, where):
        self.items[itemIndex].Unplace()
        if where == -2: # PLAYER INVENTORY
            self.player.RemoveFromInventory(itemIndex)
        elif where >= 0: # IN A ROOM
            self.rooms[where].RemoveItem(itemIndex)
        
 
    # Returns a list with the indexes of the not placed items
    def GetNotPlacedItems(self):
        unplacedList = []
        for i in range(len(self.items)):
            if self.items[i].whereIs == -1:
                unplacedList.append(i)
        return unplacedList
        
        
    def removeItem(self):
        print("NOT YET IMPLEMENTED")
