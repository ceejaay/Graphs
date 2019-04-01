import random

people = 10

face_graph = {}

for i in range(0, people):
    face_graph[i] = set()


for item in face_graph:
    rando_friend = random.randint(0, 10)





for item in face_graph:
   face_graph[item].add(1)
   total = 0 
   total += len(face_graph[item])
   print(total)


# print('face_graph', face_graph)
# print('average', avg)

# loop through each set.
# check the averate number of friends
# add a friend connection to a random friend.
# do that until the average is reached

# plan:
#     while average is less than the given aveerage.
#         add a friend connecion at random.
#         when adding the friend connection...
#         make sure a friend is not becomign friends with herself.


#         check the average
