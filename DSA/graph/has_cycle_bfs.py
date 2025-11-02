from collections import deque


def has_cycle_bfs_adjacency_matrix(graph):
    visited = [False] * len(graph)

    for node in range(len(graph)):
        if not visited[node]:
            queue = deque([(node, -1)])
            visited[node] = True

            while queue:
                n, p = queue.popleft()

                for neighbour, connected in enumerate(graph[n]):
                    if connected:
                        if not visited[neighbour]:
                            visited[neighbour] = True
                            queue.append((neighbour, n))
                        elif neighbour != p:
                            return True

    return False


def has_cycle_bfs_adjacency_list(graph):
    visited = set()

    for node in graph:
        if node not in visited:
            queue = deque([(node, -1)])
            visited.add(node)

            while queue:
                n, p = queue.popleft()

                for neighbour in graph[n]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append((neighbour, n))
                    elif neighbour != p:
                        return True

    return False


graph1 = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2]
}
graph2 = {
    0: [1],
    1: [0, 2],
    2: [1, 3],
    3: [2]
}

print("Graph1 has cycle (BFS)?", has_cycle_bfs_adjacency_list(graph1))  # True
print("Graph2 has cycle (BFS)?", has_cycle_bfs_adjacency_list(graph2))  # False

matrix_graph1 = [
    [0, 1, 1, 0],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [0, 0, 1, 0]
]

matrix_graph2 = [
    [0, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 0]
]

print("Graph1 has cycle (DFS)?", has_cycle_bfs_adjacency_matrix(matrix_graph1))  # True
print("Graph2 has cycle (DFS)?", has_cycle_bfs_adjacency_matrix(matrix_graph2))  # False

