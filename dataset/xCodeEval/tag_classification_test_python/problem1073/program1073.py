    from itertools import permutations 
    
def calc(m, t):
        if t == 0:
            ret = 1 << 60
            perm = permutations([0, 1, 2, 3, 4, 5])
            for p in list(perm):
                p = list(p)
                A = a[:]
                B = b[:]
                res = n
                for i in range(6):
                    if m & (1 << p[i]):
                        val = min(A[int(p[i] / 2)], B[(int(p[i] / 2) + 2) % 3])
                        A[int(p[i] / 2)] -= val
                        B[(int(p[i] / 2) + 2) % 3] -= val
                        res -= val
                    else:
                        val = min(A[int(p[i] / 2)], B[int(p[i] / 2)])
                        A[int(p[i] / 2)] -= val
                        B[int(p[i] / 2)] -= val
                        res -= val
                ret = min(res, ret)
            return ret
        else:
            ret = 0
            perm = permutations([0, 1, 2, 3, 4, 5])
            for p in list(perm):
                p = list(p)
                A = a[:]
                B = b[:]
                res = 0
                for i in range(6):
                    if m & (1 << p[i]):
                        val = min(A[int(p[i] / 2)], B[(int(p[i] / 2) + 1) % 3])
                        A[int(p[i] / 2)] -= val
                        B[(int(p[i] / 2) + 1) % 3] -= val
                        res += val
                    else:
                        val = min(A[int(p[i] / 2)], B[int(p[i] / 2)])
                        A[int(p[i] / 2)] -= val
                        B[int(p[i] / 2)] -= val
                ret = max(ret, res)
            return ret
    
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    mn, mx = 1 << 60, 0
    for t in (0, 1):
        for m in range(1 << 6):
            if t == 0: mn = min(mn, calc(m, t))
            else: mx = max(mx, calc(m, t))
    print(mn, mx)