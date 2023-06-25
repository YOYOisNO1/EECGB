    import itertools
    
    try: input = input
    except: pass
    
def solve():
        # read
        n, k = rint(), rint()
        fs = [[] for _ in range(n)]
        dl = [[] for _ in range(n)]
        group = [i for i in range(n)]
        for i in range(k):
            i, j = list(map(int, input().split()))
            fs[i-1].append(j-1)
            fs[j-1].append(i-1)
        m = int(input())
        for i in range(m):
            i, j = list(map(int, input().split()))
            dl[i-1].append(j-1)
            dl[j-1].append(i-1)
        
        # solve
        for i in range(n):
            if group[i] == i:
                spreadgroup(i, fs, group, group[i])
        genum = sorted(enumerate(group), key=lambda x: x[1])
        gr = [list(first(g)) for (k, g) in itertools.groupby(genum, key=lambda x: x[1])]
        gr.sort(key=lambda x: len(x), reverse=True)
        for pg in gr:
            have = set(pg)
            dislike = set()
            for x in (dl[i] for i in pg):
                for t in x:
                    dislike.add(int(t))
            if have.isdisjoint(dislike):
                print(len(pg))
                return
        print(0)
                
def spreadgroup(i, fs, group, curgroupid):
        for f in fs[i]:
            if group[f] != curgroupid:
                group[f] = curgroupid
                spreadgroup(f, fs, group, curgroupid)   
        
def first(x): 
        for i in x: yield i[0]
        
def rint(): return int(input())
    
    solve()