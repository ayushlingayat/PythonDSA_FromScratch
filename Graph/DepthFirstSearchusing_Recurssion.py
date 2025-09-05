class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
n = 6
edges = [(0, 1), (0, 3), (0, 4), (1, 2), (1, 5), (2, 4), (3, 4)]

# Adjacency list
adjList = [[] for _ in range(n)]
for x, y in edges:
    adjList[x].append(y)
    adjList[y].append(x)

# for i in range(n):
#     print(i, "->", adjList[i])

visited = [False] * n
ans = []


def dfs(i,adjList,visited):
    visited[i] = True
    ans.append(i)
    for x in adjList[i]:
        if not visited[x]:
            dfs(x,adjList, visited)


dfs(0,adjList,visited)
print("dfs using the recurssion ->",ans )