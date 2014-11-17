class Game_Map(object):

    """
    Here we have our game map, which contains a game and
    the various connections in that game
    """

    #if -1, then that means you cannot go to room
    #if >0, then that means you connect to that given room

    def __init__(self, rooms):
        
        self.map = {}
        self.rooms = rooms

        for i in rooms:
            connect = i.connections # the connection list of that particular room
            self.map[i.name] = connection

    def add_connections(room_name, conect_to_room_name):
        
        i = 0 #index of the room_name
        j = 0 #index of the connect_to_room_name
        for a in range(len(self.rooms)):
            if self.rooms[a].name == room_name:
                i = a
            elif self.rooms[a].name == connect_to_room_name:
                j = a

        for c in self.map.keys():
            if c == room_name:
                connect = c.connections
                connect[j] = 1 # create the connection


    def get_map(self):
        return self.map

    def get_rooms(self):
        return self.rooms
