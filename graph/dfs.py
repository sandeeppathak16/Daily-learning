def dfs_adjacency_matrix(graph, node, visited):
    visited.add(node)
    print(node)

    for i, connected in enumerate(graph[node]):
        if connected and i not in visited:
            visited.add(i)
            dfs_adjacency_matrix(graph, i, visited)


def dfs_adjacency_list(graph, node, visited):
    visited.add(node)
    print(node)

    for neighbour in graph[node]:
        if neighbour not in visited:
            visited.add(neighbour)
            dfs_adjacency_list(graph, neighbour, visited)


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

print(dfs_adjacency_matrix(matrix_graph, 0, set()))
print(dfs_adjacency_list(dict_graph, 0, set()))

