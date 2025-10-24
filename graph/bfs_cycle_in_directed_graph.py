from collections import deque


def has_cycle_bfs_adjacency_matrix(graph):
    n = len(graph)
    indegree = [0] * n

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                indegree[j] += 1

    queue = deque([i for i in range(n) if indegree[i] == 0])
    count = 0
    while queue:
        node = queue.popleft()
        count += 1

        for nei, connected in enumerate(graph[node]):
            if connected:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

    return count != n


def has_cycle_bfs_adjacency_list(graph):
    indegree = {node: 0 for node in graph}

    for node in graph:
        for nei in graph[node]:
            indegree[nei] += 1

    queue = deque([node for node in graph if indegree[node] == 0])

    count = 0
    while queue:
        node = queue.popleft()
        count += 1

        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                queue.append(nei)

    return count != len(graph)


graph = {
    0: [1],
    1: [2],
    2: [3],
    3: [1]  # cycle here
}

print(has_cycle_bfs_adjacency_list(graph))  # True

graph = [
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [0, 1, 0, 0]  # cycle
]
print(has_cycle_bfs_adjacency_matrix(graph))  # True
