                     #-----------------------------#
                     #-----Adventure Squirrel!-----#
                     #-----------------------------#

Final Project cs3101 - Programming Languages (Python)
Authors:
    Andrea Bonilla  - amb2335
    Bruno Goncalves - bag2136
    Wenjie Zhang    - wz2261

#---------------------------Introduction---------------------------------#

Game graphics are evolving at an alarming rate, we have already achieved
a level of photorealism that pushes computer hardware advanced further
and further. In the midst of all this, it is often forgotten how even
with simple strings of characters we can have an amazingly immersive
game experience. Our purpose is to chart our own path through the joy of
creating a text based adventure game engine that is both flexible and
simple with the help of Python as a high level language.

#------------------------------------------------------------------------#


#----------------------How to Run the Project----------------------------#
1. To create your own game:

	$ python3.4 squirrel.py

2. To play your own game:
	
	$ python3.4 runsquirrel.py <your_own_game_name>

2. To play the sample game provided by us:
	
	$ python3.4 runsquirrel.py columbia_game

#-------------------------------------------------------------------------#


#-----------------------------Caveats-------------------------------------#

1. When creating the game, please make sure that the item name has no white 
	spaces. i.e. "columbia_university" instead of "columbia university"
2. When creating the game, please make sure the terminal window size is
	large enough such as fullsize of the window.
3. Please do not remove items since it may cause a little problem. If you
	do want to remove an item, you can place it at -1 (no where) instead.

#-------------------------------------------------------------------------#


#--------------------Basic Structure of the Game Engine----------------------#

The game engine contains the following main components:
	
	1. Game Object: --> gamesquirrel.py
	The game object contains all the information about the game, including
	rooms, items, player, custom actions. By this way, we can simply save
	and load the game object as a pickle file for saving and loading.
		a. The room list in the game object contains all the room objects
			that have been created and stored in the game.
		b. The item list in the game object contains all the item objects
			that have been created and stored in the game.
		c. During the execution of the game, only the room index and item
			index would be passed as function parameters.

	2. Room Object: --> roomsquirrel.py
	The room object has its room name, room connections and room items. The
	room connections and room items are indecies of the room list and item
	list. For example:
		a. room 1's connection is a list [-1, -1, 5, -1, -1, ...] 
			Then room 5 is connected to room 1 at direction EAST.
		b. room 1's items is a list [0,1]
			Then room 1 has the first item and second item of the item list
			of the the game object.
		c. The room object supports functions such as "add item to the room"
			or "change the connection of the room".

	3. Item Object: --> itemsquirrel.py
	The item object has the following attributes:
		a. item name
		b. item description
		c. isPickable (boolean) and isDropable (boolean)
		d. location index to indicate the location of the item
			case -1: the item is placed at no where
			case -2: the item is in player's inventory
			case >=0: the item is in a specific room
		e. The item object supports functions such as "set to inventory"
			or "unplace itself".

	4. Custom Action Object --> actionsquirrel.py
	The custom action is defined to be an action that can execute one or 
	many default actions that have been defined in the game, such as "pick", 
	"drop", "go", "move", etc.

	The custom action object has the following attributes:
		a. verb: action name
		b. to which item the custom action can be applied
		c. in which room the custom action can be applied
		d. list of default actions that it would execute

	The actionsquirrel.py also contains many functions that are "default 
	actions" such as "pick", "drop", "move", "go", etc. Then the custom action 
	would call some of these function to implement the "customized action".

	5. Player Object --> playersquirrel.py
	The player has the following attributes:
		a. inventory: a list of item index to indicate what items the player has
		b. current room index to indicate the location of the player
		c. score
#----------------------------------------------------------------------------#


#---------------Basic Structure of Creat Game and Play Game------------------#

The game engine has two main functionality:
	1. Creat Game --> squirrel.py
	2. Play Game --> runsquirrel.py


Basic structure of the "create game" process:
	1. The game engine would walk through the processes of creation of rooms,
		items, actions according to the specific attributes of them.
		For example, a user could modify the connection of a specific room, and
		s/he could also add the items to this room. And then the user could
		define a customized action that exectute "add item 1 to inventory" and
		"change score" in this room.
	2. After all the element obejcts of the game have been created, the engine
		would save the entire game object as a pickle file so that the engine
		can obtain the information when it runs this file.

Basic structure of the "play game" process:
	a. The engine would load the game object, and then prompts for the user 
		to type in the command.
	b. The engine would execute the command based on the type of the action.
		For example:
		If the user types in "look", then the engine would print out the
		current room's description and what items the room has.
		And then if the user types in "move south", then the player's current
		room would be updated to the room index of the south room.
	c. The room objects, items objects, action objects and player objects would
		keep changing as the command keeps going.

#----------------------------------------------------------------------------#

All rights reserved. No part of the project, either text or source codes may be 
used for any purpose other than personal use. Therefore, reproduction, modification, 
storage in a retrieval system or retransmission, in any form or by any means, 
electronic, mechanical or otherwise, for reasons other than personal use, is 
strictly prohibited without prior permission from the authors (Andrea Bonilla, 
Bruno Goncalves, Wenjie Zhang).
