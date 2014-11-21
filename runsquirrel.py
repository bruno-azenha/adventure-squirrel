import curses
import time

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

def PlayGame(GAME, screen):
    header = GAME.name
    while True:
        screen = useful.PrintHeader(header, screen, 0, 0) 
        screen = useful.PrintText("Enter a command below: (or 'quit' to exit)", screen, 4, 0)   
        screen = useful.PrintText(">> ", screen, 6, 0)   
        
        command = useful.GetInput(screen, 6, 3)
        command = command.lower()

        if command == "quit":
            break

        # clean up --> remove "the", "a", "an"
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
            # do something
            print("NOT IMPLEMENTED")

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

    for def_act in actionsquirrel.DEFAULT_ACTIONS:

        if verb == def_act:
            screen = useful.PrintText("Where(What) do you want to " + verb + "?", screen, 8, 0)
            return None
            break

    # else statement would not be executed if the for loop has been "break"
    # --> we cannot find the verb in default actions
    # --> let's search the customActions
    else:
        for action in GAME.customActions:
            if action.verb == verb:
                # then we execute the action
                action.execute()
                return True

        # we cannot find the action
        return False

# handle the case <verb> <item>
def handleActionFormat2(GAME, screen, command_list):

    verb = command_list[0]
    item = command_list[1]

    for def_act in actionsquirrel.DEFAULT_ACTIONS:

        if verb == def_act and verb == "pick":
            for index in range(len(GAME.items)):
                if GAME.items[index].name == item:
                    if actionsquirrel.Pick(index, GAME) == True:
                        return True
                    else:
                        screen = useful.PrintText(str(item)+" is not pickable", screen, 9, 0)
                        return None
            else:
                screen = useful.PrintText(str(item)+ " does not exist", screen, 9, 0)
                return None

        elif verb == def_act and verb == "drop":
            for index in range(len(GAME.items)):
                if GAME.items[index].name == item:
                    if actionsquirrel.Drop(index, GAME) == True:
                        return True
                    else:
                        screen = useful.PrintText(str(item)+" is not dropable", screen, 9, 0)
                        return None
            else:
                screen = useful.PrintText(str(item)+ " does not exist", screen, 9, 0)
                return None

        elif verb == def_act and verb == "examine":
            for index in range(len(GAME.items)):
                if GAME.items[index].name == item:
                    description = actionsquirrel.Examine(index, GAME)
                    screen = useful.PrintText(description, screen, 9, 0)
                    return True

            else:
                screen = useful.PrintText(str(item)+ " does not exist", screen, 9, 0)
                return None

        # ---------other default actions-----------
        # NOT YET IMPLEMENTED
        # ---------other default actions-----------

    # else statement would not be executed if the for loop has been "break"
    # --> we cannot find the verb in default actions
    # --> let's search the customActions
    else:
        for action in GAME.customActions:
            if action.verb == verb:
                # then we execute the action
                action.execute()
                return True

        # we cannot find the action
        return False


# Wraps the curses changes to the terminal to prevent errors
curses.wrapper(main)
