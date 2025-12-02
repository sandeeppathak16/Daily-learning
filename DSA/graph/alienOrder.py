from collections import deque, defaultdict


def alienOrder(words):
    # Step 1: graph + indegree init
    graph = defaultdict(set)
    indegree = {c: 0 for w in words for c in w}

    # Step 2: build graph by comparing adjacent words
    for w1, w2 in zip(words, words[1:]):
        min_len = min(len(w1), len(w2))

        # invalid case: ["abc", "ab"]
        if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
            return ""

        for i in range(min_len):
            if w1[i] != w2[i]:
                c1, c2 = w1[i], w2[i]
                if c2 not in graph[c1]:
                    graph[c1].add(c2)
                    indegree[c2] += 1
                break

    # Step 3: BFS (Kahn)
    queue = deque([c for c in indegree if indegree[c] == 0])
    res = []

    while queue:
        c = queue.popleft()
        res.append(c)
        for nei in graph[c]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                queue.append(nei)

    # Step 4: check cycle
    if len(res) < len(indegree):
        return ""

    return "".join(res)
