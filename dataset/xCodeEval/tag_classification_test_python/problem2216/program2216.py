    import sys
    
    
def play_card_Afirst(A,B):
        if max(A)>=max(B):
            return 'Alice'
        else:
            return 'Bob'
def play_card_Bfirst(A,B):
        if max(B)>= max(A):
            return 'Bob'
        return 'Alice'
    
def shuffle(va, n, vb):
        return va[sum(vb)%n]
    
def double_sort(A,B,n):
        tAB = list(zip(A,B))
    #     print(tAB)
        sort_rank = sorted(enumerate(tAB), key=lambda x:x[1])
        for (_,x),(_,y) in zip(sort_rank[:-1],sort_rank[1:]):
    #         print(x,y)
            if (x[0]-y[0])*(x[1]-y[1])<0:
                print(-1)
                return
        l = [x[1][0] for x in sort_rank]
        assert(all(l[i] <= l[i+1] for i in range(len(l) - 1)))
        l = [x[1][1] for x in sort_rank]
        assert(all(l[i] <= l[i+1] for i in range(len(l) - 1)))
        swaps = []
        now_loc = list(range(n))
        now_value = list(range(n))
        for i,(after,_) in enumerate(sort_rank):
            LocJ = now_loc[after]
            if LocJ!=i:
                valueI = now_value[i]
                swaps.append((LocJ,i))
                now_loc[after] = i
                now_loc[valueI] = LocJ
                now_value[i] = after
                now_value[LocJ] = valueI
        print(len(swaps))
        for x,y in swaps:
            print(x+1,y+1)
    cache = {}
def RL(x,n):
        if x in cache.keys():
            return cache[x]
        digits = list(str(x))
        if len(digits)>n:
            return float('inf')
        minD = int(min([k for k in digits if k != '0']))
        maxD = int(max(digits))
        if len(digits) == n :
            return 0
        if maxD == 1:
            return float('inf') 
        cache[x] = 1+min([RL(x*b,n) for b in [int(k) for k in digits if k not in '01']])
        return cache[x]
    
     
    n,x = [int(x) for x in sys.stdin.readline().split()]
    result = RL(x,n)
    if result == float('inf'):
        print(-1)
    else:
        print((result))
    '''
    r = int(sys.stdin.readline())
    for j in range(r):
        n = int(sys.stdin.readline())
        A = [int(x) for x in sys.stdin.readline().split()]
        B = [int(x) for x in sys.stdin.readline().split()]
        print(double_sort(A,B,n))'''