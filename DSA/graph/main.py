class graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = []
        self.gdict = gdict

    def get_vertex(self):
        return list(self.gdict.keys())

    def get_edges(self):
        edges = []
        for v in self.gdict:
            for nv in self.gdict[v]:
                if {v, nv} not in edges:
                    edges.append({v, nv})
        return edges

    def adding_vertex(self, v):
        if v not in self.gdict:
            self.gdict[v] = []

    def adding_edge(self, edge):
        edge = set(edge)
        (v1, v2) = tuple(edge)

        if v1 in self.gdict:
            self.gdict[v1].append(v2)
        else:
            self.gdict[v1] = [v2]


graph_elements = {
    "a": ["b", "c"],
    "b": ["a", "d"],
    "c": ["a", "d"],
    "d": ["e"],
    "e": ["d"]
}
g = graph(graph_elements)
