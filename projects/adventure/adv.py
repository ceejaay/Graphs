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

# world.printrooms()
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


    def breadth_first_search(self):
        pass



    def depth_first_traverse(self):
        # searching is true
        searching = True
        # set the current room
        cur_room = player.currentRoom
        # start searching
        for i in range(5):
        # while searching:
            # if the current room is not in visited
            if cur_room.id not in self.visited:
                # add the current room to visited
                self.add_room_to_visited(cur_room)
                print('visited', self.visited)
                # loop through the exits in the current room
            print('for loop begins')
            for k, v in self.visited[cur_room.id].items():
                print(k, v)
                # print('visited in the for loop', self.visited[cur_room.id].items())
                # if a room has a ? 
                if v == '?':
                    print('checking for ?')
                    # then travel to that room
                    prev_room = cur_room
                    player.travel(k)
                    # change the current room to the room just traveled to
                    cur_room = player.currentRoom
                    # print('new room', player.currentRoom.id)
                    print(f'traveled from {prev_room.id} to {player.currentRoom.id}')
                    # print('visited', self.visited)
                    searching = True
                else:
                    print(' after the else')

                    # if the room has no question marks. then we've reached a dead end????
                    searching = False
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











m = Mapping(roomGraph)
m.depth_first_traverse()



# print('current room id', player.currentRoom.id)
# print('current travel', player.travel('n'))
# print('current room id', player.currentRoom.id)
# print('current room exits', player.currentRoom.getExits())









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
