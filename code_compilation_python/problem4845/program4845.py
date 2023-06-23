def print4(x):
        return '%s%s%s%s' % ( x/1000, (x/100)%10, (x/10)%10, x%10)
    
def printall(n,m,v):
        count = 0
        for i in range(10000):
            for j in v[(abs(n-i), 4)]:
                if count == m:
                    return
                print '%s%s' % (print4(i), print4(j))
                count += 1
    
    v = {}
    e = {}
    for i in range(10000):
        for j in range(1,5):
            e[(i,j)] = set()
            v[(i,j)] = set()
    
    for i in range(10):
        e[(i,1)].add(i)
        v[(i,1)].add(i)
    
    for i in range(0,100):
        e[(i,2)].add(i)
        v[(i,2)].add(i)
        d, u = i/10, i%10
        pos = [d+u, abs(d-u), d*u]
        for j in pos:
            e[(i, 2)].add(j)
            v[(j,2)].add(i)
    
    for i in range(0,1000):
        e[(i,3)].add(i)
        v[(i,3)].add(i)
        cuts = []
        cuts.append(( (i/100, 1), (i%100, 2) ))
        cuts.append(( (i/10, 2), (i%10, 1) ))
        for one, two in cuts:
            pos = []
            for x in e[one]:
                for y in e[two]:
                    pos.append(x+y)
                    pos.append(x*y)
                    pos.append(abs(x-y))
            pos = set(pos)
            for j in pos:
                e[(i, 3)].add(j)
                v[(j, 3)].add(i)
    
    for i in range(0,10000):
        e[(i,4)].add(i)
        v[(i,4)].add(i)
        cuts = []
        cuts.append(( (i/1000, 1), (i%1000, 3) ))
        cuts.append(( (i/100, 2), (i%100, 2) ))
        cuts.append(( (i/10, 3), (i%10, 1) ))
        for one, two in cuts:
            pos = []
            for x in e[one]:
                for y in e[two]:
                    pos.append(x+y)
                    pos.append(x*y)
                    pos.append(abs(x-y))
            pos = set(pos)
            for j in pos:
                e[(i, 4)].add(j)
                v[(j, 4)].add(i)
    
    n, m = map(int, input().split())
    printall(n,m,v)