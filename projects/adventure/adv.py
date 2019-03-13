from room import Room
from player import Player
from world import World
from rooms_graph import roomGraph
from print_room import printRooms
from queue import Queue

import random

# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.


# 
# 


world.loadGraph(roomGraph)
player = Player("Name", world.startingRoom)

# world.printRooms()
# FILL THIS IN
# printRooms(roomGraph)
# first_item = roomGraph[1][1]
# print('first[] item', first_item)


# for k, v in thing.items():
#     print(k, v)

class Mapping:
    def __init__(self, graph):
        self.graph = graph
        self.visited = {}
        self.start = player.currentRoom.id

    def directions_convert(self, current_room):
        room_data = {}
        for item in current_room.getExits():
            room_data[item] = "?"

        return room_data

    def depth_first_traverse(self):
        stack = [self.start]
        while len(stack) > 0:
            if stack[0] not in self.visited:
                self.visited[stack[0]] = self.directions_convert(player.currentRoom)
                print('visited', self.visited)
        








    def breadth_first_search(self):
        pass


m = Mapping(roomGraph)
m.depth_first_traverse()



print('current room id', player.currentRoom.id)
print('current travel', player.travel('n'))
print('current room id', player.currentRoom.id)
print('current room exits', player.currentRoom.getExits())

traversalPath = ['n', 'e']








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
