import heapq
from collections import deque


def sortest_path_in_ug(graph, src):
    n = len(graph)
    visited = [0] * n
    dist = [-1] * n

    q = deque([src])
    visited[src] = 1
    dist[src] = 0

    while q:
        node = q.popleft()

        for nei in graph[node]:
            if not visited[nei]:
                visited[nei] = 1
                dist[nei] = dist[node] + 1
                q.append(nei)

    return dist


def shortest_path_in_dg(V, edges, src):
    graph = {i: [] for i in range(V)}
    indegree = [0] * V
    dist = [float('inf')] * V

    for u, v, w in edges:
        graph[u].append((v, w))
        indegree[v] += 1

    q = deque([i for i in range(V) if indegree[i] == 0])
    topo = []

    while q:
        node = q.popleft()
        topo.append(node)
        for nei, _ in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)

    dist[src] = 0
    for u in topo:
        if dist[u] != float('inf'):
            for v, w in graph[u]:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w

    return [d if d != float('inf') else -1 for d in dist]


def dijkstra(V, edges, src):
    graph = {i: [] for i in range(V)}
    dist = [float('inf')] * V

    for u, v, w in edges:
        graph[u].append((v, w))

    heap = [(0, src)]

    while heap:
        curr_dist, node = heapq.heappop(heap)

        if curr_dist > dist[node]:
            continue

        for nei, w in graph[node]:
            new_dist = dist[node] + w
            if new_dist < dist[nei]:
                dist[nei] = new_dist
                heapq.heappush(heap, (new_dist, nei))

    return dist





