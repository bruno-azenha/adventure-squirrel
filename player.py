# The player class that is used for storing the information fo the player
import Item # Item class from Bruno

class Player(object):

    def __init__(self, name):

        self.name = name
        self.inventory = []
        self.score = 0
        self.moves = 0
        # we should define what the player's action, such as "punch", "look", etc.
        self.available_actions = []

    def pick_up(item):

    	if(isinstance(item, Item)): # Item class from Bruno
    		self.inventory.append(item)
    	else:
    		print("You cannot pick up this item.")

    	return self.inventory

    def add_score(points_worth):
    	self.score += points_worth

    def increment_move():
    	self.moves += 1

    def __str__(self):
    	return 'Player: {0}\nScore: {1}\nMoves: {2}\nInventory: {3}\nAvailable Actions: {4}'.format(self.name, 
    		self.score, self.moves,
    		self.inventory, self.available_actions)

    def __repr__(self):
    	return 'Player: {0}\nScore: {1}\nMoves: {2}\nInventory: {3}\nAvailable Actions: {4}'.format(self.name, 
    		self.score, self.moves,
    		self.inventory, self.available_actions)



def main():
	test = Player("Justin Bieber")
	print(test)

if __name__ == "__main__":
	main()
