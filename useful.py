#-------------------#
# showMenu()
# formatHeader()
# formatLinebreak()
# clearScreen()
# PrintHeader()
# PrintText()
# ShowMenu()
# GetInput()
# AskWithConfirm()
# Ask(()
# IsOnlyDigits()
#-------------------#

import readchar
import curses
import os
import pickle

#Constant to determine the line break of some of the functions
LINE_BREAK = 60

MENU_CONFIRM = ["YES", "NO"]

#This is a function that creates a menu for easier selection of options
#and returns the highlighted item. 
def showMenu( message, optionList ):
    
    # cursors
    UP = '\x1b\x5b\x41'
    DOWN = '\x1b\x5b\x42'
    ENTER = '\x0d'
    
    #Checks if there is at least one eelement in the list.
    if len(optionList) == 0 :
        return EMPTY_OPTION_LIST

    #Cursor position is an integer initially at the first element
    cursor = 0;

    clearScreen() 

    #This is the loop that prints the menu
    while True:
        print( message )
        current = 0;
        for item in optionList:
            if cursor == current:
                print('> ' + item)
            else:
                print(item)
            current += 1
 
        key = readchar.readkey()
        if key == 'a':
            break
        if key == UP:
            cursor = cursor-1 if cursor > 1 else 0
        
        if key == DOWN:
            cursor = cursor+1 if cursor < len(optionList)-1 else cursor

        if key == ENTER:
            clearScreen()
            # print('Selected: ' + str(optionList[cursor]))
            return cursor, optionList[cursor] 
 
        clearScreen()

# Function to provide nice header messages all around
def formatHeader(header_msg):
    length = len(header_msg)
    header = "/--"
    
    for i in range(length):
        header += "-"

    header += "--\\\n"
    header += "|  " + header_msg + "  |\n"
    header += "\\--"
    
    for i in range(length):
        header += "-"

    header += "--/\n"
    return header  

# Function that breaks lines on a long string in nice places 
# determined by the LINE_BREAK constant
def formatLinebreak(text, threshold=LINE_BREAK):
    
    # This will be the returned prettified text
    prettyText = ""

    # Split the text in words 
    words = text.split()

    wordIndex = 0
    charCount = 0
    while True:
        
        # Check if we got all the words 
        if wordIndex >= len(words) :
            break;

        charCount += len(words[wordIndex])
        
        # Check if the word fits in the line
        if charCount < threshold :
            prettyText += words[wordIndex] + " "
            
        else :
            charCount = len(words[wordIndex])
            prettyText += '\n' + words[wordIndex] + " "
            
        wordIndex += 1
    
    return prettyText        

     
def testFormatLinebreak():
    text = "This is a very long string that should have linke break and stuff, it is soo big that it is extra anoying to look at it. It is very very ugly! Seriously, what the fuck is this??? Makes me want to puke."

    prettyText = formatLinebreak(text, 30)
    prettyText2 = formatLinebreak(text)
    
    print(prettyText)
    print(prettyText2)

# Save pickle Story File
def SaveStory(GAME, screen):
        screen.clear()
        header = "Adventure Squirrel"
        question = "What will be the name of the file that contains the game information?"
       
        # Asks for file name and appends ".pickle" 
        filename = Ask(header, question, screen) 
        filename += ".pickle"

        with open(filename,'wb') as f:
            pickle.dump(GAME, f)

        print("\nThe game has been saved.")

def SaveGameWhilePlaying(GAME, screen):
    filename = GAME.name
    filename += "_save.pickle"
    with open(filename, 'wb') as f:
        pickle.dump(GAME, f)
    
    return True


# Loads a story file and returns a game or -1 in case of file not found
def LoadStory(filename):
    try:
        with open(filename,'rb') as f:
            GAME = pickle.load(f)
            return GAME

    except FileNotFoundError:
        return -1
    

# Function that prints the header in the given coordinates
# nice header messages all around
def PrintHeader(header_msg, screen, line, col):
    length = len(header_msg)\

    # First line of the header
    header1 = "/--"
    for i in range(length):
        header1 += "-"
    header1 += "--\\"
    screen.addstr(line, col, header1)
    
    # Second line of the header
    header2 = "|  " + header_msg + "  |"
    screen.addstr(line+1, col, header2)

    # Third line of the header    
    header3 = "\\--"
    for i in range(length):
        header3 += "-"
    header3 += "--/"
    screen.addstr(line+2, col, header3)

    return screen

def PrintText(text, screen, line, col):
    text = formatLinebreak(text)
    screen.addstr(line, col, text)
    return screen

# Function That turns on Echo for getting input
def GetInput(screen, line, col):
    curses.echo(True)
    curses.curs_set(True)
    text = screen.getstr(line, col).decode(encoding="utf-8")
    curses.echo(False)
    curses.curs_set(False)
    return text


#This is a function that creates a menu for easier selection of options
#and returns the highlighted item. 
def ShowMenu(menu, screen, lin, col):
    
    #Checks if there is at least one eelement in the list.
    if len(menu) == 0 :
        return -1

    #Cursor position is an integer initially at the first element
    cursor = 0; 

    #This is the loop that prints the menu
    while True:
        current = 0;
        for item in menu:
            if cursor == current:
                screen.addstr(lin+current, col, '> ' + item)
            else:
                screen.addstr(lin+current, col, item + "  ")
            current += 1    
 
        key = screen.getch()
        if key == curses.KEY_UP:
            cursor = cursor-1 if cursor > 1 else 0
        
        if key == curses.KEY_DOWN:
            cursor = cursor+1 if cursor < len(menu)-1 else cursor

        if key == 10:
            return (menu[cursor], cursor) 

def CleanHeader(screen):
    maxes = screen.getmaxyx()
    for i in range(maxes[1]):
        screen.addstr(0,i," ")
        screen.addstr(1,i," ")
        screen.addstr(2,i," ")

# Function that stays in the loop until the user confirms the input
def AskWithConfirm(header, question, screen):
    screen.clear()
    # Asks for it's name
    screen = PrintHeader(header, screen, 0, 0) 
    screen = PrintText(question, screen, 4, 0) 
    userInput = GetInput(screen, 6, 0)

    # Asks for confirmation 
    while True:
        screen.clear()
        screen = PrintHeader(header, screen, 0, 0) 
        checkText = "Is the following correct?  ---  " + userInput
        screen = PrintText(checkText, screen, 4, 0) 
        if ShowMenu(MENU_CONFIRM, screen, 6, 0 )[0] == "NO":
            screen.clear()
            # Asks for it's name again
            screen = PrintHeader(header, screen, 0, 0) 
            screen = PrintText(question, screen, 4, 0) 
            userInput = GetInput(screen, 6, 0)
        else:
            break 
    return userInput

# Ask without confirmation
def Ask(header, question, screen):
    screen.clear()
    # Asks for it's name
    screen = PrintHeader(header, screen, 0, 0) 
    screen = PrintText(question, screen, 4, 0) 
    userInput = GetInput(screen, 6, 0)
    return userInput

# Verifies if a string is convertable to an integer
def IsOnlyDigits(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
