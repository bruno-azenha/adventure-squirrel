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

def defaultPrompt(header, screen):
    screen.clear()
    screen = useful.PrintHeader(header, screen, 0, 0) 
    screen = useful.PrintText("Enter a command below: (or 'quit' to exit)", screen, 4, 0)   
    screen = useful.PrintText(">> ", screen, 6, 0)
    screen.refresh()

def PlayGame(GAME, screen):
    header = GAME.name
    while True:
        useful.CleanHeader(screen) 
        header = GAME.rooms[GAME.player.current_room].name
        screen = useful.PrintHeader(header, screen, 0, 0) 
        screen = useful.PrintText("Enter a command below: (or 'quit' to exit)", screen, 4, 0)   
        screen = useful.PrintText(">> ", screen, 6, 0)   
        
        command = useful.GetInput(screen, 6, 3)
        defaultPrompt(header, screen)
        command = command.lower()

        if command == "quit" or command == "exit" :
            break

        # clean up --> remove "the", "a", "an", "show"
        command_list = clean(command)

        # case <verb>
        if len(command_list) == 1: 
            
            # boolean type to indicate whether the action is successfully executed
            result = handleActionFormat1(GAME, screen, command_list)
            response(GAME, screen, command_list, result)

        # case <verb> <item>
        elif len(command_list) == 2:
            
            # boolean type to indicate whether the action is successfully executed
            result = handleActionFormat2(GAME, screen, command_list)
            response(GAME, screen, command_list, result)

        # case <verb> <preposition> <item>
        elif len(command_list) == 3:
            
            # boolean type to indicate whether the action is successfully executed
            result = handleActionFormat3(GAME, screen, command_list)
            response(GAME, screen, command_list, result)

        # case <verb> <item> <preposition> <item>
        elif len(command_list) == 4:
            # do something
            print("NOT IMPLEMENTED")
        
        # cannot find the action format
        else:
            screen = useful.PrintText("Sorry, I'm not quit sure what do you mean by \"" + command + "\"", screen, 8, 0)

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

def response(GAME, screen, command_list, result):

    if result == False:
        response = "Sorry, " + "\""
        for i in command_list:
            response += i
        response += "\"" + " is not defined."

        screen = useful.PrintText(response, screen, 10, 0)

    elif result == True:
        response = "OK then, what's next?"
        screen = useful.PrintText(response, screen, 10, 0)

# handle the case <verb>
def handleActionFormat1(GAME, screen, command_list):

    verb = command_list[0]

    # if it's not a verb but it's inventory
    inventory = ""
    if verb == "inventory":
        indecies = actionsquirrel.Inventory(GAME)
        for i in indecies:
            inventory += GAME.items[i].name + ", "
        screen = useful.PrintText(inventory, screen, 8, 0)
        return True
    
    elif verb == "look":
        screen = useful.PrintText(actionsquirrel.Look(GAME.player.current_room, GAME)[0], screen, 8,0)
        itemlist = "items: "
        for j in actionsquirrel.Look(GAME.player.current_room, GAME)[1]:
            itemlist += GAME.items[j].name + ", "
        screen = useful.PrintText(itemlist, screen, 9,0)
        return None

    elif verb == "score":
        screen = useful.PrintText("Your score is: " + str(actionsquirrel.score(GAME)), screen, 8,0)
        return None

    elif verb == "help":
        screen = useful.PrintText(actionsquirrel.ShowHelp(GAME), screen, 8,0)
        return True

    elif verb == "save":
        actionsquirrel.SaveGame(GAME, sys.argv[1])
        screen = useful.PrintText("Game has been saved", screen, 8, 0)
        return None

    elif verb == "pick" or verb == "take" or verb == "examine" or verb == "drop":
        screen = useful.PrintText("Sorry you need to add an item to " + verb, screen, 8,0)
        return None

    elif verb == "move" or verb == "go":
        screen = useful.PrintText("Sorry, you need to add a direction", screen, 8, 0)
        return None

    elif verb == "combine":
        screen = useful.PrintText("Sorry you need to add two items", screen, 8,0)
        return None

    # else statement would not be executed if the for loop has been "break"
    # --> we cannot find the verb in default actions
    # --> let's search the customActions
    else:
        for action in GAME.customActions:
            if action.verb == verb:
                # then we execute the action
                action.execute(GAME)
                return True

        # we cannot find the action
        return False

# handle the case <verb> <item> or <verb> <direction>
def handleActionFormat2(GAME, screen, command_list):

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

    if verb == "pick":
        for index in range(len(GAME.items)):
            if GAME.items[index].name.lower() == item.lower():
                if actionsquirrel.Pick(index, GAME) == True:
                    screen = useful.PrintText(str(item) + " was added to inventory", screen, 9,0)
                    return True
                else:
                    screen = useful.PrintText(str(item)+ " is not pickable", screen, 9, 0)
                    return None
        else:
            screen = useful.PrintText(str(item)+ " does not exist", screen, 9, 0)
            return None

    elif verb == "drop":
        for index in range(len(GAME.items)):
            if GAME.items[index].name == item:
                if actionsquirrel.Drop(index, GAME) == True:
                    screen = useful.PrintText(str(item)+ " was dropped", screen, 9, 0)
                    return True
                else:
                    screen = useful.PrintText(str(item)+ " is not dropable", screen, 9, 0)
                    return None
        else:
            screen = useful.PrintText(str(item)+ " does not exist", screen, 9, 0)
            return None

    elif verb == "examine":
        for index in range(len(GAME.items)):
            if GAME.items[index].name.lower() == item.lower():
                description = actionsquirrel.Examine(index, GAME)
                screen = useful.PrintText(description, screen, 9, 0)
                return True

        else:
            screen = useful.PrintText(str(item)+ " does not exist", screen, 9, 0)
            return None

    elif verb == "move":
        direction = item
        for k in KEYS:
            if direction in DIRECTION_DICT[k]:
                result = actionsquirrel.Move(GAME, k)
                if result == False:
                    screen = useful.PrintText("Sorry cannot move to " + direction, screen, 9, 0)
                    return None
                elif result == True:
                    screen = useful.PrintText("Successfully move to " + direction, screen, 9, 0)
                    return None
        else:
            screen = useful.PrintText("Sorry no such direction.", screen, 9, 0)
            return None
        
    elif verb == "combine":
        screen = useful.PrintText("Sorry you need an additional item to combine", screen, 9, 0)
        return None

    elif verb == "look":
        screen = useful.PrintText("Sorry you can only use 'look' by itself", screen, 9, 0)
        return None

    elif verb == "help":
        screen = useful.PrintText("Please just type 'help'", screen, 8,0)
        return None

    elif verb == "save":
        screen = useful.PrintText("Please just type 'save'", screen, 8, 0)
        return None

    # --> we cannot find the verb in default actions
    # --> let's search the customActions
    else:
        for action in GAME.customActions:
            if action.verb == verb:
                # then we execute the action
                action.execute(GAME.player.current_room, GAME.player.inventory)
                return True

        # we cannot find the action
        return False

# handle the case <verb> <preposition> <item>
def handleActionFormat3(GAME, screen, command_list):
    
    verb = command_list[0]
    preposition = command_list[1]
    item = command_list[2]

    # if it's a default action
    for act in actionsquirrel.DEFAULT_ACTIONS:
        if act == verb:
            screen = useful.PrintText("Please just type \"" + verb + " " + item + "\"", screen, 8, 0)
            return None

    # if it's not a default action --> it's a custom action
    for action in GAME.customActions:
        if action.verb == verb:
            # then we execute the action
            action.execute(GAME.player.current_room, GAME.player.inventory)
            return True

        # we cannot find the action
        return False

# handle the case <verb> <item> <preposition> <item>
def handleActionFormat4(GAME, screen, command_list):
    
    verb = command_list[0]
    item1 = command_list[1]
    preposition = command_list[2]
    item2 = command_list[3]



# Wraps the curses changes to the terminal to prevent errors
curses.wrapper(main)
