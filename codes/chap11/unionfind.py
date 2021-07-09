class UnionFind:
    def __init__(self, n: int):
        self.par = [-1] * n
        self.siz = [1] * n

    def root(self, x: int):
        if self.par[x] == -1:
            return x
        else:
            return self.root(self.par[x])

    def issame(self, x: int, y: int):
        return self.root(x) == self.root(y)

    def unite(self, x: int, y: int):
        x = self.root(x)
        y = self.root(y)

        if x == y:
            return False

        if self.siz[x] < self.siz[y]:
            x, y = y, x

        self.par[y] = x
        self.siz[x] += self.siz[y]
        return True

