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

    def removeRoom(self, room):
        print("NOT YET IMPLEMENTED")

    def removeItem(self):
        print("NOT YET IMPLEMENTED")
