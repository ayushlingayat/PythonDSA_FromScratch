# A simple implementation of the Disjoint Set Union (DSU) data structure
parent = []


def find(i):
    """
    Finds the representative (or parent) of the set that element i belongs to.
    Uses path compression for efficiency.
    """
    if parent[i] == i:
        return i
    # Path compression: make the current node's parent the root
    parent[i] = find(parent[i])
    return parent[i]


def union(i, j):
    """
    Merges the sets containing elements i and j.
    """
    root_i = find(i)
    root_j = find(j)
    if root_i != root_j:
        parent[root_j] = root_i
        return True  # Union was successful
    return False  # They are already in the same set


# --- Kruskal's Algorithm Implementation ---

def kruskal_mst(adjMatrix):
    global parent  # Use the global parent list for DSU
    n = len(adjMatrix)

    # Step 1: Create a list of all edges with their weights
    edges = []
    for i in range(n):
        for j in range(i + 1, n):  # Avoid duplicate edges (i,j) and (j,i)
            if adjMatrix[i][j] != 0:
                edges.append((adjMatrix[i][j], i, j))  # (weight, node1, node2)

    # Step 2: Sort the edges by weight in ascending order
    edges.sort()

    # Initialize the DSU data structure
    parent = list(range(n))

    mst_cost = 0
    num_edges = 0
    mst_edges = []

    # Step 3: Iterate through the sorted edges and build the MST
    for weight, u, v in edges:
        # Check if adding this edge creates a cycle using the DSU find operation
        if find(u) != find(v):
            # If they are not in the same set, add the edge to the MST
            union(u, v)
            mst_cost += weight
            num_edges += 1
            mst_edges.append((u, v))

            # Stop when we have n-1 edges
            if num_edges == n - 1:
                break

    return mst_cost, mst_edges




# adjacency matrix
adjMatrix = [[0, 9, 75, 0, 0],
             [9, 0, 95, 19, 42],
             [75, 95, 0, 51, 66],
             [0, 19, 51, 0, 31],
             [0, 42, 66, 31, 0]]

total_cost, mst_edges = kruskal_mst(adjMatrix)

print("Total cost of the Minimum Spanning Tree:", total_cost)
print("Edges in the MST:", mst_edges)