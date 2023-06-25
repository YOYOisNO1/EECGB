    
    from sys import stdin, stdout
    
def int1():
        return int(stdin.readline().strip())
    
def ints():
        return map(int, stdin.readline().strip().split(" "))
    
def arr():
        return list(stdin.readline().strip().split(" "))
    
def iarr():
        return list(ints())
    
    class DS:
    def __init__(self, n):
            self.p = [i for i in range(n)]
            self.r = [0 for _ in range(n)]
    def find(self, x):
            if self.p[x] != x:
                self.p[x] = self.find(self.p[x])
            return self.p[x]
    def merge(self, a, b):
            a = self.find(a)
            b = self.find(b)
            if a == b:
                return 0
            if self.r[a] < self.r[b]:
                p[a] = b
            else:
                p[b] = a
                if self.r[a] == self.r[b]:
                    r[a]+=1
            return 1
    
    class BIT:
    def __init__(self, n):
            self.n = n + 2
            self.arr = [0 for _ in range(self.n)]
    def inc(self, index, val):
            index += 1
            while index < self.n:
                self.arr[index] += n
                index += (index&-index)
    
    MOD = 998244353
    n,k = ints()
    memo = dict()
    memo2 = dict()
    memo3 = [[0 for _ in range(((n*(n-1))>>1)+2)] for _ in range(k+1)]
    for i in range(1,k+1):
        memo3[i][0] = 1
        for j in range(1,(n*(n-1)>>1)+2):
            memo3[i][j] = memo3[i][j-1] * i
            memo3[i][j] %= MOD
    
def mexp(b,e,m):
        if e == 0:
            return 1
        if e == 1:
            return b % m
        s = mexp(b,e>>1,m)
        return (s * s * (b if (e&1) else 1)) % m
    
def inv(x):
        if not x in memo2:
            memo2[x] = mexp(x, MOD - 2, MOD)
        return memo2[x]
    
def go(left, last):
        if left == 0:
            return 1
        if last == k:
            return 0
        st = left * 300 + last
        if not st in memo:
            scale = 1
            memo[st] = 0
            comp = n - left
            for i in range(left+1):
                ex = (comp - 1) * i + ((i * (i-1))>>1)
                memo[st] += go(left-i,last+1) * scale * memo3[k-last][ex]
                scale *= (left - i)
                scale *= inv(i+1)
                scale %= MOD
            memo[st] %= MOD
        return memo[st] 
    
    print(go(n-1,0))
    