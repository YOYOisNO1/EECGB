    n = 0
    k = 0
    t = 0
    P = {}
    used = []
    
def third(x, n=2):
        for i in x:
            yield i[n]
    
def solve():
        global n, k, t, P, used
        read = reader()
        n, k, t = list(map(int, next(read).split()))
        t -= 1
        for i in range(n):
            P[i] = []
        used = [False] * n
        for i in range(k):
            m1, m2, r = list(map(int, next(read).split()))
            P[m1-1].append((m2-1, r))
        comb = []
        rec(0, comb)
        comb.sort(key=lambda x: sum(third(x)))
        comb.insert(0, (-1, -1, 0))
        print(sum(third(comb[t])))
    
def rec(i, comb, currentpairs = None):
        global n, k, t, P, used
        if not i < n:
            return
        if currentpairs == None:
            currentpairs = []
        for (m2, r) in P[i]:
            if used[m2]:
                continue
            used[m2] = True
            cp = currentpairs[:]
            cp.append((i, m2, r))
            comb.append(cp)
            rec(i+1, comb, cp)
            used[m2] = False
            
    
def reader():
        USE_FILE = True
        if __name__ == "__main__" and USE_FILE:
            with open("F.in", "r") as fin:
                while True:
                    yield next(fin)
        else:
            try: input = input
            except: pass
            while True:
                yield input()
    
    solve()