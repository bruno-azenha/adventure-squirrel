import curses
import useful
def main(stdscr):

    # Initializes curses
    stdscr = curses.initscr() 

    # Changes terminal behavior
    #curses.noecho()     # Makes not printing to the screen the default
    #curses.cbreak()     # Catch keys pressed without return character
    #stdscr.keypad(True) # To get multibyte escape key sequences

    begin_x = 5; begin_y = 5
    nlines = 50; ncols = 50 
    win = curses.newwin(nlines, ncols, begin_y, begin_x)

    header = useful.formatHeader("Game") 
    stdscr.addstr(header)
    text = win.getstr()
    
    
    stdscr.refresh()
    text2 = win.getch()

    curses.endwin()
    # Reverts terminal behavior to normal
    #curses.nocbreak()
    #stdscr.keypad(False)
    #curses.echo()

    # Exit curses

# Does all of the above changes to terminal behavior on call
# Restore default config before return

curses.wrapper(main)
