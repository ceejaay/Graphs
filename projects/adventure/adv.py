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
traversalPath = []

class Mapping:
    def __init__(self, graph):
        self.graph = graph
        self.visited = {}
        self.start = player.currentRoom.id

    # def directions_convert(self, current_room):
    #     room_data = {}
    #     for item in current_room.getExits():
    #         room_data[item] = "?"
    #     return room_data
    # {"n": "?"}

    def reverse_direction(self, direction):
        compass_dir = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e', }
        return compass_dir[direction]

    def add_room_to_visited(self, room):
        room_data = {}
        for item in room.getExits():
            room_data[item] = "?"

        self.visited[room.id] = room_data

    def update_room(self, direction):
        this_room = player.currentRoom
        if this_room.id in self.visited:
            print('need to update room')
        else:
            print('this room is not in the database')

    def travel(self, path):
        destination = path[-1]
        current_room = player.currentRoom.id
        for i in range(len(path) - 1, 0, -1):
            print(path[i])
            # for k, v in self.visited[path[i]].items():
            #     # if v == path[i]:
            #     print(f'v: {v}, path number {path[i]}')









    def breadth_first_search(self, start):
        # exit = player.currentRoom.getExits()[0]
        # next_room = self.visited[start][exit]
        cur_room = start
        # print(next_room)
        q = []
        q.append(start)
        path = [start]
        searching = True
        while searching:
        # for i in range(5):
            # print('path', path)
            checking = q.pop(0)
            # print(f'checking {checking} path { path } cur room {player.currentRoom.id}, visited: {self.visited}')
            if '?' in self.visited[checking].values():
                # print(f' FOUND ONE => checking {checking} - path { path } - cur room: {player.currentRoom.id} - visited: {self.visited}')
                # print(' found one')
                # print('checking value', checking)
                searching = False
            else:
                for k, v in self.visited[checking].items():
                    # print(k, v)
                    # print(f' LOOP => checking {checking} \n - path { path } \n - q: {q} \n - cur room: {player.currentRoom.id} \n - cur room exits {self.visited[checking]}\n - visited: {self.visited}')
                    # print('adding to path', k)
                    if v != cur_room:
                        q.append(v)
                        new_path = list(path)
                        path.append(v)
                # print('you should move on')
                # print('q', q)
            # for thing in path:
            #     player.travel(thing)
            #     traversalPath.append(thing)
                # print('player location:', player.currentRoom.id)

        # while len(q) > 0:

        return path


    def depth_first_traverse(self):
        # searching is true
        searching = True
        # set the current room
        cur_room = player.currentRoom
        exit = None
        prev_room = None
        # start searching
        while searching:
            # print('dft running')
            # print('dft room visit', cur_room.id)
        # for i in range(3):
            # print('visited', self.visited)
            # print(f'cur room {cur_room.id}')
            if cur_room.id not in self.visited:
                self.add_room_to_visited(cur_room)

            prev_room = cur_room
            # print('cur room', cur_room.id)
            # print('cur room exits', self.visited[cur_room.id])

            for k, v in self.visited[cur_room.id].items():
                if v == '?':
                    exit = k
                else:
                    searching = False
                    # print(f'out of values')
            player.travel(exit)
            traversalPath.append(exit)
            cur_room = player.currentRoom
            if cur_room.id not in self.visited:
                # print(f'cur room: {cur_room.id}  exit: {exit}')
                self.add_room_to_visited(cur_room)

            self.visited[prev_room.id][exit] = cur_room.id
            self.visited[cur_room.id][self.reverse_direction(exit)] = prev_room.id
            last_room = cur_room.id
            # print('last room', cur_room.id)
            # print('traversal', traversalPath)
            # print('visited', self.visited)
        return last_room


m = Mapping(roomGraph)
# print('graph length', len(roomGraph) )
# print('visited', len(m.visited) )
df = m.depth_first_traverse()
p = m.breadth_first_search(4)
# print(m.breadth_first_search(4))
m.travel(p)

# print('room graph length', len(roomGraph))
# while len(m.visited) < len(roomGraph):
# # for i in range(13):
#     df = m.depth_first_traverse()
#     # print('dead end room', df)
#     # print('path length', len(traversalPath))
#     m.breadth_first_search(df)
    # print(m.breadth_first_search(df))


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
#         print('cur room', m.directions_convert(player.currentRoom))
#     else:
#         print("I did not understand that command.")
