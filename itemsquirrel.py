# Class to store the information of each item object  
class ItemSquirrel():

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
