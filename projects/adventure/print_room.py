
# from room import Room
# from player import Player
# from world import World
# from rooms_graph import roomGraph
# from print_room import printRooms
# from queue import Queue

def printRooms(self):
       rotatedRoomGrid = []
       for i in range(0, len(self.roomGrid)):
           rotatedRoomGrid.append([None] * len(self.roomGrid))
       for i in range(len(self.roomGrid)):
           for j in range(len(self.roomGrid[0])):
               rotatedRoomGrid[len(self.roomGrid[0]) -
                               j - 1][i] = self.roomGrid[i][j]
       roomGrid = rotatedRoomGrid
       map_str = ""
       for row in roomGrid:
           map_str += "#"
           for room in row:
               if room is not None and room.n_to is not None:
                   map_str += "  |  "
               else:
                   map_str += "     "
           map_str += "#\n"
           # Print room row
           map_str += "#"
           for room in row:
               if room is not None and room.w_to is not None:
                   map_str += "-"
               else:
                   map_str += " "
               if room is not None:
                   map_str += f"{room.id}".zfill(3)
               else:
                   map_str += "   "
               if room is not None and room.e_to is not None:
                   map_str += "-"
               else:
                   map_str += " "
           map_str += "#\n"
           map_str += "#"
           for room in row:
               if room is not None and room.s_to is not None:
                   map_str += "  |  "
               else:
                   map_str += "     "
           map_str += "#\n"
       print(map_str)

