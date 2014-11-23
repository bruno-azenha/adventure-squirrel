import curses
import time
import pdb

import sys
import useful
import gamesquirrel
import roomsquirrel
import itemsquirrel
import playersquirrel
import actionsquirrel

MENU_TOP = ["Start Game", "Load Game", "Exit Game"]

def main(screen):

    # Checks for the rght number of command line arguments
    if len(sys.argv) != 2:
        print ("Usage: " + sys.argv[0] + " <game_name>")
        time.sleep(2)
        sys.exit(1)

    # Name of the Story File
    storyFile = sys.argv[1] + ".pickle"
    savedStoryFile = sys.argv[1] + "_save.pickle"
    
    # Initialize curses
    screen = curses.initscr()
    curses.curs_set(False) # Removes blinking cursor

    header = "Adventure Squirrel"

    while True:
        screen.clear()
        # TOP MENU #     
        screen = useful.PrintHeader(header, screen, 0, 0) 
        screen = useful.PrintText("A text-based adventure game engine", screen, 4, 0)   
        screen = useful.PrintText("Story File: " + storyFile , screen, 5, 0)   
        selection = useful.ShowMenu(MENU_TOP, screen, 7, 0)
        # End TOP MENU #
        
        # Start New Game #
        if selection[0] == MENU_TOP[0]:
            screen.clear()
            GAME = useful.LoadStory(storyFile)
            if GAME == -1:
                screen.clear()
                question2 = "The Story file '" + storyFile + "' was not found."
                screen = useful.PrintHeader(header, screen, 0, 0)
                screen = useful.PrintText(question2, screen, 4, 0)
                screen.refresh()
                time.sleep(2) 
            else: 
                PlayGame(GAME, screen)
                break
        # END Start New Game #

        # Load Saved Game #
        elif selection[0] == MENU_TOP[1]:
            screen.clear()
            GAME = useful.LoadStory(savedStoryFile)
            if GAME == -1:
                screen.clear()
                question2 = "The Save file '" + savedStoryFile + "' was not found."
                screen = useful.PrintHeader(header, screen, 0, 0)
                screen = useful.PrintText(question2, screen, 4, 0)
                screen.refresh()
                time.sleep(2) 
            else:
                screen = useful.PrintText("The game has been loaded", screen, 4, 0)
                screen.refresh()
                time.sleep(2)
                PlayGame(GAME, screen)
                break
        # END Load Saved Game #                 

        # BEGIN EXIT THIS PROGRAM #
        else:
            screen.clear()
            screen = useful.PrintHeader(header, screen, 0, 0)
            screen = useful.PrintText("It was good to have you around!", screen, 4, 0)
            screen.refresh()
            time.sleep(2)
            break
        # END EXIT this program#

    curses.endwin()

def ShapeScreen(header, body, screen):
    screen = useful.PrintHeader(header, screen, 0, 0) 
    screen = useful.PrintText("Enter a command below: (or 'quit' to exit)", screen, 4, 0)   
    screen = useful.PrintText(">> ", screen, 6, 0)
    screen = useful.PrintText(body, screen, 8, 0)
    return screen

def PlayGame(GAME, screen):
    header = GAME.name
    body = GAME.credits
    
    while True:
        screen.clear()
        screen = ShapeScreen(header, body, screen)

        command = useful.GetInput(screen, 6, 3)
        command = command.lower()
        if command == "quit" or command == "exit" :
            break

        # clean up --> remove "the", "a", "an", "show"
        command_list = clean(command)
        response = ""
        # case <verb>
        if len(command_list) == 1: 
            
            # boolean type to indicate whether the action is successfully executed
            result, response = handleActionFormat1(GAME, command_list)
            #response += checkOK(GAME, command, result)

        # case <verb> <item>
        elif len(command_list) == 2:
            
            # boolean type to indicate whether the action is successfully executed
            result, response = handleActionFormat2(GAME, command_list)
            #response += checkOK(GAME, command, result)

        # case <verb> <preposition> <item>
        elif len(command_list) == 3:
            
            # boolean type to indicate whether the action is successfully executed
            result, response = handleActionFormat3(GAME, command_list)
            #response += checkOK(GAME, command, result)

        # case <verb> <item> <preposition> <item>
        elif len(command_list) == 4:
            # do something
            print("NOT IMPLEMENTED")
        
        # cannot find the action format
        else:
            screen = useful.PrintText("Sorry, I'm not quit sure what do you mean by \"" + command + "\"", screen, 8, 0)

        # Variable Changes for next screen print # 
        header = GAME.rooms[GAME.player.current_room].name
        body = response 
        # -------------------------------------- #
def clean(command):

    command_list = command.split(" ")

    while True:

        #remove "the"
        if "the" in command_list:
            command_list.remove("the")

        # remove "a"
        elif "a" in command_list:
            command_list.remove("a")

        # remove "an"
        elif "an" in command_list:
            command_list.remove("an")

        elif "show" in command_list:
            command_list.remove("show")
        else:
            break

    return command_list

def checkOK(GAME, command, result):

    if result == False:
        response  = "\nSorry, I couldn't undestand \""
        response += command
        response += "\" is not defined."

    elif result == True:
        response = "\nOK then, what's next?"

    return response

# handle the case <verb>
def handleActionFormat1(GAME, command_list):

    verb = command_list[0]
    
    clean_command_line = ""
    for word in command_list:
        clean_command_line += " " + word
    clean_command_line = clean_command_line[1:]

    # if it's not a verb but it's inventory
    inventory = ""
    if verb == "inventory":
        indecies = actionsquirrel.Inventory(GAME)
        for i in indecies:
            inventory += GAME.items[i].name + ", "
        response = inventory
        return True, response
    
    elif verb == "look":
        response = actionsquirrel.Look(GAME.player.current_room, GAME)[0]
        itemlist = "items: "
        for j in actionsquirrel.Look(GAME.player.current_room, GAME)[1]:
            itemlist += GAME.items[j].name + ", "
        response += "\n"+itemlist
        return True, response

    elif verb == "score":
        response = "Your score is: " + str(actionsquirrel.score(GAME))
        return True, response

    elif verb == "help":
        response = actionsquirrel.ShowHelp(GAME)
        return True, response

    elif verb == "save":
        if actionsquirrel.SaveGame(GAME, sys.argv[1]) is False:
            response = "did not save"
            return None, response
        else:
            response = "Game has been saved"
            return True, response

    elif verb == "pick" or verb == "take" or verb == "examine" or verb == "drop":
        response = "Sorry you need to add an item to "
        return None, response

    elif verb == "move" or verb == "go":
        response = "Sorry, you need to add a direction"
        return None, response

    elif verb == "combine":
        response = "Sorry you need to add two items"
        return None, response

    # else statement would not be executed if the for loop has been "break"
    # --> we cannot find the verb in default actions
    # --> let's search the customActions
    else:
        for action in GAME.customActions:
            if action.verb == clean_command_line:
                # then we execute the action
                returnList = action.execute(GAME)
                response = ""
                for item in returnList: 
                    response += item
                return True, response

        response = clean_command_line
        # we cannot find the action
        return False, response

# handle the case <verb> <item> or <verb> <direction>
def handleActionFormat2(GAME, command_list):

    DIRECTION_DICT = {"NORTH": ["north","n"], "NORTHEAST":
                    ["northeast", "ne"], "EAST": ["east","e"], "SOUTHEAST":
                    ["southeast","se"], "SOUTH": ["south","s"], "SOUTHWEST":
                    ["southwest","sw"], "WEST": ["west","w"], "NORTHWEST":
                    ["northwest","nw"], "UP": ["up"], "DOWN": ["down"],
                    "IN": ["in"], "OUT": ["out"]
            }
    KEYS = DIRECTION_DICT.keys()

    verb = command_list[0]
    item = command_list[1]

    clean_command_line = ""
    for word in command_list:
        clean_command_line += " " + word
    clean_command_line = clean_command_line[1:]
    
    if verb == "pick":
        for index in range(len(GAME.items)):
            if GAME.items[index].name.lower() == item.lower():
                if actionsquirrel.Pick(index, GAME) == True:
                    response = "You picked " + str(item) + " up."
                    return True, response
                else:
                    response = str(item)+ " is not pickable"
                    return None, response
        else:
            response = str(item)+ " does not exist"
            return None, response

    elif verb == "drop":
        for index in range(len(GAME.items)):
            if GAME.items[index].name.lower() == item.lower():
                if actionsquirrel.Drop(index, GAME) == True:
                    response = str(item)+ " was dropped"
                    return True, response
                else:
                    response = str(item)+ " is not dropable"
                    return None, response
        else:
            response = str(item)+ " does not exist"
            return None, response

    elif verb == "examine":
        for index in range(len(GAME.items)):
            if GAME.items[index].name.lower() == item.lower():
                description = actionsquirrel.Examine(index, GAME)
                response = description
                return True, response

        else:
            response = str(item)+ " does not exist"
            return None, response

    elif verb == "move" or verb == "go":
        direction = item
        for k in KEYS:
            if direction in DIRECTION_DICT[k]:
                result = actionsquirrel.Move(GAME, k)
                if result == False:
                    response = "Sorry cannot move to " + direction
                    return None, response
                elif result == True:
                    response = GAME.rooms[GAME.player.current_room].description
                    return True, response
        else:
            response = "Sorry, there is no such direction."
            return None, response
        
    elif verb == "combine":
        response = "Sorry you need an additional item to combine"
        return None, response

    elif verb == "look":
        response = "Sorry you can only use 'look' by itself"
        return None, response

    elif verb == "help":
        response = "Please just type 'help'"
        return None, response

    elif verb == "save":
        response = "Please just type 'save'"
        return None, response

    # --> we cannot find the verb in default actions
    # --> let's search the customActions
    else:
        response = ""
        for action in GAME.customActions:
            response += action.verb + " | " + clean_command_line + " | "
            if action.verb == clean_command_line:
                # then we execute the action
                returnList = action.execute(GAME)
                response = ""
                for item in returnList: 
                    response += item
                return True, response

        # we cannot find the action
        return False, str(len(clean_command_line))

# handle the case <verb> <preposition> <item>
def handleActionFormat3(GAME, command_list):
    
    verb = command_list[0]
    preposition = command_list[1]
    item = command_list[2]

    clean_command_line = ""
    for word in command_list:
        clean_command_line += " " + word
    clean_command_line = clean_command_line[1:]
    
    # if it's a default action
    for act in actionsquirrel.DEFAULT_ACTIONS:
        if act == verb:
            response = "Please just type \"" + verb + " " + item + "\""
            return None, response

    # if it's not a default action --> it's a custom action
    for action in GAME.customActions:
        if action.verb == clean_command_line:
            # then we execute the action
            returnList = action.execute(GAME)
            response = ""
            for item in returnList: 
                response += item
            return True, response

        # we cannot find the action
        response = "It failed."
        return False, response

# handle the case <verb> <item> <preposition> <item>
def handleActionFormat4(GAME, screen, command_list):
    
    verb = command_list[0]
    item1 = command_list[1]
    preposition = command_list[2]
    item2 = command_list[3]


# Wraps the curses changes to the terminal to prevent errors
curses.wrapper(main)
