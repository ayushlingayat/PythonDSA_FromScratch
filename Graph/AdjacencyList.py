n = 6  # number of nodes
e = 7  # number of edges

edges = [(0, 1), (0, 3), (0, 4), (1, 2), (1, 5), (2, 4), (3, 4)]  # edges

# print(n, e, egdes)

adjList = []
for i in range(n):
    adjList.append([])

print(adjList)

for edge in edges:
    x = edge[0]
    y = edge[1]

    adjList[x].append(y)
    adjList[y].append(x)

for i in range(n):
    print(i,"->",adjList[i])


