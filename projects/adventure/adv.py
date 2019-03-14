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

world.printRooms()
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

    def reverse_direction(self, direction):
        compass_dir = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e', }
        return compass_dir[direction]

    
    def peek_in_room(self, direction):
        player.travel(direction)
        next_room = player.currentRoom
        player.travel(self.reverse_dir[direction])
        return next_room



    def depth_first_traverse(self):
        # add current room to stack
        stack = [player.currentRoom]
        # go through the loop
        while len(stack) > 0:
            # pop the item off the stack
            room = stack.pop(0)
            print('stack before', stack)
            print('room id', room.id)
            # if the id isn't in visited do the things
            if room.id not in self.visited:
                # get the doors from the room
                # convert them to cardinal directions
                doors = self.directions_convert(room)
                # add the id and it's doors to the visited list
                self.visited[room.id] = doors
                print('visited', self.visited)
                # add the doors to the stack
                for k, v in doors.items():
                    # insert them at the beginning of teh stack
                    stack.insert(0, self.peek_in_room(k))
                    # for i in stack:
                    #     print(i.id)
            else:
                stack.pop(0)
                # pop the top of the stack.
                # player.travel(stack[0])
                # player.travel(stack[0])
            print('stack after', stack)

add a room to the stack.
check if it's been visited
if not, add it to visited.
check for ?marks.
if there are some add those directions to the stack.
    When going to a new room.
    may have to empty the stack and start over in a new room.
    Treat each room like it has 


Check for ? in any of the directions.
add the first one to the stack.








    def breadth_first_search(self):
        pass


m = Mapping(roomGraph)
m.depth_first_traverse()



# print('current room id', player.currentRoom.id)
# print('current travel', player.travel('n'))
# print('current room id', player.currentRoom.id)
# print('current room exits', player.currentRoom.getExits())

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
