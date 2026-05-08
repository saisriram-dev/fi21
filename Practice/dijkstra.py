import heapq


def dijkstra(graph, source):
    # graph: adjacency list {node: [(neighbor, weight), ...]}

    # Step 1: Initialize distances
    dist = {node: float("inf") for node in graph}
    dist[source] = 0

    # Min heap: (distance, node)
    pq = [(0, source)]

    while pq:
        current_dist, node = heapq.heappop(pq)

        # Skip if we already found a better path
        if current_dist > dist[node]:
            continue

        # Explore neighbors
        for neighbor, weight in graph[node]:
            distance = current_dist + weight

            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return dist


# 🔍 Example usage
graph = {"A": [("B", 4), ("C", 1)], "B": [("D", 1)], "C": [("B", 2), ("D", 5)], "D": []}

print(dijkstra(graph, "A"))
