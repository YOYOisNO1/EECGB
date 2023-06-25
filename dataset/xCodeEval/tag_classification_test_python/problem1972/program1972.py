    import sys
    import collections
    
    s = sys.stdin.readline().strip()
    nb, ns, nc = list(map(int,sys.stdin.readline().strip().split(' ')))
    pb, ps, pc = list(map(int,sys.stdin.readline().strip().split(' ')))
    r = int(sys.stdin.readline().strip())
    
def solve(nb, ns, nc, c, r, tc):
        #print('calling:')
        #print(nb, ns, nc, r)
        if nb == 0 and ns == 0 and nc == 0:
            return r // tc
    
        mb, ms, mc = 0, 0, 0
        if nb < c['B']:
            mb = c['B'] - nb
        if ns < c['S']:
            ms = c['S'] - ns
        if nc < c['C']:
            mc = c['C'] - nc
    
    
        cost = mb*pb + ms*ps + mc*pc
        #print(mb, ms, mc)
        #print(cost)
        if r >= cost:
            nb += mb
            nc += mc
            ns += ms
            return 1 + solve(nb - c['B'], ns - c['S'], nc - c['C'], c, r - cost, tc)
        else:
            return 0
    
    
    c = collections.Counter(s)
    if c['B'] == 0:
        nb = 0
    if c['C'] == 0:
        nc = 0
    if c['S'] == 0:
        ns = 0
    tc = pb * c['B'] + pc * c['C'] + ps * c['S']
    print(solve(nb, ns, nc, c, r, tc))