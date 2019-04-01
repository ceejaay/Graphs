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
room_path = []
world.printRooms()

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

    def take_the_path(self, a):
        if a == False:
            print('you should be done')
        else:
            for i in range(0, len(a) - 1):
                current_room = a[i]
                next_room = a[i + 1]
                for key, value in self.visited[current_room].items():
                    if value == next_room:
                        traversalPath.append(key)
                        # room_path.append(value)
                        self.player.travel(key)
            # print('cur room', current_room, 'next room ', next_room)
            # print(f'visited item {a[i]} exits: {self.visited[a[i]]}', )

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
            # room_path.append(self.visited[cur_room][exit])
            self.player.travel(exit)
            cur_room = self.player.currentRoom

    def bf_search(self, room):
        # room is the current room number
        q = [[room]]
        searching = True
        # while len(q) > 0:
        while searching:
            # print('queue', q)
        # for i in range(99):
            path = q.pop(0)
            # print('bf searching 75')
            # print('path', path)
            new_room = path[-1]
            # print('new room True or False and length of visited', new_room == '?' and len(self.visited) >= len(roomGraph))
            # print('new room', new_room)
            # print('outside if statement', path)
            if new_room == '?':
                # print('bf searching 79')
                # print('no ? and in visited')
                # print('inside if statement', path)
                searching = False
                path.pop()
                return path
            elif new_room != '?' and len(self.visited) >= len(roomGraph):
                searching = False
                return False
            for k, v in self.visited[new_room].items():
                if v not in path:
                    # print('looking for ?', v)
                    new_path = list(path)
                    new_path.append(v)
                    q.append(new_path)
        # return False

m = Mapping(player)
# print('df output', m.df_traverse())
# print('visited len', len(m.visited), 'graph len', len(roomGraph))
while len(m.visited) < len(roomGraph):
# for i in range(10):
    dft = m.df_traverse()
    # print('depth first traversal', dft)
    bf = m.bf_search(dft)
    # print(bf)
    # print('breadth first array', bf)
    m.take_the_path(bf)
    # print('traversal', traversalPath)
    # print('visited len', len(m.visited), 'graph len', len(roomGraph))

# print('visited after df traverse', m.visited)
# m.translate(None)

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
