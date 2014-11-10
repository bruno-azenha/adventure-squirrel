import useful
import Story

def make_game():
    
    useful.clearScreen()    
    # Prompts the writer for his name
    print("Hello, what is your name?")
    writer_name = input()

    #Loop in the main menu while user does not chose to exit
    while True:
        # Asks what he wants to do
        msg = "Hi " + writer_name + ", what would you like to do?"
        opt = ["CREATE a new game", "EDIT a saved game", 
               "PREVIEW a saved game", "EXIT this program"]
        answer = useful.showMenu(msg, opt)

        # Writer chose to CREATE a new game
        if answer[0] == 0:
            createNewGame(writer_name)

        # Writer chose to EDIT a saved game
        elif answer[0] == 1:
            editSavedGame()

        # Writer chose to PREVIEW a saved game
        elif answer[0] == 2:
            previewSavedGame()
        
        # Writer chose to EXIT this program
        elif answer[0] == 3:
            print(writer_name + ", it was great to have you around.")
            break;
       
        # Something strange happened
        else:
            print("What kind of sorcery is this?")
            print(answer)
            break;

# Drives the user through the pipeline of game making
def createNewGame(writer_name):
    
    # Here we create a mock game object - although Bruno believes it would be 
    # better to make that the last thing to do.
    game = Story.GameStory()

    # Here we will have our user create his/her game
    print(
"""Hey there {0}! We are going to ask you a few questions to help
you creating your own text-based adventure game. Please be sure to
have your room connections, items, and actions already in mind.
"""
.format(writer_name)
    )
     
    # Prompts the user for the name of the game
    print("First off, what is your game's name?")
    game_name = input()
    game.name = game_name
    
    # Or should we have you two make this?
    print("What is your player's name?")
    player_name = input()
    player = Player(player_name)
    game.player = player    

    # Add stuff to the game:
    game = writeGame(game)
    
    # create_item()
    
    #now we will create rooms
    #create_rooms()

# Loads a story file and puts the user back on the pipeline of game making
# THIS IS NOT YET IMPLEMENTED
def editSavedGame():    
    print("EDIT SAVED GAME IS NOT YET IMPLEMENTED")

# The idea is that a user can play his unfinished game through here and
# still retain his editing skills.
# THIS IS NOT YET IMPLEMENTED - PROBABLY WILL NEVER BE
def previewSavedGame():
    print("PREVIEW SAVED GAME IS NOT YET IMPLEMENTED")

    
#This function keeps prompting the user for additions for his game
def writeGame(game):
    
    while True:
        msg = useful.formatHeader("What do you want to do now?")
        opt = ["CREATE a ROOM", "EDIT a ROOM", "REMOVE a ROOM",
               "CREATE an ITEM", "EDIT an ITEM", "REMOVE an ITEM",
               "SAVE STORY FILE", "SAVE AND EXIT", "EXIT WITHOUT SAVING"]
        
        answer = useful.showMenu(msg, opt)
        
        # User selected CREATE a ROOM
        if answer[1] == opt[0]:
            game.createRoom()
            print("Ok so far.")        

        # User selected EDIT a ROOM
        elif answer[1] == opt[1]:
            game.editRoom()

        # User selected REMOVE a ROOM
        elif answer[1] == opt[2]:
            game.removeRoom()

        # User selected CREATE an ITEM
        elif answer[1] == opt[3]:
            game.createItem()
        
        # User selected EDIT an ITEM
        elif answer[1] == opt[4]:
            game.editItem()
        
        # User selected REMOVE an ITEM
        elif answer[1] == opt[5]:
            game.removeItem()
        
        # User selected SAVE STORY FILE
        elif answer[1] == opt[6]:
            game.saveStory()
        
        # User selected SAVE AND EXIT
        elif answer[1] == opt[7]:
            game.saveStoryAndExit()
        
        # User selected EXIT WITHOUT SAVING
        elif answer[1] == opt[8]:
            break
            game.exitWithoutSave()
                
     
    #returns the modified game
    return game