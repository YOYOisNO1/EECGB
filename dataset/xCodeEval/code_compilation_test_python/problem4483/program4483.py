    f = open('test.txt', 'r')
    from math import factorial
    fac = factorial
    
def dfs(lst):
        sums = [[] for i in xrange(k+1)]
        sums[0].append(0)
        while len(lst)>0:
            cur = lst.pop(0)
            length = [len(sums[i]) for i in xrange(k+1)]
            for i in xrange(k+1):
                for j in xrange(length[i]):
                    if sums[i][j] + cur <=s:
                        sums[i].append(sums[i][j]+cur)
                        temp = sums[i][j]+fac(cur)
                        if cur<19 and i<k and temp<=s:
                            sums[i+1].append(sums[i][j]+fac(cur))
        return sums
    
def binsearch(x, k):
        
    
    n, k, s = map(int, f.readline().split())
    a = [int(item) for item in f.readline().split()]
    a.sort()
    
    first = dfs(a[:n/2])
    second = dfs(a[n/2:])
    
    for i in xrange(k+1):
        for item in first[i]:
            binsearch(item, k-i)
    
    f.close()