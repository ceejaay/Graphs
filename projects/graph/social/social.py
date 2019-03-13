import random

class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        for i in range(numUsers):
            self.addUser(f"User {i+1}")

        # Create friendships
        possibleFriendships = []
        for userID in self.users:
            for friendID in range(userID + 1, self.lastID + 1):
                possibleFriendships.append( (userID, friendID) )
        print(possibleFriendships)
        random.shuffle(possibleFriendships)
        print(possibleFriendships)

        for friendship in possibleFriendships[: (numUsers * avgFriendships) // 2 ]:
            print(f"CREATING FRIENDSHIP: {friendship}")
            self.addFriendship(friendship[0], friendship[1]) 






        # !!!! IMPLEMENT ME

        # Add users

        # Create friendships

    def getAllSocialPaths(self, userID):
        # create a queue
        q = Queue()
        # the starting list
        initial_list = [userID]
        # the visited dict
        visited = {}
        # put the first list in the queue
        q.enqueue(initial_list)
        # go through the loop
        while q.size() > 0:
            print('queue', q.queue)
            # pop out the path
            path = q.dequeue()
            # designate the new id
            newID = path[-1]
            # check if the new id is in visited
            if newID not in visited:
                # if it's not then add it with the current path
                # [1, 5]
                # newID = 1
                # path = [1]
                # [1, 5]
                visited[newID] = path
                # go through the id's friend connections
                for friendID in self.friendships[newID]:
                    # set the new path to a new list including the old path
                    new_path = list(path)
                    # add the id that is in the list of connections to the current friend
                    new_path.append(friendID)
                    # add the new path to the queue
                    q.enqueue(new_path)
        # return the visited dict
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(7, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
