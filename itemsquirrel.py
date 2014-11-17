# Class to store the information of each item object  
class ItemSquirrel():

    # Constructor
    def __init__(self, name, desc, pick, drop):
        self.name = name
        self.description = desc
        self.isPickable = pick
        self.isDroppable = drop
        self.whereIs = -1 # At the moment of creation, an item isn't anywhere
                          # Later this will be a room index at GAME.rooms list

    def setName(self, name):
        self.name = name

    def setDescription(self, description):
        self.description = description

    def setInventory(self, isPickable, isDroppable):
        self.isPickable = isPickable
        self.isDroppable = isDroppable

    def PlaceAt(self, place):
        self.whereIs = place

    def Unplace(self):
        self.whereIs = -1
