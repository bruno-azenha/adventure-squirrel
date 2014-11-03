# This is the engine that actually runs the game
import Pickle
import player
import actions
import game_map
import room # Andrea's source file about room capability
import item # Bruno's source file about item capability

def run_game(GAME):

	while GAME.isRunning():

		directions = ["north", "south", "east", "west",
                  "northeast", "northwest", "southeast",
                  "southwest", "up", "down", "in", "out"]

		# initial room
		current_room = GAME.rooms[0]

		player = GAME.PLAYER

		actions = GAME.ACTIONS

		command = input("\nwhat are you going to do\n").lower()

		# Quits the game
        if command.startswith("quit") or command.startswith("die") :
            GAME.stopRunning = False
            break

        elif command.startswith("search") or command.startswith("look"):
        	print(current_room.items)

        elif command.startswith("pick up"):
        	item = command.split()[2]
        	if item == None:
        		print("What do you want to pick up?")

        	elif item not in current_room.items:
        		print("{0} is not in this room.".format(item))
        	else:
        		player.pick_up(item)
        		print("{0} is now in your pocket.".format(item))

        elif command.startswith("go") or command.startswith("go to"):
        	
        	direction = command.split()[2]

        	if direction == None:
        		print("Which way do you want to go? North? East?")

        	else:
        		direct_index = directions.indexof(direction)
        		if current_room.connections[direct_index] > 0:
        			current_room = ???
        			print("Your are now in {0}".format(current_room.name))
        		else:
        			print("There's no room in that direction")

        elif command.startswith("pocket") or command.startswith("inventory"):
        	print(player.inventory)

        elif "score" in command:
        	print("Your score now is {0}".format(player.score))


def make_rooms():
	number_of_rooms = input("How many rooms do you want to create?");
	while(not isinstance(number_of_rooms, int)):
		try:
			number_of_rooms = int(number_of_rooms)
		except ValueError:
			print("Please enter a valid integer number")

	rooms_list = []
	
	for i in range(number_of_rooms):
        fix = True
        while fix==True:
            room_name = input("What is an area's name?")
            room_description = input("""Please write the text you want
                                         your player to see when
                                         he/she enters""")
            print(room_name)
            print(room_description)
            correction = input("Is this correct?")
            if handle_human_input(correction) is True:
                fix = False
            	rooms_list.append(Room(room_name, room_description,i))

	return rooms_list

#obviously need to handle for 'y' or 'yes' etc
def handle_human_input(human_input):
    if human_input=='y':
        return True
    else:
        return False

def mode3():
	# This mode require a "game.pickle" file
	with open('game.pickle', 'r') as f:
		GAME = pickle.load(f)

	#run the game
	run_game(GAME)
	print("Thanks for playing! Goodbye!")

	return 0

def mode2():
	
	PLAYER = Player(input("What is your player's name?"))
	ROOMS = make_rooms() # instantiate the room object
	ACTIONS = Actions() # all the verbs available in the entire game
	GAME_MAP = Game_Map(ROOMS)

	#create game object
	GAME = Game(GAME_MAP, ROOMS, PLAYER, ACTIONS)

	# create the pickle file for game object
	with open('game.pickle', 'w') as f:
		pickle.dump(GAME, f)

	#run the game
	run_game(GAME)
	print("Thanks for playing! Goodbye!")

	return 0

def mode1():
	print(
		"""
		BACKGROUND:
		a. You will traverse all the rooms that has been designed.
		b. Your job is to accumulate the scores as much as possible
		   by using remarkable move or picking up items

		MAIN CONTROLS:  
		a. To move around you simply enter which way you want to go.
		   For example, if you want to go east side of the room, type in \"go east"\"
		b. There are many other actions that you can use.
		   For example, if you want to look around, type in \"look\".  
		c. You are carrying stuff. To see what you are holding you can input \"check inventory\". 
		d. You can also drop stuff by inputting \"drop\" or check if you can pick anything
		    up from your environment by inputting \"search\".
		e. If you want to know how many scores you have, type in \"scores\" 
		f. To quit the game, simply type in \"quit\"
		"""
		)

def intro():
	print("\nWelcome to the game.")
	print("Please choose the mode you want (\"1\" or \"2\" or \"3\"): ")
	print("1. How to play")
	print("2. Start creating the game")
	print("3. Start the game with the Pickle File generated previously")
	
	i = None
	while(i == None):
		i = input()
		if i == "1":
			return 1
		elif i == "2":
			return 2
		elif i == "3":
			return 3
		else:
			print("Please enter a valid integer from 1 to 3 only")
			i = None
	return i

def main():
	mode = intro()
	if mode == 1:
		mode1()
	elif mode == 2:
		mode2()
	elif mode == 3:
		mode3()



if __name__ == "__main__":
	main()
