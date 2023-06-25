    from sys import stdin
    
    
    class disjointset:
    def __init__(self, n):
            self.rank, self.parent, self.n, self.nsets = [0] * (n + 1), [i for i in range(n + 1)], n, [1] * (n + 1)
    
    def find(self, x):
            xcopy = x
            while x != self.parent[x]:
                x = self.parent[x]
    
            while xcopy != x:
                self.parent[xcopy], xcopy = x, self.parent[xcopy]
    
            return x
    
    def union(self, x, y):
            xpar, ypar = self.find(x), self.find(y)
    
            # already union
            if xpar == ypar:
                return
            # perform union by rank
            par, child = xpar, ypar
            if self.rank[xpar] < self.rank[ypar]:
                par, child = ypar, xpar
    
            elif self.rank[xpar] == self.rank[ypar]:
                self.rank[xpar] += 1
    
            self.parent[child] = par
            self.nsets[par] += self.nsets[child]
            self.n -= 1
    
    
    p, k = map(int, stdin.readline().split())
    mod = 10 ** 9 + 7
    if k == 0:
        print(pow(p, p - 1, mod))
    elif k == 1:
        print(pow(p, p, mod))
    else:
        dis = disjointset(p - 1)
        for i in range(1, p):
            dis.union(i, (i * k) % p)
    
        print(pow(p, dis.n, mod))