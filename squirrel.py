#
# main()
#

import pdb

import curses
import time

import useful
import gamesquirrel
import roomsquirrel
import itemsquirrel
import playersquirrel
import actionsquirrel


MENU_TOP = ["CREATE a new game", "EDIT a saved game", 
            "EXIT this program"]

MENU_WRITE_GAME = ["GAME", "ROOMS", "ITEMS", "PLAYER", "ACTIONS", "SAVE STORY FILE", 
                  "SAVE AND EXIT", "EXIT WITHOUT SAVING"]

MENU_PLAYER = ["DEFINE Starting Room", "DEFINE Starting Inventory", "BACK"]

MENU_PLAYER_INV = ["ADD Item", "REMOVE Item", "BACK"]

MENU_EDIT_GAME = ["CHANGE NAME", "WRITE HELP", "WRITE CREDITS", "BACK"]

MENU_ROOMS = ["ADD Room", "EDIT Room", "REMOVE Room", "BACK"]

MENU_ROOM_ITEM = ["ADD item to this Room", "REMOVE item from this Room", "BACK"]

MENU_EDIT_ROOM = ["NAME", "DESCRIPTION", "CONNECTIONS", "ITEMS", "BACK"]

MENU_ITEMS = ["ADD Item", "EDIT Item", "REMOVE Item", "BACK"]

MENU_EDIT_ITEM = ["NAME", "DESCRIPTION", "INVENTORY BEHAVIOR",
                  "PLACE ITEM", "BACK"]

MENU_ACTIONS = ["ADD Custom Action", "EDIT Custom Action", 
                "REMOVE Custom Action", "BACK"]

MENU_ACTION_FORMAT = ["<verb>", 
                      "<verb> <item>",
                      "<verb> <preposition> <item>",
                      "<verb> <item> <preposition> <item>"]

MENU_CONFIRM = ["YES", "NO"]

MENU_DIRS = ["NORTH", "NORTHEAST", "EAST", "SOUTHEAST", "SOUTH", "SOUTHWEST",
             "WEST", "NORTHWEST", "UP", "DOWN", "IN", "OUT", "-- BACK --"]

MENU_BUILDING_BLOCKS = ["Regular Move", "Change Score", "Display Text",
                       "Add Item to Inventory", "Drop Item from Inventory", 
                       "Remove Item from Inventory",  
                       "Add Item to Room", "Remove Item From Room"]
def main(screen):

    # Initialize curses
    screen = curses.initscr()
    curses.curs_set(False) # Removes blinking cursor


    header = "Adventure Squirrel"

    while True:
        screen.clear()
        # TOP MENU #     
        screen = useful.PrintHeader(header, screen, 0, 0) 
        screen = useful.PrintText("A text-based adventure game engine", screen, 4, 0)   
        selection = useful.ShowMenu(MENU_TOP, screen, 6, 0)
        # End TOP MENU #
        
        # BEGIN Create a new game #
        if selection[0] == MENU_TOP[0]:
            screen.clear()
            
            # Initialize the Game
            GAME = gamesquirrel.GameSquirrel()
            
            # Ask for the name of the game
            question = "What is the name of your game?"
            GAME.name = useful.AskWithConfirm(header, question, screen)

            WriteGame(GAME, screen)
            break
        # END Create a new game#

        # BEGIN EDIT a saved game #
        elif selection[0] == MENU_TOP[1]:
            screen.clear()
           
            question = "What is name of the pickle file that contains the game information?"
            # Ask for the name of the pickle file
            while True:
                filename = useful.Ask(header, question, screen)
                filename += ".pickle" 
                GAME = useful.LoadStory(filename)
                if GAME == -1:
                    screen.clear()
                    question2 = "The file '" + filename + "' was not found. Do you want to try a different one?."
                    screen = useful.PrintHeader(header, screen, 0, 0)
                    screen = useful.PrintText(question2, screen, 4, 0)
                    again = useful.ShowMenu(MENU_CONFIRM, screen, 6, 0)
                    if again[0] != "YES":
                        break
                    
                else: 
                    WriteGame(GAME, screen)
                    break
            if GAME != -1:
                break
        # END EDIT a saved game #                 

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

def WriteGame(GAME, screen):
    while True:
        screen.clear()
        # WRITE GAME MENU # 
        header = GAME.name
        screen = useful.PrintHeader(header, screen, 0, 0) 
        screen = useful.PrintText("What do you want do edit?", screen, 4, 0)   
        selection = useful.ShowMenu(MENU_WRITE_GAME, screen, 6, 0)
        # END WRITE GAME MENU #

        # GAME #
        if selection[0] == MENU_WRITE_GAME[0]:
            EditGame(GAME, screen)
        # END GAME #        

        # ROOMS #
        if selection[0] == MENU_WRITE_GAME[1]:
            WriteRooms(GAME, screen)
        # END ROOMS #

        # ITEMS #
        if selection[0] == MENU_WRITE_GAME[2]:
            WriteItems(GAME, screen)
        # END ITEMS #

        # PLAYER #
        if selection[0] == MENU_WRITE_GAME[3]:
            WritePlayer(GAME, screen)
        # END PLAYER #
        
        # ACTIONS #
        if selection[0] == MENU_WRITE_GAME[4]:
            WriteActions(GAME, screen)
        # END ACTIONS # 
        
        # SAVE STORY FILE #
        if selection[0] == MENU_WRITE_GAME[5]:
            useful.SaveStory(GAME, screen)
            time.sleep(2)
        # END SAVE STORY FILE #

        # SAVE AND EXIT #
        if selection[0] == MENU_WRITE_GAME[6]:
            useful.SaveStory(GAME, screen)
            time.sleep(2)
            break
        # END SAVE AND EXIT #

        # EXIT WITHOUT SAVING #
        if selection[0] == MENU_WRITE_GAME[7]:
            break
        # END EXIT WITHOUT SAVING #

def EditGame(GAME, screen):
    while True: 
        screen.clear()

        # GAME MENU #
        header = GAME.name
        screen = useful.PrintHeader(header, screen, 0, 0)
        screen = useful.PrintText("What do you want to do?", screen, 4, 0)
        selection = useful.ShowMenu(MENU_EDIT_GAME, screen, 6, 0)
        # END GAME MENU #

        # CHANGE NAME #
        if selection[0] == MENU_EDIT_GAME[0]:
            screen.clear()
            question = "What is the new name of your game?"
            GAME.name = useful.AskWithConfirm(header, question, screen)
        # END CHANGE NAME #

        # WRITE HELP #
        if selection[0] == MENU_EDIT_GAME[1]:
            question = "Write the HELP information."
            GAME.instructions = useful.AskWithConfirm(header, question, screen)
        # END WRITE HELP "
        
        # WRITE CREDITS #
        if selection[0] == MENU_EDIT_GAME[2]:
            question = "Write the CREDITS."
            GAME.credits = useful.AskWithConfirm(header, question, screen)
        # END WRITE CREDITS "

        # BACK #
        if selection[0] == MENU_EDIT_GAME[3]:
            break
        # END BACK #
        

def WriteRooms(GAME, screen):
    while True:
        screen.clear()

        # ROOMS MENU #
        header = GAME.name
        screen = useful.PrintHeader(header, screen, 0, 0)
        screen = useful.PrintText("What do you want to do?", screen, 4, 0)
        selection = useful.ShowMenu(MENU_ROOMS, screen, 6, 0)
        # END ROOMS MENU #

        # ADD ROOM #
        if selection[0] == MENU_ROOMS[0]:
            AddRoom(GAME, screen)
        # END ADD ROOM #

        # EDIT ROOM #
        if selection[0] == MENU_ROOMS[1]:
            EditRoom(GAME, screen)
        # END EDIT ROOM "
        
        # REMOVE ROOM #
        if selection[0] == MENU_ROOMS[2]:
            RemoveRoom(GAME, screen)
        # END REMOVE ROOM "

        # BACK #
        if selection[0] == MENU_ROOMS[3]:
            break
        # END BACK #

def AddRoom(GAME, screen): 

    # Get the name of the room
    screen.clear()
    header = GAME.name
    question = "What is the name of this room?"
    name = useful.AskWithConfirm(header, question, screen)

    # Get the description of the room
    screen.clear()
    header = name
    question = "What is the description of this room? ('Look' action)"
    description = useful.AskWithConfirm(header, question, screen)

    Room = roomsquirrel.RoomSquirrel(name, description)
    GAME.rooms.append(Room)

def EditRoom(GAME, screen): 
    while True:
        screen.clear()

        # Chose Room to Edit
        header = GAME.name
        question = "Which room would you like to edit?"
        screen = useful.PrintHeader(header, screen, 0, 0)
        screen = useful.PrintText(question, screen, 4, 0)
        
        RoomMenu = [(r.name) for r in GAME.rooms]
        RoomMenu.append("BACK")
        roomselected = useful.ShowMenu(RoomMenu, screen, 6, 0)
    
        if roomselected[0] == "BACK":
            break

        else:
            while True:
                screen.clear()
                room = GAME.rooms[roomselected[1]]
                header = room.name
                name = "Name: " + room.name
                description = "Description: " + room.description
                
                currentLine = 0 
                screen = useful.PrintHeader(header, screen, currentLine, 0)
                screen = useful.PrintText(name, screen, currentLine + 4, 0)
                screen = useful.PrintText(description, screen, currentLine + 5, 0)

                # Print items in the room
                screen = useful.PrintText("Items in this room:", screen, currentLine + 7, 0)
                itemNameList = []
                currentLine = 8
                for itemIndex in room.items:
                    itemNameList.append(GAME.items[itemIndex].name)
                    screen = useful.PrintText(GAME.items[itemIndex].name, screen, currentLine, 0)
                    currentLine += 1

                currentLine += 1 

                # Print connections of the room
                screen = useful.PrintText("Connections:", screen, currentLine, 0)
                currentLine += 1
                connectionList = []
                for i in range(len(MENU_DIRS)-1): # -1 because MENU_DIRS has -- BACK --
                    if room.connections[i] < 0:
                        connectionList.append(MENU_DIRS[i] + ":")
                    else:
                        connectionList.append(MENU_DIRS[i] + ": " + GAME.rooms[room.connections[i]].name )
                    screen = useful.PrintText(connectionList[i], screen, currentLine, 0)
                    currentLine += 1


                question = "What would you like to change?"            
                screen = useful.PrintText(question, screen, currentLine + 1, 0)
                selection = useful.ShowMenu(MENU_EDIT_ROOM, screen, currentLine + 3, 0)

                # EDIT NAME #
                if selection[0] == MENU_EDIT_ROOM[0]:
                    screen.clear()
                    question = "What is the new name of this room?"
                    name = useful.AskWithConfirm(header, question, screen)
                    GAME.rooms[roomselected[1]].name = name # roomselected[1] is the index 
                    header = name                            # of the selected room
                # END EDIT NAME #

                # EDIT DESCRIPTION #
                elif selection[0] == MENU_EDIT_ROOM[1]:
                    screen.clear()
                    question = "What is the new description of this room?"
                    description = useful.AskWithConfirm(header, question, screen)
                    GAME.rooms[roomselected[1]].description = description
                # END EDIT DESCRIPTION #

                # EDIT CONNECTIONS #
                elif selection[0] == MENU_EDIT_ROOM[2]:
                    screen.clear()
                    question = "Which direction do you want to edit?"
                    screen = useful.PrintHeader(header, screen, 0, 0)
                    screen = useful.PrintText(question, screen, 4, 0)
                    
                    connectionEditList = connectionList
                    connectionEditList.append("-- BACK --")
                    selectedDirection = useful.ShowMenu(connectionEditList, screen, 6, 0)
                    if selectedDirection[0] == "-- BACK --":
                        continue
                    else:
                        EditRoomConnection(GAME, screen, roomselected[1], selectedDirection[1])
                    
                # END EDIT CONNECTIONS #

                # EDIT ITEMS #
                elif selection[0] == MENU_EDIT_ROOM[3]:
                    while True:
                        screen.clear()
                        question = "What do you want to do?"
                        screen = useful.PrintHeader(header, screen, 0, 0)
                        screen = useful.PrintText(question, screen, 4, 0)
                        selectedOption = useful.ShowMenu(MENU_ROOM_ITEM, screen, 6, 0)
                        
                        if selectedOption[0] == "ADD item to this Room":
                            AddItemToRoom(GAME, screen, roomselected[1])

                        elif selectedOption[0] == "REMOVE item from this Room":
                            RemoveItemFromRoom(GAME, screen, roomselected[1])
                   
                        elif selectedOption[0] == "BACK":
                            break

                # END EDIT ITEMS #

                elif selection[0] == "BACK":
                    break
        
def EditRoomConnection(GAME, screen, room, direction):
    while True:
        screen.clear()

        # Chose Room to Edit
        header = GAME.rooms[room].name
        question = "Which room would you like to connect through direction " + MENU_DIRS[direction] + "?"
        screen = useful.PrintHeader(header, screen, 0, 0)
        screen = useful.PrintText(question, screen, 4, 0)
        
        RoomMenu = [(r.name) for r in GAME.rooms]
        RoomMenu.append("BACK")
        roomselected = useful.ShowMenu(RoomMenu, screen, 6, 0)
    
        if roomselected[0] == "BACK":
            break

        else:
            GAME.EditConnection(room, roomselected[1], direction)
            break

def RemoveRoom(GAME, screen):
    while True:
        screen.clear()

        # Chose Room to Remove
        header = GAME.name
        question = "Which room would you like to remove?"
        screen = useful.PrintHeader(header, screen, 0, 0)
        screen = useful.PrintText(question, screen, 4, 0)
        
        RoomMenu = [(r.name) for r in GAME.rooms]
        RoomMenu.append("BACK")
        selection = useful.ShowMenu(RoomMenu, screen, 6, 0)
     
        if selection[0] == "BACK":
            break

        else:            
            screen.clear()
            
            header = GAME.name
            question = "Are you sure you want to REMOVE " + selection[0] + "?"
            question += "\nNotice: All the items in this room will be placed at NOWHERE."
            screen = useful.PrintHeader(header, screen, 0, 0)
            screen = useful.PrintText(question, screen, 4, 0)
            if useful.ShowMenu(MENU_CONFIRM, screen, 6, 0)[0] == "YES":
                
                # remove the room from the game class
                GAME.removeRoom(selection[1])
  
def WriteItems(GAME, screen):
    while True:    
        screen.clear()

        # ITEMS MENU #
        header = GAME.name
        screen = useful.PrintHeader(header, screen, 0, 0)
        screen = useful.PrintText("What do you want to do?", screen, 4, 0)
        selection = useful.ShowMenu(MENU_ITEMS, screen, 6, 0)
        # END ITEMS MENU #
    
        # ADD ITEM #
        if selection[0] == MENU_ITEMS[0]:
            AddItem(GAME, screen, 0)
        # END ADD ITEM #

        # EDIT ITEM #
        elif selection[0] == MENU_ITEMS[1]:
            EditItem(GAME, screen)
        # END EDIT ITEM "
        
        # REMOVE ITEM #
        elif selection[0] == MENU_ITEMS[2]:
            RemoveItem(GAME, screen)
        # END REMOVE ITEM "

        # BACK #
        elif selection[0] == MENU_ITEMS[3]:
            break
        # END BACK #

def AddItemToRoom(GAME, screen, roomIndex):
    
    # Gets a list with all items not yet placed
    itemsIndexes = GAME.GetNotPlacedItems()

    itemsMenu = []
    for i in itemsIndexes:
        itemsMenu.append(GAME.items[i].name)
    itemsMenu.append("NEW ITEM")
    itemsMenu.append("BACK")
    
    screen.clear()
    screen = useful.PrintHeader(GAME.rooms[roomIndex].name, screen, 0, 0)
    question = "Select the item to ADD to this room"
    screen = useful.PrintText(question, screen, 4, 0)
    itemselected = useful.ShowMenu(itemsMenu, screen, 6, 0)

    if itemselected[0] == "BACK":
        return 0

    if itemselected[0] == "NEW ITEM":
        AddItem(GAME, screen, 1)
        GAME.PlaceItem(len(GAME.items)-1, roomIndex)
       
    else:  
        GAME.PlaceItem(itemsIndexes[itemselected[1]], roomIndex)
                            
def RemoveItemFromRoom(GAME, screen, roomIndex):
    itemsIndexes = GAME.rooms[roomIndex].items

    itemsMenu = []
    for i in itemsIndexes:
        itemsMenu.append(GAME.items[i].name)
    itemsMenu.append("BACK")

    screen.clear()
    screen = useful.PrintHeader(GAME.rooms[roomIndex].name, screen, 0, 0)
    question = "Select the item to REMOVE from this room"
    screen = useful.PrintText(question, screen, 4, 0)
    itemselected = useful.ShowMenu(itemsMenu, screen, 6, 0)

    if itemselected[0] != "BACK":
        GAME.UnplaceItem(itemsIndexes[itemselected[1]], roomIndex)


def AddItem(GAME, screen, fromRoomFlag):

    # Ask for the name of the item
    screen.clear()
    header = GAME.name
    question = "What is the name of this item?"
    name = useful.AskWithConfirm(header, question, screen)

    # Ask for the description of the item
    screen.clear()
    header = name
    question = "What is the description of this item? ('Look' action)"
    description = useful.AskWithConfirm(header, question, screen)

    # Pickable?
    screen.clear()
    question = "Can the user pick this item up?";
    screen = useful.PrintHeader(header, screen, 0, 0)
    screen = useful.PrintText(question, screen, 4, 0)
    if useful.ShowMenu(MENU_CONFIRM, screen, 6, 0)[0] == "YES":
        isPickable = True

        # Droppable? 
        screen.clear()
        question = "Can the user drop this item from his inventory?";
        screen = useful.PrintHeader(header, screen, 0, 0)
        screen = useful.PrintText(question, screen, 4, 0)
        if useful.ShowMenu(MENU_CONFIRM, screen, 6, 0)[0] == "YES":
            isDroppable = True
        else: 
            isDroppable = False
    else:
        isPickable = False
        isDroppable = False

    newItem = itemsquirrel.ItemSquirrel(name, description, isPickable, isDroppable)
    
    if fromRoomFlag == 0:
        # which room does it belong to?
        screen.clear()
        question = "What is the initial placement of this item??"
        screen = useful.PrintHeader(header, screen, 0, 0)
        screen = useful.PrintText(question, screen, 4, 0)
        
        RoomMenu = [(r.name) for r in GAME.rooms]
        RoomMenu.append("Player Inventory")
        RoomMenu.append("NOWHERE")
        roomselected = useful.ShowMenu(RoomMenu, screen, 6, 0)

        # if it belongs to no room, we simply append it to the item list
        if roomselected[0] == "NOWHERE":
            GAME.AddItem(newItem)

        elif roomselected[0] == "Player Inventory":
            GAME.AddItem(newItem)
            GAME.PlaceItem(len(GAME.items)-1, -2)

        # if it belongs to a specific room, then we set the location attribute of this item
        else:
            # roomselected[1] is actual room index in GAME.rooms
            GAME.AddItem(newItem)
            GAME.PlaceItem(len(GAME.items)-1, roomselected[1])
    
    else:
        GAME.AddItem(newItem)

def EditItem(GAME, screen):
        while True:
            screen.clear()
            # Chose Item to Edit
            header = GAME.name
            question = "Which item would you like to edit?"
            screen = useful.PrintHeader(header, screen, 0, 0)
            screen = useful.PrintText(question, screen, 4, 0)
            
            ItemMenu = [(i.name) for i in GAME.items]
            ItemMenu.append("BACK")
            itemselected = useful.ShowMenu(ItemMenu, screen, 6, 0)
        
            if itemselected[0] == "BACK":
                break

            else:
            
                while True:
                    screen.clear()
                    item = GAME.items[itemselected[1]]
                    header = item.name
                    name = "Name: " + item.name
                    description = "Description: " + item.description
                    pickable = "Is Pickable: " + str(item.isPickable)
                    droppable = "Is Droppable: " + str(item.isDroppable)
                    if item.whereIs == -1:
                        place = "Place: NOT SET"
                    elif item.whereIs == -2:
                        place = "Place: PLAYER INVENTORY"
                    else:
                        place = "Place: " + GAME.rooms[item.whereIs].name

                    screen = useful.PrintHeader(header, screen, 0, 0)
                    screen = useful.PrintText(name, screen, 4, 0)
                    screen = useful.PrintText(description, screen, 5, 0)
                    screen = useful.PrintText(pickable, screen, 6, 0)
                    screen = useful.PrintText(droppable, screen, 7, 0)
                    screen = useful.PrintText(place, screen, 8, 0)
                    question = "What would you like to change??"            
                    screen = useful.PrintText(question, screen, 10, 0) 
                    
                    selected = useful.ShowMenu(MENU_EDIT_ITEM, screen, 12, 0)

                    # EDIT NAME #
                    if selected[0] == MENU_EDIT_ITEM[0]:
                        screen.clear()
                        question = "What is the new name of this item?"
                        name = useful.AskWithConfirm(header, question, screen)
                        GAME.items[itemselected[1]].name = name
                        header = name                
                    # END EDIT NAME #

                    # EDIT DESCRIPTION #
                    elif selected[0] == MENU_EDIT_ITEM[1]:
                        screen.clear()
                        question = "What is the new description of this item?"
                        description = useful.AskWithConfirm(header, question, screen)
                        GAME.items[itemselected[1]].description = description                    
                    # END EDIT DESCRIPTION #

                    # INVENTORY BEHAVIOR #
                    elif selected[0] == MENU_EDIT_ITEM[2]:
                        # Pickable?
                        screen.clear()
                        question = "Can the user pick this item up?";
                        screen = useful.PrintHeader(header, screen, 0, 0)
                        screen = useful.PrintText(question, screen, 4, 0)
                        if useful.ShowMenu(MENU_CONFIRM, screen, 6, 0)[0] == "YES":
                            isPickable = True
                 
                            # Droppable? 
                            screen.clear()
                            question = "Can the user drop this item from his inventory?";
                            screen = useful.PrintHeader(header, screen, 0, 0)
                            screen = useful.PrintText(question, screen, 4, 0)
                            if useful.ShowMenu(MENU_CONFIRM, screen, 6, 0)[0] == "YES":
                                isDroppable = True
                            else: 
                                isDroppable = False
                        else:
                            isPickable = False
                            isDroppable = False
                        GAME.items[itemselected[1]].isPickable = isPickable
                        GAME.items[itemselected[1]].isDroppable = isDroppable
                            
                    # END INVENTORY BEHAVIOR #

                    # PLACE ITEM #
                    elif selected[0] == MENU_EDIT_ITEM[3]:
                        # Select room in which to place item
                        screen.clear()
                        question = "Where would you like to put this item?"
                        screen = useful.PrintHeader(header, screen, 0, 0)
                        screen = useful.PrintText(question, screen, 4, 0)
                        
                        RoomMenu = [(r.name) for r in GAME.rooms]
                        if item.isPickable == True:
                            RoomMenu.append("PLAYER INVENTORY")
                        RoomMenu.append("NOWHERE")
                        RoomMenu.append("BACK")
                        roomselected = useful.ShowMenu(RoomMenu, screen, 6, 0)
                   
                        if roomselected[0] == "BACK":
                            break

                        elif roomselected[0] == "PLAYER INVENTORY":
                            # HERE I'M USING -2 TO MARK PLAYER INVENTORY
                            GAME.PlaceItem(itemselected[1], -2)
                   
                        elif roomselected[0] == "NOWHERE":
                            GAME.PlaceItem(itemselected[1], -1)
                        else:
                            GAME.PlaceItem(itemselected[1], roomselected[1])
                            
                    # END PLACE ITEM #
          
                    # Exit menu 
                    elif selected[0] == "BACK":
                        break

def RemoveItem(GAME, screen):
    while True:
        screen.clear()

        # Chose Item to Remove
        header = GAME.name
        question = "Which item would you like to remove?"
        screen = useful.PrintHeader(header, screen, 0, 0)
        screen = useful.PrintText(question, screen, 4, 0)
        
        ItemMenu = [(i.name) for i in GAME.items]
        ItemMenu.append("BACK")
        selection = useful.ShowMenu(ItemMenu, screen, 6, 0)
     
        if selection[0] == "BACK":
            break

        else:            
            screen.clear()
            
            header = GAME.name
            question = "Are you sure you want to REMOVE " + selection[0] + "?"
            screen = useful.PrintHeader(header, screen, 0, 0)
            screen = useful.PrintText(question, screen, 4, 0)
            if useful.ShowMenu(MENU_CONFIRM, screen, 6, 0)[0] == "YES":
                
                GAME.RemoveItem(selection[1])

def WritePlayer(GAME, screen):
    while True:
        screen.clear()

        # PLAYER MENU #
        header = GAME.name
        screen = useful.PrintHeader(header, screen, 0, 0)
        screen = useful.PrintText("What do you want to do?", screen, 4, 0)
        selection = useful.ShowMenu(MENU_PLAYER, screen, 6, 0)
        # END PLAYER MENU #

        # DEFINE Starting Room #
        if selection[0] == MENU_PLAYER[0]:
            DefineStartRoom(GAME, screen)
        # END DEFINE Starting Room #

        # DEFINE Starting Inventory #
        elif selection[0] == MENU_PLAYER[1]:
            DefineStartInventory(GAME, screen)
        # END DEFINE Starting Inventory #
 
        # BACK #
        else: # selection[0] == "BACK":
            break

def DefineStartRoom(GAME, screen):
    screen.clear()

    # STARTING ROOM CHOICE MENU#
    header = GAME.name
    screen = useful.PrintHeader(header, screen, 0, 0)
    question = "What do you want to be the room the player starts in?";
    screen = useful.PrintText(question, screen, 4, 0)
    
    roomMenu = [(r.name) for r in GAME.rooms]
    roomMenu.append("BACK")

    roomselected = useful.ShowMenu(roomMenu, screen, 6, 0)
    # END STARTING ROOM CHOICE MENU #

    if roomselected[0] != "BACK":
        GAME.DefinePlayerStart(roomselected[1])
        
def DefineStartInventory(GAME, screen):
    while True:
        screen.clear()
        header = "Starting Inventory"
        question = "What do you want to do?" 
        screen = useful.PrintHeader(header, screen, 0, 0)
        screen = useful.PrintText(question, screen, 4, 0)

        currentLine = 10
        # Print items in the inventory
        screen = useful.PrintText("Items:", screen, currentLine, 0)
        currentLine += 1
        itemNameList = []
        for itemIndex in GAME.player.inventory:
            itemNameList.append(GAME.items[itemIndex].name)
            screen = useful.PrintText(GAME.items[itemIndex].name, screen, currentLine, 0)
            currentLine += 1

        currentLine += 1 

        selection = useful.ShowMenu(MENU_PLAYER_INV, screen, 6, 0)
        # ADD ITEM #
        if selection[0] == MENU_PLAYER_INV[0]:
            screen.clear()
            question = "Which item should be added to the player's starting inventory?"
            
            itemsIndexes = GAME.GetNotPlacedItems()
            itemsMenu = []
            for i in itemsIndexes:
                itemsMenu.append(GAME.items[i].name)
            itemsMenu.append("BACK")
            
            screen = useful.PrintHeader(header, screen, 0, 0)
            screen = useful.PrintText(question, screen, 4, 0)
            itemselected = useful.ShowMenu(itemsMenu, screen, 6, 0)

            if itemselected[0] != "BACK":
                GAME.PlaceItem(itemsIndexes[itemselected[1]], -2)

        # REMOVE ITEM
        if selection[0] == MENU_PLAYER_INV[1]:
            screen.clear()
            question = "Which item should be removed from the player's starting inventory?"
            
            itemsIndexes = []
            itemsMenu = []
            index = 0
            for i in GAME.player.inventory:
                itemsMenu.append(GAME.items[i].name)
                itemsIndexes.append(GAME.player.inventory[index])
                index += 1
            itemsMenu.append("BACK")
            
            screen = useful.PrintHeader(header, screen, 0, 0)
            screen = useful.PrintText(question, screen, 4, 0)
            itemselected = useful.ShowMenu(itemsMenu, screen, 6, 0)

            if itemselected[0] != "BACK":
                GAME.UnplaceItem(itemsIndexes[itemselected[1]], -2)
    
        # BACK #
        if selection[0] == "BACK":
            break

def WriteActions(GAME, screen):
    while True:
        screen.clear()

        # ACTIONS MENU #
        header = GAME.name
        screen = useful.PrintHeader(header, screen, 0, 0)
        screen = useful.PrintText("What do you want to do?", screen, 4, 0)
        selection = useful.ShowMenu(MENU_ACTIONS, screen, 6, 0)
        # END ROOMS MENU #

        # ADD CUSTOM ACTION #
        if selection[0] == MENU_ACTIONS[0]:
            AddCustomAction(GAME, screen)
        # END ADD CUSTOM ACTION #

        # ADD COMBINE ITEM ACTION #
        if selection[0] == MENU_ACTIONS[1]:
            AddCombineAction(GAME, screen)
        # END ADD COMBINE ITEM ACTION #

        # EDIT CUSTOM ACTION #
        if selection[0] == MENU_ACTIONS[1]:
            EditCustomAction(GAME, screen)
        # END EDIT CUSTOM ACTION "
        
        # REMOVE CUSTOM ACTION #
        if selection[0] == MENU_ACTIONS[2]:
            RemoveCustomAction(GAME, screen)
        # END REMOVE CUSTOM ACTION "

        # BACK #
        if selection[0] == MENU_ACTIONS[3]:
            break
        # END BACK #

MENU_BULDING_BLOCKS = ["Regular Move", "Change Score", "Display Text",
                       "Add Item to Inventory", "Drop Item from Inventory", 
                       "Remove Item from inventory",  
                       "Add item to Room", "Remove Item From Room", ]

def AddCustomAction(GAME, screen): 

    # Get the verb of the action
    screen.clear()
    header = GAME.name
    question = "What is the verb associated with this action?"
    verb = useful.AskWithConfirm(header, question, screen)

    # Get the format of the action
    screen.clear()
    header = verb
    question = "What is the format of this action?"
    screen = useful.PrintHeader(header, screen, 0, 0)
    screen = useful.PrintText(question, screen, 4, 0)
    selectedformat = useful.ShowMenu(MENU_ACTION_FORMAT, screen, 6, 0)

    # To which room is this action bound?
    screen.clear()
    header = verb
    question = "To which room is this action bound?"
    screen = useful.PrintHeader(header, screen, 0, 0)
    screen = useful.PrintText(question, screen, 4, 0)
    
    roomMenu = [(r.name) for r in GAME.rooms]
    roomMenu.append("NOT ROOM BOUND")
    roomselected = useful.ShowMenu(roomMenu, screen, 6, 0)
    
    if roomselected[0] == "NOT ROOM BOUND":
        roomBound = False
    else:
        roomBound = roomselected[1]

    # To which item is this action bound?
    screen.clear()
    header = verb
    question = "To which item is this action bound?"
    screen = useful.PrintHeader(header, screen, 0, 0)
    screen = useful.PrintText(question, screen, 4, 0)
    
    pickableItems = GAME.GetPickableItems()
    itemMenu = []
    for item in pickableItems:
        itemMenu.append(GAME.items[item].name) 
    itemMenu.append("NOT ITEM BOUND")
    itemselected = useful.ShowMenu(itemMenu, screen, 6, 0)
    
    if itemselected[0] == "NOT ITEM BOUND":
        itemBound = False
    else:
        itemBound = pickableItems[itemselected[1]]

    # <verb>
    if selectedformat[0] == MENU_ACTION_FORMAT[0]:
        listFuns, listArgs = ChooseBehaviors(GAME, screen, verb)                
        
    # <verb> <item>        

    customAction = actionsquirrel.CustomAction(verb, roomBound, itemBound, 
                                               listFuns, listArgs, )
    GAME.customActions.append(customAction)

def ChooseBehaviors(GAME, screen, verb):
    
    listOfFunctions = []
    listOfArguments = []
    while True:
        screen.clear()
        header = verb
        question = "What behavior would you like to add to your action?"
        screen = useful.PrintHeader(header, screen, 0, 0)
        screen = useful.PrintText(question, screen, 4, 0)
        selectedblock = useful.ShowMenu(MENU_BUILDING_BLOCKS, screen, 6, 0)

        if selectedblock[0] == "Regular Move":
            fun, arg = AddBlockRegMove(GAME, screen, verb)    
        
        elif selectedblock[0] == "Change Score":
            fun, arg = AddBlockChangeScore(GAME, screen, verb)

        elif selectedblock[0] == "Display Text":
            fun, arg = AddBlockDisplayText(GAME, screen, verb)
        
        elif selectedblock[0] == "Add Item to Inventory":
            fun, arg = AddBlockAddItemToInv(GAME, screen, verb)
        
        elif selectedblock[0] == "Drop Item from Inventory":
            fun, arg = AddBlockDropItemFromInv(GAME, screen, verb)

        elif selectedblock[0] == "Remove Item from Inventory":
            fun, arg = AddBlockRemoveItemFromInv(GAME, screen, verb)

        elif selectedblock[0] == "Add Item to Room":
            fun, arg = AddBlockAddItemToRoom(GAME, screen, verb)

        else: # selectedblock[0] == "Remove Item from Room":
            fun, arg = AddBlockRemoveItemFromRoom(GAME, screen, verb)
        
        if fun != False: 
            listOfFunctions.append(fun)
            listOfArguments.append(arg)

            # Asks if the user wants to add another behavior
            screen.clear()
            header = GAME.name
            question = "Do you want to add another behavior?"
            screen = useful.PrintHeader(header, screen, 0, 0)
            screen = useful.PrintText(question, screen, 4, 0)
            if (useful.ShowMenu(MENU_CONFIRM, screen, 6, 0)[0] == "NO"):
                break

    return listOfFunctions, listOfArguments

def AddBlockRegMove(GAME, screen, verb):
    screen.clear()
    header = verb
    question = "Where does this action move the player to?"
    screen = useful.PrintHeader(header, screen, 0, 0)
    screen = useful.PrintText(question, screen, 4, 0)
    
    RoomMenu = [(r.name) for r in GAME.rooms]
    RoomMenu.append("BACK")
    roomselected = useful.ShowMenu(RoomMenu, screen, 6, 0)

    if roomselected[0] == "BACK":
        return False, False
    return actionsquirrel.RegularMove, roomselected[0]

def AddBlockChangeScore(GAME, screen, verb):
    screen.clear()
    header = verb
    question = "How many points does the player gain? (Only Digits)"
    
    while True:
        points = useful.AskWithConfirm(header, question, screen)
        if useful.IsOnlyDigits(points):
            break

    return actionsquirrel.ChangeScore, int(points)  
        
def AddBlockDisplayText(GAME, screen, verb):
    screen.clear()
    header = verb
    question = "What text do you want to be displayed?"
    
    text = useful.AskWithConfirm(header, question, screen)

    return actionsquirrel.DisplayText, text  

def AddBlockAddItemToInv(GAME, screen, verb):
    screen.clear()
    header = verb
    question = "Which item should be added to the player's inventory?"
    screen = useful.PrintHeader(header, screen, 0, 0)
    screen = useful.PrintText(question, screen, 4, 0)
    
    pickableItemsIndexes = GAME.GetPickableItems()
    itemMenu = []
    for item in pickableItemsIndexes:
        itemMenu.append(GAME.items[item].name)
    itemMenu.append("BACK")

    itemselected = useful.ShowMenu(itemMenu, screen, 6, 0)

    if itemselected[0] == "BACK":
        return False, False    
    return actionsquirrel.AddItemToInventory, item  
    
def AddBlockDropItemFromInv(GAME, screen, verb):
    screen.clear()
    header = verb
    question = "Which item should be dropped from the player's inventory?"
    screen = useful.PrintHeader(header, screen, 0, 0)
    screen = useful.PrintText(question, screen, 4, 0)
    
    pickableItemsIndexes = GAME.GetPickableItems()
    itemMenu = []
    for item in pickableItemsIndexes:
        itemMenu.append(GAME.items[item].name)
    itemMenu.append("BACK")

    itemselected = useful.ShowMenu(itemMenu, screen, 6, 0)
    
    if itemselected[0] == "BACK":
        return False, False    
    return actionsquirrel.DropItem, item  

def AddBlockRemoveItemFromInv(GAME, screen, verb):
    screen.clear()
    header = verb
    question = "Which item should be removed from the player's inventory?"
    screen = useful.PrintHeader(header, screen, 0, 0)
    screen = useful.PrintText(question, screen, 4, 0)
    
    pickableItemsIndexes = GAME.GetPickableItems()
    itemMenu = []
    for item in pickableItemsIndexes:
        itemMenu.append(GAME.items[item].name)
    itemMenu.append("BACK")

    itemselected = useful.ShowMenu(itemMenu, screen, 6, 0)
    
    if itemselected[0] == "BACK":
        return False, False    
    return actionsquirrel.RemoveItemFromInventory, item  

def AddBlockAddItemToRoom(GAME, screen, verb):

    # Which item?
    screen.clear()
    header = verb
    question = "Which item should be added to a room?"
    screen = useful.PrintHeader(header, screen, 0, 0)
    screen = useful.PrintText(question, screen, 4, 0)
    
    itemMenu = [(i.name) for i in GAME.items]
    itemMenu.append("BACK")
    itemselected = useful.ShowMenu(itemMenu, screen, 6, 0)
    if itemselected[0] == "BACK":
        return False, False    
    
    # Add to which room?
    screen.clear()
    header = verb
    question = "To which room should " + itemselected[0] + " be added?"
    screen = useful.PrintHeader(header, screen, 0, 0)
    screen = useful.PrintText(question, screen, 4, 0)
    
    roomMenu = [(r.name) for r in GAME.rooms]
    roomMenu.append("BACK")
    roomselected = useful.ShowMenu(roomMenu, screen, 6, 0)
    if roomselected[0] == "BACK":
        return False, False    
    
    return actionsquirrel.AddItemToRoom, [itemselected[1], roomselected[1]]  

def AddBlockRemoveItemFromRoom(GAME, screen, verb):
    # Which item?
    screen.clear()
    header = verb
    question = "Which item should be removed from a room?"
    screen = useful.PrintHeader(header, screen, 0, 0)
    screen = useful.PrintText(question, screen, 4, 0)
    
    itemMenu = [(i.name) for i in GAME.items]
    itemMenu.append("BACK")
    itemselected = useful.ShowMenu(itemMenu, screen, 6, 0)
    if itemselected[0] == "BACK":
        return False, False    
    
    # Add to which room?
    screen.clear()
    header = verb
    question = "From which room should " + itemselected[0] + " be removed?"
    screen = useful.PrintHeader(header, screen, 0, 0)
    screen = useful.PrintText(question, screen, 4, 0)
    
    roomMenu = [(r.name) for r in GAME.rooms]
    roomMenu.append("BACK")
    roomselected = useful.ShowMenu(roomMenu, screen, 6, 0)
    if roomselected[0] == "BACK":
        return False, False    
    return actionsquirrel.RemoveItemFromRoom, [itemselected[1], roomselected[1]]  

# Wraps the curses changes to the terminal to prevent errors
curses.wrapper(main)



















