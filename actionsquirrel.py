import useful

DEFAULT_ACTIONS = ["pick", "drop", "examine", "look" , "move", 
                "help", "save", "combine"]

#
# Stories the information of each action and the 
# suite of hardcoded functions for action effects
#

class CustomAction:

    def __init__(self, verb):
        self.verb = verb
        self.listOfItems = []
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
        r = []
        for fun in self.listOfFunctions:
            result = fun(*listOfArguments[index])
            if result is not True or result is not False:
                r.append(result)
            index += 1    
        return r

# ------------------------------------------------------- #
# ----- The Following are all of our Default Action ----- #
# ------------------------------------------------------- #

# Returns True if succeed, False otherwise 
def Pick(itemIndex, game):
    

    if (game.items[itemIndex].isPickable):
        # Implement add to inventory
        game.player.inventory.append(itemIndex)
        return True
    else: 
        return False

# Returns True if succeed, False otherwise 
def Drop(itemIndex, game):

    if (game.items[itemIndex].isDroppable):
        # Implement drop to room
        game.player.inventory.remove(itemIndex)
        game.items[itemIndex].whereIs = game.player.current_room
        return True
    else:
        return False

# Returns item description as str
def Examine(itemIndex, game):
    return game.items[itemIndex].description

# Returns the room's description and room's itemIndex
def Look(roomIndex, game):

    return (game.rooms[roomIndex].description, game.rooms[roomIndex].items)

# Returns True if movement is valid, False otherwise
def Move(game, direction):
    # Implement validity check
    # assume "direction" is a member of DIRS

    # find where is the player
    current_room = game.player.current_room

    # get the connection of the current room
    connections = current_room.connections

    DIRS = ["NORTH", "NORTHEAST", "EAST", "SOUTHEAST", "SOUTH", "SOUTHWEST"
             "WEST", "NORTHWEST", "UP", "DOWN", "IN", "OUT"]

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
def ShowHelp(game):
    # Implement help retrieval
    
    return game.instruction

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
def CombineItems(game, item1_index, item2_index, item3_index):
    # Implement CombineItems
    game.items[item1_index].whereIs = -1 # disappear
    game.items[item2_index].whereIs = -1 # disappear
    game.items[item3_index].whereIs = -2 # the item 3 is created in inventory
    return game.items[item3_index].description #optional
    
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
    game.player.current_room = roomIndex
    return True

# Changes the Player's score
def ChangeScore(game, scoreChange):
    game.player.score += scoreChange
    return True

# Oops we tried not to print anything in here, but...
# Displays Text
def DisplayText(game, text):
    return text

# Add Item to player inventory
def AddItemToInventory(game, item):
    game.player.inventory.append(item)
    return True

# Remove Item from player inventory
def RemoveItemFromInventory(game, item):
    game.player.inventory.remove(item)
    return True

# Drop item
def DropItem(game, itemIndex):
    del game.items[itemIndex]
    return True

# Drop all items
def DropAll(game):
    for i in range(len(game.items)):
        game.items[i].whereIs = game.player.current_room
    return True

# Win the Game
# need to figure out with our game engine
def Winning(game):
    return True
