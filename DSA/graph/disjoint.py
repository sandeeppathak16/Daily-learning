class DisjointSetRank:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find_parent(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find_parent(self.parent[node])
        return self.parent[node]

    def union_by_rank(self, u, v):
        pu = self.find_parent(u)
        pv = self.find_parent(v)

        if pu == pv:
            return

        # Attach smaller rank tree under bigger rank tree
        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv
        elif self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu
        else:
            # Same rank → attach one under the other and increase rank
            self.parent[pv] = pu
            self.rank[pu] += 1


class DisjointSetSize:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def find_parent(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find_parent(self.parent[node])
        return self.parent[node]

    def union_by_rank(self, u, v):
        pu = self.find_parent(u)
        pv = self.find_parent(v)

        if pu == pv:
            return

        # Attach smaller size tree under bigger size tree
        if self.size[pu] < self.size[pv]:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
        elif self.size[pu] > self.size[pv]:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
        else:
            # Same size → attach one under the other and increase size
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]

