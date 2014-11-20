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

        if command == "quit":
            break


# Wraps the curses changes to the terminal to prevent errors
curses.wrapper(main)
