class UnionFind:
    def __init__(self, grid):
        rows, cols = len(grid), len(grid[0])
        self.parent = {}
        self.rank = {}
        self.count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    idx = r * cols + c
                    self.parent[idx] = idx
                    self.rank[idx] = 0
                    self.count += 1

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return

        if self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1

        self.count -= 1


def num_islands(grid):
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    uf = UnionFind(grid)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                idx = r * cols + c

                if r + 1 < rows and grid[r + 1][c] == '1':
                    uf.union(idx, (r + 1) * cols + c)

                if c + 1 < cols and grid[r][c + 1] == '1':
                    uf.union(idx, r * cols + (c + 1))

    return uf.count
