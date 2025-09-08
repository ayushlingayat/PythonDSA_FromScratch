import heapq

def dijkstra(graph, start):
    # graph: adjacency list -> {node: [(neighbor, weight), ...]}
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    pq = [(0, start)]  # (distance, node)

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # If this path is already longer, skip
        if current_distance > distances[current_node]:
            continue

        # Update distances of neighbors
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


# Example Usage
graph = {
    "A": [("B", 4), ("C", 1)],
    "B": [("A", 4), ("C", 2), ("D", 5)],
    "C": [("A", 1), ("B", 2), ("D", 8)],
    "D": [("B", 5), ("C", 8)]
}

start = "A"
shortest_paths = dijkstra(graph, start)
print("Shortest paths from A:", shortest_paths)

