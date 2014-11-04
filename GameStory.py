import useful

# Master Class to store all the game information
class GameStory():



    # Constructor
    def __init__(self):
        self.name = ""
        self.gameMap = GameMapStory()

    def createRoom():

    def createRoom():        
        print("NOT YET IMPLEMENTED")

    def editRoom():
        print("NOT YET IMPLEMENTED")

    def removeRoom():
        print("NOT YET IMPLEMENTED")

    def createItem():
        print("NOT YET IMPLEMENTED")

    def editItem():
        print("NOT YET IMPLEMENTED")

    def removeItem():
        print("NOT YET IMPLEMENTED")

    def saveStory():
        print("NOT YET IMPLEMENTED")

    def saveStoryAndExit():
        print("NOT YET IMPLEMENTED")

# Class to store the information of each room object 
class RoomStory():
    
    # Index is a variable shared by all RoomStory objects
    # it helps mantaining unique indexes for the rooms
    index = 0

    # Constructor
    def __init__(self):
        self.index = index
        index += 1
        print("What is this area's name?")
        self.name = input()
        prettyName = useful.formatHeader(self.name)
        print(prettyName)
        print(
"""Please write the text you want your player 
to see when he enters this area""")
        self.description = input()

        



# Class to store the information of each item object  
class ItemStory():

    # Constructor
    def __init__(self)i:
        
        self.name = ""

# Class to store the room connections
class GameMapStory(list):

    # Constructor    
    def __init__(self):
    
    # This method adds the room, with the 
    # passed connection list to the game map       
    def addRoom(room, connections):
        self.append 

def room_name_and_description():
    fix = True
    while fix ==True:
        room_description = input("""Please write the text you
                                 want your player to see when he or
                                 she enters this area""")
        print(room_name, room_description)
        correction = input("""Is this correct? Please type y for yes
                           and n for no""")
        if handle_human_input(correction) is True:
            fix = False
    return room_name, room_description
