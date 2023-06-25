    class DisjoinSet:
    def __init__(self, N):
            self.sets = [i for i in xrange(N)]
            self.rank = [0 for i in xrange(N)]
    
    def root(self, x):
            if self.sets[x] == x:
                return x
            return self.root(self.sets[x])
    
    def union(self, x, y):
            root_x = self.root(x)
            root_y = self.root(y)
            if self.rank[root_x] > self.rank[root_y]:
                self.sets[root_y] = root_x
            else:
                if self.rank[root_x] == self.rank[root_y]:
                    self.rank[root_y] += 1
                self.sets[root_x] = root_y
    
def test_tree():
        sets = DisjoinSet(N+1)
        nodes = [0 for i in xrange(N+1)]
        not_t = 0
        for i in xrange(N-1):
            edge = edges[x[i]]
            v1 = sets.root(edge[0])
            v2 = sets.root(edge[1])
            if v1 == v2:
                return False
            nodes[edge[0]] += 1
            nodes[edge[1]] += 1
            
        Ktupik = nodes.count(1)
        if Ktupik != K:
            return False
        return True
            
    
    N, M, K = map(int, input().split())
    
    edges = []
    for i in xrange(M):
        v1, v2 = map(int, input().split())
        edges.append((v1, v2))
    
    x = [i for i in xrange(M)]
    fin = [i for i in xrange(M - N + 1, M)]
    count = 0
    while True:
        if test_tree():
            count += 1
        if x[:N-1] == fin:
            break
        s = N - 2
        while not ( x[s] < M - N + s + 1):
            s -= 1
        x[s] += 1
        for i in xrange(s + 1, M):
            x[i] = x[i-1] + 1
    print count