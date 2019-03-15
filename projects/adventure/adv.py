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


    # def peek_in_room(self, direction):
    #     player.travel(direction)
    #     next_room = player.currentRoom
    #     player.travel(self.reverse_direction(direction))
    #     return next_room

    def update_room(self, direction):
        this_room = player.currentRoom
        if this_room.id in self.visited:
            print('need to update room')
        else:
            print('this room is not in the database')


    def breadth_first_search(self, start):
        # print('visited 0', '?' in self.visited[0].values())
        # path only has the id of the room from the dft
        # path = [start]
        searching = True
        cur_room = player.currentRoom
        cur_room_exits = cur_room.getExits()
        prev_room = None
        for i in range(5):
        # while searching:
            # print('bfs running')
            # print('cur room', cur_room.id)
            # print('bfs result', cur_room.id)
            print(self.visited[cur_room.id])
            print("?" in self.visited[0].keys())
            if '?' in self.visited[cur_room.id].values():
                # go through the existing direction.
               # find the next place to go
                searching = False
                return False
            else:
                if len(cur_room_exits) <= 1:
                    print('room before', player.currentRoom.id)
                    player.travel(cur_room_exits[0])
                    print('room after', player.currentRoom.id)
                    prev_room = cur_room
                    cur_room_exits = cur_room.getExits()

                # for item in cur_room_exits:
                #     print('direction: ', item)
                    
                    # if prev_room.id != self.visited[cur_room.id][item]:
                    #     prev_room = cur_room
                    #     player.travel[item]
                    #     traversalPath.append(item)
                    #     cur_room = player.currentRoom
                    #     cur_room_exits = cur_room.getExits()
            # else:
            #     player.travel(cur_room_exits[0])
            #     traversalPath.append(cur_room_exits[0])
            #     cur_room = player.currentRoom
            #     cur_room_exits = cur_room.getExits()


            #     print('looking for ?')
            #     # print('checking for visitd room')
            #     searching = False
            #     # print(f'searching: {searching} cur room: {cur_room.id}')
            # else:
            #     return False

            # if prev_room:
            #     # print('there is a prev room')
            #     for item in cur_room_exits:
            #         if prev_room.id != self.visited[cur_room.id][item]:
            #             prev_room = cur_room
            #             player.travel[item]
            #             traversalPath.append(item)
            #             cur_room = player.currentRoom
            #             cur_room_exits = cur_room.getExits()
            # else:
            #     player.travel(cur_room_exits[0])
            #     traversalPath.append(cur_room_exits[0])
            #     cur_room = player.currentRoom
            #     cur_room_exits = cur_room.getExits()
        return True

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
m.breadth_first_search(df)
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
