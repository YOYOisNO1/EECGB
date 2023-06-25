def ccw(A, B, C):
        return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])
    
    
def intersect(A, B, C, D):
        return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)
    
    
    R, B = map(int, input().split())
    
    rs = []
    bs = []
    for r in range(R):
        rs.append(list(map(int, input().split())))
    for r in range(B):
        bs.append(list(map(int, input().split())))
    
    if R != B:
        print('No')
    else:
    def rec(at, done, remain):
            if at >= B:
                return True
            for b in remain:
                for r, d in zip(rs, done):
                    if intersect(r, bs[d], rs[at], bs[b]):
                        break
                else:
                    ok = rec(at + 1, done + [b], remain - {b})
                    if ok:
                        return True
            return False
    
        print(['NO', 'YES'][rec(0, [], set(range(B)))])