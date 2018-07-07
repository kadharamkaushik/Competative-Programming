def canvisitroom(rooms):
    visited = [0] * (len(rooms))
    dfs(rooms, 0, visited)
    return sum(visited) == len(rooms)

def dfs(rooms, index, visited):
    visited[index] = 1
    # print(visited)

    for key in rooms[index]:
        # print (key)
        if not visited[key]:
            dfs(rooms, key, visited)

print (canvisitroom([[1], [0,2], [2]]))
print (canvisitroom([[1,3], [3,0,1], [2], [0]]))
print (canvisitroom([[1,2,3], [0], [0], [0]]))
print (canvisitroom([[1], [0,2,4], [1,3,4], [2], [1,2]]))
print (canvisitroom([[1], [2,3], [1,2], [4], [1], [5]]))
print (canvisitroom([[1], [2], [3], [4], [2]]))
print (canvisitroom([[1], [1,3], [2], [2,4,6], [], [1,2,3], [1]]))

