import useful
#
# Stories the information of each action and the 
# suite of hardcoded functions for action effects
#

class CustomAction:

    def __init__(self, verb):
        self.verb = verb
        self.listOfFunctions = []
        self.listOfArguments = []

    # In order to create the custom actions, we merge together
    # different harcoded smaller actions to result on the desired
    # effect.
    def execute(self):
        # Executes each one of the functions in self.listOfFunction
        # passing as parameter the associated argument stored in
        # self.listOfArguments
        index = 0
        for fun in self.listOfFunctions:
            # This shouldn't run yet 
            fun(*listOfArguments[index])
            index += 1
        

# ------------------------------------------------------- #
# ----- The Following are all of our Default Action ----- #
# ------------------------------------------------------- #

# Returns True if succeed, False otherwise 
def Pick(item, game):
    #print("NOT IMPLEMENTED")
    if (item.isPickable):
        # Implement add to inventory
        game.player.inventory.append(item)
        return True
    else: 
        return False

# Returns True if succeed, False otherwise 
def Drop(item, game):
    #print("NOT IMPLEMENTED")

    if (item.isDroppable):
        # Implement drop to room
        game.player.inventory.remove(item)
        return True
    else:
        return False

# Returns item description as str
def Examine(item):
    return item.description

# Returns True if movement is valid, False otherwise
def Move(game, direction):
    # Implement validity check
    # assume "direction" is a member of DIRS

    # find where is the player
    current_room = game.player.current_room

    # get the connection of the current room
    connections = current_room.connections

    DIRS = ["North", "South", "East", "West",
        "Northeast", "Northwest", "Southeast",
        "Southwest", "Up", "Down", "In", "Out", "FINISHED"]

    target_index = DIRS.index(direction)

    # we can go this way
    if connections[target_index] > 0:
        return True
    # we cannot go this way
    else:
        return False

# Returns a list with the items that are in the players inventory 
def Inventory(game):
    # Implemment inventory retrieval
    #print("NOT IMPLEMENTED")
    
    return game.player.inventory

# Returns help text as string
def ShowHelp():
    # Implement help retrieval
    print("NOT IMPLEMENTED")
    text = "Help text."
    return text

# Save current state of the game
# Returns True if succes, False otherwise
def SaveGame(game):
    # Implement save game
    #print("NOT IMPLEMENTED")

    game.saveStory()
    return True

# Load a previous state of the game
# Returns True if succes, False otherwise
def LoadGame(game):
    # Implement load game
    #print("NOT IMPLEMENTED")
    game = None
    while True:

        intro = useful.formatLinebreak("What is name of the pickle file that contains the game information? (e.g. \"Game_Info.pickle\")",50)
        filename = input(intro + "\n"*2)
        
        try:
            with open(filename,'rb') as f:
                game = pickle.load(f)
            break

        except FileNotFoundError:
            print("\nThe file doesn't exist. Try again.\n")

    print("The game info has been loaded.\n")

    return True

# Combine two items to generate a third
# Returns True if succes, False otherwise
def CombineItems(item1, item2, item3):
    # Implement CombineItems
    print("NOT IMPLEMENTED")
    return True
    
# ---------------------------------- #
# ----- End of Default Actions ----- #
# ---------------------------------- #


# ------------------------------------- #
# ----- Results "Building Blocks" ----- # 
# ------------------------------------- #

# Some explanations about results building blocks:
# The following  function are building blocks of custom actions behavior
# When you create a custom action, you can use multiple of these blocks
# in order to achieve the result you want.
# For example: A custom action of entering a portal that destroys your inventory
# could use the blocks SpecialMove, DeleteInventory and DisplayText

# Because we can never know how the writer is going to mix these blocks,
# we do not expect any kind of return parameter in any one of them.

# Each one of the blocks receives as parameter a Tuple
# The first element is the game object
# The following ones depend on the block type

# Moves the player to an adjacent room according to game map
def RegularMove(game, roomIndex):  
    # Implement RegularMove
    print("NOT IMPLEMENTED")

# Moves the player to a room, independent of game map validity
def SpecialMove(game, roomIndex):
    # Implement SpecialMove
    print("NOT IMPLEMENTED")

# Changes the Player's score
def ChangeScore(game, scoreChange):
    # Implement ChangeScore
    print("NOT IMPLEMENTED")

# Oops we tried not to print anything in here, but...
# Displays Text
def DisplayText(game, text):
    # Implement DisplayText
    print("NOT IMPLEMENTED")

# Add Item to player inventory
def AddItemToInventory(game, item):
    # Implement AddItemToInventory
    print("NOT IMPLEMENTED")

# Drop item

# Drop all items

# Win the Game

# 
#
#
