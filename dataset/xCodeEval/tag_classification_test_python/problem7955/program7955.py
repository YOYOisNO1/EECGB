    class DisjointSetStructure():
    def __init__(self, n):
            self.A = [[i,0,1] for i in range(n)]
            self.size = n
    def getpair(self, i):
            p = i
            while self.A[p][0] != p: p = self.A[p][0]
            j = self.A[i][0]
            while j != p:
                self.A[i][0] = p
                i, j = j, self.A[j][0]
            return (p, self.A[p][2])
    def __getitem__(self, i):
            return self.getpair(i)[0]
    def union(self, i, j):
            u, v = self[i], self[j]
            if u == v: return
            self.size -= 1
            if self.A[u][1] > self.A[v][1]:
                self.A[v][0] = u
                self.A[u][2] += self.A[v][2]
            else:
                self.A[u][0] = v
                self.A[v][2] += self.A[u][2]
                if self.A[u][1] == self.A[v][1]:
                    self.A[v][1] += 1
    def __len__(self): return self.size
    
    n = int(input())
    k = int(input())
    D = DisjointSetStructure(n)
    for i in range(k):
        u, v = [int(x) - 1 for x in input().split()]
        D.union(u, v)
    l = int(input())
    friendly = [True for i in range(n)]
    for i in range(l):
        u, v = [int(x) - 1 for x in input().split()]
        if D[u] == D[v]: friendly[D[u]] = False
    
    print(max(D.getpair(i)[1] if friendly[D[i]] else 0 for i in range(n)))