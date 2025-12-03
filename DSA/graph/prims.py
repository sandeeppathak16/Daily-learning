import heapq


def prims(n, edges):
    graph = {node: [] for node in range(n)}

    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    mst = []
    summ = 0
    visited = [0] * n
    heap = []

    for start in range(n):
        if visited[start]:
            continue

        heapq.heappush(heap, (0, start, -1))

        while heap:
            weight, node, parent = heapq.heappop(heap)

            if visited[node]:
                continue

            visited[node] = 1

            if parent != -1:
                mst.append((parent, node))
                summ += weight

            for nei, w in graph[node]:
                if not visited[nei]:
                    heapq.heappush(heap, (w, nei, node))

    return mst, summ
