
class Game(object):

    # all the parameters input must be initialied before we create a game class
    def __init__(self, game_map, rooms, player, all_actions):
        self.game_map = game_map
        self.rooms = rooms
        self.player = player
        # we should provide all the available actions in the initialization of the game
        # such as "look","search","touch",etc.
        all_actions = all_actions
        running = True

    def isRunning():
        return running

    def stopRunning():
        running = False

    # for testing
    def __str__(self):
        return "Game Class"

    # for testing
    def __repr__(self):
        return "Game Class"

def main():
    test = Game("game_map1","rooms1","player1", "all_actions1")
    print(test)

if __name__ == "__main__":
    main()