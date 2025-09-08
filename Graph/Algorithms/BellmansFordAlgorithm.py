def bellman_ford(vertices, edges, start):
    # Step 1: Initialize distances
    distance = {v: float("inf") for v in vertices}
    distance[start] = 0

    # Step 2: Relax edges (V - 1) times
    for _ in range(len(vertices) - 1):
        for u, v, w in edges:  # u = from, v = to, w = weight
            if distance[u] != float("inf") and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w

    # Step 3: Check for negative weight cycles
    for u, v, w in edges:
        if distance[u] != float("inf") and distance[u] + w < distance[v]:
            print("Graph contains a negative weight cycle!")
            return None

    return distance


# Example Usage
vertices = ["A", "B", "C", "D"]
edges = [
    ("A", "B", 4),
    ("A", "C", 5),
    ("B", "C", -3),
    ("B", "D", 6),
    ("C", "D", 2)
]

start = "A"
shortest_paths = bellman_ford(vertices, edges, start)
print("Shortest paths from", start, ":", shortest_paths)
