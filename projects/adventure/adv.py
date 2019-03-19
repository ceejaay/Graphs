from room import Room
from player import Player
from world import World
from rooms_graph import roomGraph

import random

# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.


world.loadGraph(roomGraph)
player = Player("Name", world.startingRoom)




# FILL THIS IN
traversalPath = []




# world.printRooms()

class Mapping():
    def __init__(self, p):
        self.visited = {}
        self.player = p

    def add_room(self):
        room = self.player.currentRoom.getExits()
        new_room = {}
        for item in room:
            new_room[item] = '?'
        self.visited[self.player.currentRoom.id] = new_room


    def df_traverse(self):
        searching = True
        prev_room = False
        for i in range(0, 5):
        # while searching:
            cur_room = self.player.currentRoom.id
            exit = None
            if cur_room not in self.visited:
                self.add_room()
                # print('visited', self.visited)

            for k, v in self.visited[cur_room].items():
                if v == '?':
                    exit = k
                else:
                    searching = False
                    return cur_room

            prev_room = cur_room
            self.player.travel(exit)
            cur_room = self.player.currentRoom.id
            if cur_room in self.visited:
                print('in there')
                print('the door we went through', self.visited[prev_room])
            else:
                self.add_room()

            print('room after', self.player.currentRoom.id)
            # print('visited', self.visited)
            # print('exit', exit)



        # while we don't have a dead end keep searching
        # when get to a room. Check if in visited
        # if it's not, add it to visited









m = Mapping(player)
m.df_traverse()




# TRAVERSAL TEST
visited_rooms = set()
player.currentRoom = world.startingRoom
visited_rooms.add(player.currentRoom)
for move in traversalPath:
    player.travel(move)
    visited_rooms.add(player.currentRoom)

if len(visited_rooms) == len(roomGraph):
    print(f"TESTS PASSED: {len(traversalPath)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(roomGraph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.currentRoom.printRoomDescription(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     else:
#         print("I did not understand that command.")
