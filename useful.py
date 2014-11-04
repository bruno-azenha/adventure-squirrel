import readchar
import os

#Constant to determine the line break of some of the functions
LINE_BREAK = 70

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

    os.system('clear') 

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
            os.system('clear')
            print('Selected: ' + str(optionList[cursor]))
            return cursor, optionList[cursor] 
 
        os.system('clear')

def test_showMenu():
    directions = ["north", "south", "east", "west",
                  "northeast", "northwest", "southeast",
                  "southwest", "up", "down", "in", "out"]

    direction, cursor = showMenu( "To which direction are you facing?", directions )

    print('Option: ' + direction)
    print('Index: ' + str(cursor))

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

def testFormatHeader():
    text = "This is a very pretty header"
    prettyHeader = formatHeader(text)
    print(prettyHeader)

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

