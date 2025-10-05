def has_cycle_dfs_adjacency_matrix(graph):
    visited = set()

    def dfs(node, parent):
        visited.add(node)

        for i, connected in enumerate(graph[node]):
            if connected:
                if i not in visited:
                    if dfs(i, node):
                        return True

                elif i != parent:
                    return True

        return False

    for i in range(len(graph)):
        if i not in visited:
            if dfs(i, -1):
                return True

    return False


def has_cycle_dfs_adjacency_list(graph):
    visited = set()

    def dfs(node, parent):
        visited.add(node)

        for neighbour in graph[node]:
            if neighbour not in visited:
                if dfs(neighbour, node):
                    return True

            elif neighbour != parent:
                return True

        return False

    for vertex in graph:
        if vertex not in visited:
            if dfs(vertex, -1):
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

print("Graph1 has cycle (BFS)?", has_cycle_dfs_adjacency_list(graph1))  # True
print("Graph2 has cycle (BFS)?", has_cycle_dfs_adjacency_list(graph2))  # False

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

print("Graph1 has cycle (DFS)?", has_cycle_dfs_adjacency_matrix(matrix_graph1))  # True
print("Graph2 has cycle (DFS)?", has_cycle_dfs_adjacency_matrix(matrix_graph2))  # False

