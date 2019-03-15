### Depth First Traverse
  * This returns a room. It will be used as a starting point for the DFS
  * Steps.
      1. start in a new room
          What does the new room look like. How do we get it?
            * can call player functions to know what exits there are.
            * ???? 
            * The first go around it is zero.
      2. check the room. See if it is in the visited list.
        * if isn't then add it.
            Add all rooms to visited with their exits
            get the exits with the player.currentRoom method.
        * if it is then move on to the next step.
      3. Look at all the rooms.
        * is there one with a question mark?
            how do we get the question mark? Iterate through it?
            if yes. Then move to the next step.
            if No, then I think we've reached a dead end.
      4. Move to the room where you find value is a question mark.
      5. Then update the previous room's data and the new rooms data in their dictionaries.
        * To the old room. Add the number of the new room to the direction in the dictionary. ie: 01: { n: 002}
        * To the new room. Add the number of the old room to the opposite direction of the new room's dictionary. ie 002: {s: 01}

      6. Repeat the above steps until a room with no question marks are found.

### Breadth First Search.
  * this takes in the return from the DFT.
  * It returns a path. That the player will walk to get to the nearest room with a question mark


How to update '?' in the room Dict.
  At the top of the loop.
  if a prev and cur room exist.
  Then we have the things to swap info
  Move to new room.
  keep track of the old room exit
  keep track of the reversed exit in the new room.
  When at the top of loop. Use that data to update the key/value in both the rooms .


