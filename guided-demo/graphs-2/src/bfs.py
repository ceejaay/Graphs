# field verticies tha maps vertex labels to edges
# add vertex method
# add edge method

class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

class Graph:
    def __init__(self):
        # self.vertices = {
        #             "1": {"2", "3"},
        #             "2": {"4", "5", "1"},
        #             "3": {"6", "7", "1"},
        #             "4": {"2", "8", "9"},
        #             "5": {"2", "10", "11"},
        #             "6": {"3","12","13"},
        #             "7": {"3", "14", "15"},
        #             "8": {"4"},
        #             "9": {"4"},
        #             "10": {"5"},
        #             "11": {"5"},
        #             "12": {"6"},
        #             "13": {"6"},
        #             "14": {"7"},
        #             "15": {"8"}
        #             }
        self.vertices = {
            "1": {"5", "2"},
            "2": {"5", "1", "3"},
            "3": {"4", "2"},
            "4": {"3", "6", "5"},
            "5": {"4", "1", "2"},
            "6": {"4"}
            }

    def add_vertex(self, key):
        self.vertices[key] = set()

    def add_edge(self, key, value):
        if not self.vertices[key] and not self.vertices[value]:
            print('error: no vertext')
        else:
            self.vertices[key].add(value)
            self.vertices[value].add(key)

    def add_directed_edge(self, key, value):
        if not self.vertices[key] and not self.vertices[value]:
            print('error: no vertext')
        else:
            self.vertices[key].add(value)

    def bf_traverse(self, start):
        queue = [start]
        visited = set()
        while len(queue) > 0:
            for v in self.vertices[queue[0]]:
                if v not in queue and v not in visited:
                    queue.append(v)
            print('q: ', queue)
            print(f'VISITED: {queue[0]}')
        visited.add(queue.pop(0))

    def breadth_first_path(self, start, end):
        queue = [start]
        visited = set()
        path = []
        while len(queue) > 0:
            for v in self.vertices[queue[0]]:
                if v not in queue and v not in visited:
                    queue.append(v)
            print('q: ', queue)
            print(f'VISITED: {queue[0]}')
            print('path: ', path)
            visited.add(queue.pop(0))

    def df_traverse(self, start):
        # start a stack
        stack = [start]
        # set up visited list
        visited = set()
        # while stack has items in it go through the loop
        while len(stack) > 0:
            # temp = stack.pop(0)
            if stack[0] not in visited:
                visited.add(stack[0])
                for v in self.vertices[stack[0]]:
                    stack.insert(0, v)
                    print('stack', stack)
            else:
                stack.pop(0)
        print(visited)

    def depth_first_path(self, start, end):
        stack = [[0]]
        path = set()
        while len(stack) > 0:
            if stack[0] not in path:
                # we copy the path.
                path.add(stack[0])
                for v in self.vertices[stack[-1]]:
                    path_copy = stack[0]
                    path_copy.append[v]
                    stack.insert(0, path_copy)

                # path_copy = path[0]
                # path_copy.append(stack[0])
                # path.insert(0, path_copy)
                print('path', path)
                # Then append the latest vertex

                temp_array = path[0]
                temp_array.append(stack[0])

                path.add(stack[0])
                # for v in self.vertices[stack[0]]:

            else:
                stack.pop(0)



                    # print('after putting edge in stack: ', stack)





            # look at first item.
            # add all it's children to the top of the stack.
            # look at that top item.
            # add all it's children to the top of the stack.
            # Look at the first item.
            # How do we know we've reached the end of the stack.



# q.insert(0, q[0].right)



g = Graph()
# g.bf_traverse('1')
# g.df_traverse('1')
g.breadth_first_path('1', '9')
# g.depth_first_path('1', '6')
