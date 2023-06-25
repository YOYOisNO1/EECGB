    class UnionFind:
    def __init__(self,size):
            self.table = [-1]*size
            
    def find(self, x):
            if self.table[x] < 0: return x
            else:
                self.table[x] = self.find(self.table[x])
                return self.table[x]
                
    def union(self, x, y):
            s1 = self.find(x)
            s2 = self.find(y)
            if s1 != s2:
                self.table[s2] = s1
                return True
            return False
            
    def get(self):
            d = {}
            for i in xrange(len(self.table)):
                if self.table[i] == -1:
                    idx = i
                else:
                    idx = self.find(i)
                if idx not in d:
                    d[idx] = []
                d[idx].append(i)
            return d
    
def gcd(a,b):
        while True:
            c = a%b
            if c==0: return b
            a = b
            b = c
    
def lcm(a,b):
        return a*b/gcd(a,b)
    
    n=int(input())
    c=map(int,input().split())
    for i in xrange(n):
        c[i] -= 1
    uf = UnionFind(n)
    for i in xrange(n):
        uf.union(i,c[i])
    g = uf.get()
    gs = []
    isValid = True
    for vs in g.values():
        start = vs[0]
        now = vs[0]
        for i in xrange(len(vs)):
            now = c[now]
        if start != now: isValid = False
        else:
            if len(vs)%2==0: gs.append(len(vs)/2)
            else: gs.append(len(vs))
    if not isValid: print(-1)
    else:
        ans = 1
        for i in gs:
            ans = lcm(ans, i)
        print(ans)