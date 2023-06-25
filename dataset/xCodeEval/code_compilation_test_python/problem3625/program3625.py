    import collections
    import sys
def recur(_list):
        idx = -1
        next_list = []
        for i,x in enumerate(_list):
            if x > 1:
                idx = i
                q = _list[idx] // 2
                r = _list[idx] % 2
                next_list += [q,r,q]
            else:
                next_list += [x]
        if idx == -1:
            return _list
        else:
            return recur(next_list)
    
    sys.setrecursionlimit(100000)
    n,s,e = list(map(int,input().split(' ')))
    _list = [n]
    print(collections.Counter(recur(_list[:])[s-1:e])[1])