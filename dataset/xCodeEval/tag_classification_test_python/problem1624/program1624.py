    n,k=map(int,input().split())
def go(l, r, need, alph):
        m = l + (r-l)/2
        if need < m:
            return go(l, m-1, need, alph-1)
        elif need > m:
            return go(m+1, r, need, alph-1)
        else:
            return alph
    print(go(1,2**n) - 1,k,n)