    from sys import stdin
    
def gen(orig, no, depth):
        if depth == 4:
            return int(no == orig)
        res = 0
        for i, n in enumerate(arr):
            if not used[i]:
                used[i] = True
                if n < no:
                    return 0
                res += gen(orig, no % n, depth+1)
                used[i] = False
        return res
    
    used = [False]*4
    MINL = 7
    arr = [int(x) for x in stdin.readline().split()]
    up, down = arr[4:]
    arr = arr[:4]
    res = 0
    for orig in xrange(up, down+1):
        if gen(orig, orig, 0) >= MINL:
            res += 1
    print(res)