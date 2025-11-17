nodes = {
    "A": (0, 1),
    "B": (1, 2),
    "C": (2, 1),
    "D": (1, 0)
}

edges = [
    ("A", "B", 4),
    ("A", "C", 5),
    ("B", "C", -2),
    ("C", "D", 3),
    ("B", "D", 4)
]


# Bellman-Ford Implementation
def bellman_ford(nodes, edges, source):
    dist = {node: float("inf") for node in nodes}
    dist[source] = 0

    for _ in range(len(nodes) - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Negative cycle check
    neg_cycle = False
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            neg_cycle = True
            break

    return dist, neg_cycle


dist, neg_cycle = bellman_ford(nodes, edges, "A")
