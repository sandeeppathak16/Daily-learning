from collections import defaultdict

max_clique = []


def get_max_clique(R, P, X, graph):
    global max_clique

    if not P and not X:
        if len(R) > len(max_clique):
            max_clique = list(R)
        return

    for v in list(P):
        get_max_clique(
            R | {v},
            P & graph[v],
            X & graph[v],
            graph
        )

        P.remove(v)
        X.add(v)


def solve(filename="23.txt"):
    global max_clique

    graph = defaultdict(set)

    with open(filename, "r") as f:
        for line in f:
            source, destination = line.strip().split("-")

            graph[source].add(destination)
            graph[destination].add(source)

    triangles = set()

    for source, neighbours in graph.items():
        for neighbour in neighbours:
            common_nodes = graph[source] & graph[neighbour]

            for common_node in common_nodes:
                triangles.add(
                    tuple(sorted([source, neighbour, common_node]))
                )

    part1 = 0

    for triangle in triangles:
        if any(node.startswith("t") for node in triangle):
            part1 += 1

    print(f"Part 1: {part1}")
    
    get_max_clique(
        set(),
        set(graph.keys()),
        set(),
        graph
    )

    password = ",".join(sorted(max_clique))

    print(f"Largest Clique: {sorted(max_clique)}")
    print(f"Part 2 Password: {password}")


solve()