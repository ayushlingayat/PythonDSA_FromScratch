n = 6  # number of nodes
e = 7  # number of edges

edges = [(0, 1), (0, 3), (0, 4), (1, 2), (1, 5), (2, 4), (3, 4)]  # edges

# Initialize the adjacency matrix with all zeros
adjMatrix = [[0] * n for _ in range(n)]

# Iterate through each edge in the list
for edge in edges:
    # Get the two nodes from the current edge
    x = edge[0]
    y = edge[1]

    # For an undirected graph, the connection is two-way.
    # Set the value to 1 for both adjMatrix[x][y] and adjMatrix[y][x].
    adjMatrix[x][y] = 1
    adjMatrix[y][x] = 1

# Print the resulting adjacency matrix
for row in adjMatrix:
    print(row)