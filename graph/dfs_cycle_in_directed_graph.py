def has_cycle_dfs_adjacency_matrix(graph):
    n = len(graph)
    visited = [0] * n
    stack = set()

    def dfs(node, visited, stack):
        if node in stack:
            return True

        if visited[node]:
            return False

        visited[node] = 1
        stack.add(node)

        for j in range(len(graph[node])):
            if graph[node][j]:
                if dfs(j, visited, stack):
                    return True

        stack.remove(node)
        return False

    for node in range(n):
        if not visited[node]:
            if dfs(node, visited, stack):
                return True

    return False


def has_cycle_dfs_adjacency_list(graph):
    visited = set()
    stack = set()

    def dfs(node, visited, stack):
        if node in stack:
            return True

        if node in visited:
            return False

        visited.add(node)
        stack.add(node)

        for j in graph[node]:
            if dfs(j, visited, stack):
                return True

        stack.remove(node)
        return False

    for node in graph:
        if node not in visited:
            if dfs(node, visited, stack):
                return True

    return False


graph = [
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [0, 1, 0, 0]  # cycle 1->2->3->1
]

print(has_cycle_dfs_adjacency_matrix(graph))  # True

graph = {
    0: [1],
    1: [2],
    2: [3],
    3: [1]  # cycle
}

print(has_cycle_dfs_adjacency_list(graph))  # True

