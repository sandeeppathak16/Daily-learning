from collections import deque


def bfs_adjacency_matrix(graph, start):
    queue = deque([(start, 0)])
    visited = set()
    visited.add(start)
    level_order = {}

    while queue:
        node, level = queue.popleft()

        if level not in level_order:
            level_order[level] = []

        level_order[level].append(node)

        for i, connected in enumerate(graph[node]):
            if connected and i not in visited:
                visited.add(i)
                queue.append((i, level + 1))

    return level_order


def bfs_adjacency_list(graph, start):
    queue = deque([(start, 0)])
    visited = set()
    visited.add(start)
    level_order = {}

    while queue:
        node, level = queue.popleft()

        if level not in level_order:
            level_order[level] = []

        level_order[level].append(node)

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour, level + 1))

    return level_order


matrix_graph = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0]
]


dict_graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2]
}

print(bfs_adjacency_matrix(matrix_graph, 0))
print(bfs_adjacency_list(dict_graph, 0))

