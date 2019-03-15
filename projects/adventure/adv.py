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
        path = [self.visited[start]]
        # print(f'bfs path: id: {start}: {path}')
        searching = True
        exit = None
        cur_room = player.currentRoom
        print('cur room', cur_room.id)
        # while searching:
        for i in range(3):
            if "?" in self.visited[cur_room.id].values():
                print('found a ?')
                searching = False
                # return something here
                # walk the path
                # keep track of the directions
            for k, v in self.visited[cur_room.id].items():
                # have to pick the exit we haven't gone before
                # have to add to the path
                new_path = list(path)
                exit = k
                print(f'cur room {cur_room.id} exit: { exit }')
            player.travel(exit)
            cur_room = player.currentRoom


        # while searching:





    def depth_first_traverse(self):
        # searching is true
        searching = True
        # set the current room
        cur_room = player.currentRoom
        exit = None
        prev_room = None
        # start searching
        while searching:
        # for i in range(3):
            # print('visited', self.visited)
            # print(f'cur room {cur_room.id}')
            if cur_room.id not in self.visited:
                self.add_room_to_visited(cur_room)

            prev_room = cur_room
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
                self.add_room_to_visited(cur_room)

            self.visited[prev_room.id][exit] = cur_room.id
            self.visited[cur_room.id][self.reverse_direction(exit)] = prev_room.id
            last_room = cur_room.id
            # print('last room', cur_room.id)
            # print('traversal', traversalPath)
            # print('visited', self.visited)
        return last_room


m = Mapping(roomGraph)
m.depth_first_traverse()
m.breadth_first_search(4)



            # # print(f'prev room: {prev_room} cur room: {cur_room}')
            # if cur_room.id not in self.visited:
            #     self.add_room_to_visited(cur_room)

            # if prev_room and cur_room:
            #     print(f'visited cur id: {cur_room.id}: {self.visited[cur_room.id]}', )
            #     print(f'visited prev id: {prev_room.id}: {self.visited[prev_room.id]}', )
            #     self.visited[prev_room.id][exit] = cur_room.id
            #     self.visited[prev_room.id][self.reverse_direction(exit)] = prev_room.id
            # else:
            #     print('no prev room')


            # for k, v in self.visited[cur_room.id].items():
            #     if v == '?':
            #         exit = k

            # prev_room = cur_room
            # player.travel(exit)
            # cur_room = player.currentRoom
         # top of loop.
        # check for current room in visited.
        # if not add it.
        # loop through exits.
        # get an unexplored one.
        # set current room to old room.
        # travel
        # set current room to the new room.


        #     if cur_room.id not in self.visited:
        #         print('visited before', self.visited)
        #         self.add_room_to_visited(cur_room)
        #     print('visited ', self.visited )
        #     exit = None
            # for k, v in self.visited[cur_room.id].items():
            #     if v == '?':
            #         exit = k
            #     else:
            #         searching = False

            # print(f'old room: {old_room.id} cur room: { cur_room.id }')
            # old_room = cur_room
            # # print('player loc before', player.currentRoom.id)
            # player.travel(exit)
            # cur_room = player.currentRoom


            # searching = False


        # # while searching:
        #     # if the current room is not in visited
        #     if cur_room.id not in self.visited:
        #         # add the current room to visited
        #         self.add_room_to_visited(cur_room)
        #         print('visited', self.visited)
        #         # loop through the exits in the current room
        #     print('for loop begins')
        #     for k, v in self.visited[cur_room.id].items():
        #         print(k, v)
        #         if v == '?':
        #             exit = v

        #     old_room = cur_room
        #     print('location before', player.currentRoom.id)
        #     player.travel(exit)
        #     print('location after', player.currentRoom.id)


                    # print('checking for ?')
                    # then travel to that room
                    # prev_room = cur_room
                    # player.travel(k)
                    # change the current room to the room just traveled to
                    # cur_room = player.currentRoom
                    # print('new room', player.currentRoom.id)
                    # print(f'traveled from {prev_room.id} to {player.currentRoom.id}')
                    # print('visited', self.visited)
                    # searching = True

                    # if the room has no question marks. then we've reached a dead end????
                    # searching = False
            # not sure what I'm doing here
            # searching = False




            
            # cur_room = player.currentRoom
            # if cur_room.id not in self.visited:
            #     doors = self.directions_convert(cur_room)
            #     self.visited[cur_room.id] =  doors


            # old_room = cur_room
            # for k, v in self.visited[cur_room.id].items():
            #     if v == '?':
            #         player.travel(k)
            #         print('old room in visited', self.visited[old_room.id])
            #         print('current room in visited', self.visited[player.currentRoom.id])
            #         print(f'traveled from {old_room.id} to {cur_room.id}')
            #         searching = False
            #     else:
            #         searching = False
            #         return player.currentRoom.id
             
            # cur_room = player.currentRoom
            # if cur_room.id not in self.visited:
            #     doors = self.directions_convert(cur_room)
            #     self.visited[cur_room.id] = doors
            #     old_room = cur_room
            #     for k, v in doors.items():
            #         if v == "?":
            #             player.travel(k)
            #             cur_room = player.currentRoom
            #             print('old_room', old_room.id)
            #             self.visited[old_room.id][k] = cur_room.id
            #             print('current room id', cur_room.id)

            #             # self.visited[cur_room.id][self.reverse_direction(k)] = old_room.id
            #             print('visited', self.visited)

            #     # self.update_room('n')
            #     searching = False


        # # add current room to stack which is room id == 0
        # stack = [player.currentRoom]
        # # go through the loop
        # while len(stack) > 0:
        #     # pop the item off the stack
        #     # for i in stack:
        #     #     print('rooms in stack', i.id)
        #     # print('stack', stack)
        #     room = stack.pop(0)
        #     # check to see if player is in current room
        #     if player.currentRoom.id != room.id:
        #         current_room_doors = self.directions_convert(player.currentRoom) 
        #         # loop through the curruent room directions to find the room to go to
        #         for k, v in current_room_doors.items():
        #             print(k, v)
        #             if self.peek_in_room(k).id == room.id:
        #                 # add the direction to the traversal path
        #                 # print('room id', room.id)
        #                 # print('visited', self.visited[player.currentRoom.id])
        #                 traversalPath.append(k)
        #                 # travel to new room
        #                 print('before move', player.currentRoom.id)
        #                 player.travel(k)
        #                 print('after move', player.currentRoom.id)

        #     # if player.currentRoom.id == room.id:
        #         print('this is running')
        #     if room.id not in self.visited:
        #         # get the doors from the room
        #         # convert them to a key value dictionary
        #         doors = self.directions_convert(room)
        #         # add the id and it's doors to the visited list
        #         self.visited[room.id] = doors
        #         # add the doors to the stack
        #         for k, v in doors.items():
        #             # insert them at the beginning of teh stack
        #             stack.insert(0, self.peek_in_room(k))
        #                 # print('rooms added', self.peek_in_room(k).id)
        #     # if user is not in the room that was popped off the stack, then travel to the room
        #         # the doors where you are right now.
        #     print(room.getExits())
        #     print('stack', stack)


# if room has a question mark. The go that way.


# to_check = checking.pop()
# go to one. check one come back to 0
# # to check curren check
# checked already visited






        # print(f'current room id: {player.currentRoom.id}, stack room id: {room.id}')
                # player.travel(stack[0])
                # player.travel(stack[0])
        # print('stack after', stack)

# add a room to the stack.
# check if it's been visited
# if not, add it to visited.
# check for ?marks.
# if there are some add those directions to the stack.
#     When going to a new room.
#     may have to empty the stack and start over in a new room.
#     Treat each room like it has it's own stack?


# Check for ? in any of the directions.
# add the first one to the stack.

# start with the first room
# check the first room. 
# if it's in visited.
#     Then do something else.

# if its not. 
#     Then add it to visited.
#     add it with it's exits and question marks
#     then loop through the exits.
#     peek in the rooms and add those to the stack.
#     Check the next room in the stack.
#     if it's in visited. Then go to the next in the stack.
#         if the room on the stack is not visited. 
#             travel to the room and repeat.























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
