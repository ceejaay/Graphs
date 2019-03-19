from room import Room
from player import Player
from world import World
from rooms_graph import roomGraph

import random

# Load world
world = World()
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

    def direction_swap(self, direction):
        cardinal_directions = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
        return cardinal_directions[direction]

    def df_traverse(self):
        searching = True
        prev_room = False
        exit = None
        cur_room = self.player.currentRoom
        while searching:
            if cur_room.id not in self.visited:
                self.add_room()
            if prev_room:
                self.visited[cur_room.id][self.direction_swap(exit)] = prev_room.id
                self.visited[prev_room.id][exit] = cur_room.id
            if '?' in self.visited[cur_room.id].values():
                for key, value in self.visited[cur_room.id].items():
                    if value == '?':
                        exit = key
            else:
                searching = False
                return cur_room.id
            prev_room = cur_room
            traversalPath.append(exit)
            self.player.travel(exit)
            cur_room = self.player.currentRoom

    def bf_search(self, room):
        # room is the current room number
        q = [[room]]
        searching = True
        while searching:
            path = q.pop(0)
            print('path', path)
            new_room = path[-1]
            print('new room', new_room)
            if '?' in self.visited[new_room]:
                print('path', path)
                return path

            print('cur room data', self.visited[new_room])
            for k, v in self.visited[new_room].items():
                print('value', v)
                q.append(v)








m = Mapping(player)
# print('df output', m.df_traverse())
dft = m.df_traverse()

m.bf_search(dft)
# print('visited after df traverse', m.visited)

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
