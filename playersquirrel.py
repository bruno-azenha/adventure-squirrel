# The player class that is used for storing the information fo the player

class Player(object):

    def __init__(self):

        #self.name = name
        self.inventory = []
        self.score = 0
        self.moves = 0
        self.current_room = 0
        
    def __str__(self):
    	return 'Player: {0}\nScore: {1}\nMoves: {2}\nInventory: {3}\nAvailable Actions: {4}'.format(self.name, 
    		self.score, self.moves,
    		self.inventory, self.available_actions)

    def AddToInventory(self, itemIndex):
        self.inventory.append(itemIndex)

    def RemoveFromInventory(self, itemIndex):
        self.inventory.remove(itemIndex)
