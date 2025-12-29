import heapq


def dijkstra(graph, start):

    dist = {v: float("inf") for v in graph}
    prev = {v: None for v in graph}

    dist[start] = 0
    pq = [(0, start)]

    while pq:
        cur_dist, u = heapq.heappop(pq)

        if cur_dist != dist[u]:
            continue

        for v, w in graph[u]:
            new_dist = cur_dist + w
            if new_dist < dist[v]:
                dist[v] = new_dist
                prev[v] = u
                heapq.heappush(pq, (new_dist, v))

    return dist, prev


def build_path(prev, start, target):
    
    if start == target:
        return [start]
    if prev[target] is None:
        return None 

    path = []
    cur = target
    while cur is not None:
        path.append(cur)
        if cur == start:
            break
        cur = prev[cur]

    if path[-1] != start:
        return None
    return path[::-1]


if __name__ == "__main__":
    graph = {
        "A": [("B", 5), ("C", 1)],
        "B": [("A", 5), ("C", 2), ("D", 1)],
        "C": [("A", 1), ("B", 2), ("D", 4), ("E", 8)],
        "D": [("B", 1), ("C", 4), ("E", 3), ("F", 6)],
        "E": [("C", 8), ("D", 3)],
        "F": [("D", 6)],
    }

    start = "A"
    dist, prev = dijkstra(graph, start)

    print(f"Найкоротші відстані від {start}:")
    for node in dist:
        print(f"{start} -> {node}: {dist[node]}")

    
    target = "F"
    path = build_path(prev, start, target)
    print(f"\nМаршрут {start} -> {target}: {path}")
