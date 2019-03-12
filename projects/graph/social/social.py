import random

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
        for i  in range(numUsers):
            self.addUser(f'Friend #{i+1}')

        # create friendships
        friendships = []
        friends_left = numUsers * avgFriendships
        total_friends = numUsers * avgFriendships

        for i in range(numUsers):
            if friends_left > 0:
                friends = round(random.random() * (avgFriendships * 2))
                print('friends', friends)
                friends_left -= friends
                friendships.append(friends)
            elif friends <= 0:
                friendships.append(0)

        while sum(friendships) < total_friends:
            print('adding more')
            for i in range(len(friendships)):
                if friends_left:
                    friendships[i] += 1
                    friends_left -= 1

        while sum(friendships) > total_friends:
            print('taking away')
            for k in range(len(friendships)):
                if friends_left:
                    friendships[k] -= 1
                    friends_left += 1

        for user in self.users:
            if len(friendships) > user-1:
                if friendships[user-1]:
                    for new_friend_index in range(len(friendships)):
                        if friendships[new_friend_index] == friendships[user-1]:
                            pass
                        elif friendships[new_friend_index] and friendships[user-1]:
                            self.addFriendship(user, new_friend_index+1)
                            friendships[new_friend_index] -= 1
                            friendships[user-1] -= 1




        # !!!! IMPLEMENT ME

        # Add users

        # Create friendships

    def getAllSocialPaths(self, userID):
        # use a queue
        que = [[userID]]
        # print('stack', stack)
        # if userID is 1
        # 5: 4, 3, 2, 1
        visited = {}

        while len(que) > 0:
            # vertex is an array
            vertex = que.pop()
            # print('vertex', vertex[-1])
            if str(vertex[-1]) not in visited:
                for item in self.friendships[vertex[-1]]:
                    # print(f'{item}: is friends with {vertex[-1]}')
                    # print('que', que)
                    # print('visited', visited)
                    # adding the path to the queue
                    que.insert(0, vertex + [item])

                visited[str(vertex[-1])] = que 

                # print('user', self.friendships[vertex[-1]])
                # print('not here')
            else:
                vertex = que.pop()
                # print('it here')




                    # path = path + [item]
                    # stack.append(path)
                # stack.insert.append(path)

                # I think the path gets added to the
                # visited[str(vertex)] = path





        # so if userID 1's connections are this: {3, 4, 5}
        # then the entry in the dict will look like this. {'3': [1]} <= this one looks like this because there is only one connection between 3 and 1

        # then add the connections to the stack. Along with the path.



            # how to check if in visited
        # Takes a user's userID as an argument

        # Returns a dictionary containing every user in that user's
        # extended network with the shortest friendship path between them.

        # The key is the friend's ID and the value is the path.

        
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(7, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
