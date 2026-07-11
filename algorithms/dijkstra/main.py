import heapq


def dijkstra(graph, source_node):
    distances = {node: float("inf") for node in graph}
    distances[source_node] = 0

    visited = set()
    to_visit = [(0, source_node)]

    while to_visit:
        current_distance, current_node = heapq.heappop(to_visit)

        if current_node in visited:
            continue

        for neighbor, weight in graph[current_node]:
            if neighbor in visited:
                continue

            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(to_visit, (distance, neighbor))

            visited.add(current_node)

    return distances

graph = {
    "A": [("B", 4), ("C", 2)],
    "B": [("A", 4), ("D", 5)],
    "C": [("A", 2), ("D", 1), ("E", 7)],
    "D": [("B", 5), ("C", 1)],
    "E": [("C", 7)]
}

source_node = "A"

print(dijkstra(graph, source_node))
