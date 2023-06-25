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
                        if cur<19 and i<k and sums[i][j]+fac(cur)<=s:
                            sums[i+1].append(sums[i][j]+fac(cur))
        return sums
    
#def search(x, k):
    #    count = 0
    #    for i in xrange(k+1):
    #        count += second[i].count(x)
    #    return count
    
    n, k, s = map(int, f.readline().split())
    a = [int(item) for item in f.readline().split()]
    a.sort()
    
    first = dfs(a[:n/2])
    second = dfs(a[n/2:])
    
    df = [{} for i in xrange(k+1)]
    ds = [{} for i in xrange(k+1)]
    for i in xrange(k+1):
        for item in set(first[i]):
            df[i][item] = first[i].count(item)
        for item in set(second[i]):
            ds[i][item] = second[i].count(item)
    #for i in xrange(k+1):
    #    second[i].sort()
    count = 0
    for i in xrange(k+1):
        for sum1 in df[i]:
            for kk in xrange(k-i+1):
                if s-sum1 in ds[kk]:
                    count += df[i][sum1]*ds[kk][s-sum1]
    print count