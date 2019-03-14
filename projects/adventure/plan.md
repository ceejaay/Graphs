### Depth First Traverse
  * This returns a room. It will be used as a starting point for the DFS
  * Steps.
      1. start in a new room
          What does the new room look like. How do we get it?
            * The first go around it is zero.
      2. check the room. See if it is in the visited list.
        * if isn't then add it.
            Add all rooms to visited with their exits
        * if it is then move on to the next step.
      3. Look at all the rooms.
        * is there one with a question mark?
            how do we get the question mark? Iterate through it?
            if yes. Then move to the next step.
            if No, then I think we've reached a dead end.
      4. Move to the room where you find value is a question mark.

      5. Repeat the above steps until a room with no question marks are found.

### Breadth First Search.
  * this takes in the return from the DFT.
  * It returns a path. That the player will walk to get to the nearest room with a question mark
