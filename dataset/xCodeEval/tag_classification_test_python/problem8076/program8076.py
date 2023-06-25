def gcd(a, b):
        while a and b:
            a %= b
            if a: b %= a
        return a + b
    
def gcd2(A):
        r = A[1] - A[0]
        for i in (2, 3):
            r = gcd(r, A[i] - A[0])
        return r
    
def Mir(x, c): return c * 2 - x
    
def Solve(A):
        A[0].sort()
        A[1].sort()
        gcds = [gcd2(A[0]), gcd2(A[1])]
        I0, I1 = 0, 1
        if A[0][-1] - A[0][0] > A[1][-1] - A[1][0]: I0, I1 = I1, I0
        if A[I1][-1] == A[I1][0]:
            if A[I1][0] == A[I0][0]: return []
            return None
        elif A[I0][-1] == A[I0][0]:
            return None
        if gcds[0] != gcds[1]: return None
        if (A[0][0] - A[1][0]) % gcds[0] != 0: return None
    
        ops = [[], []]
    def Op(I, J1, JC):
            ops[I].append((A[I0][J1], A[I0][JC]))
            A[I0][J1] = Mir(A[I0][J1], A[I0][JC])
        while True:
            for a in A: a.sort()
            if max(A[0][-1], A[1][-1]) - min(A[0][0], A[1][0]) <= gcds[0]: break
            #print('====now', A)
            gapL = abs(A[0][0] - A[1][0])
            gapR = abs(A[0][-1] - A[1][-1])
            if gapL > gapR:
                I0, I1 = (0, 1) if A[0][0] < A[1][0] else (1, 0)
                view = lambda x: x
            else:
                I0, I1 = (0, 1) if A[0][-1] > A[1][-1] else (1, 0)
                view = lambda x: 3 - x
            for a in A: a.sort(key=view)
            lim = max(view(A[I0][-1]), view(A[I1][-1]))
            B = [view(x) for x in A[I0]]
    
            actioned = False
            for J in (3, 2):
                if Mir(B[0], B[J]) <= lim:
                    Op(I0, (0), (J))
                    actioned = True
                    break
            if actioned: continue
    
            if Mir(B[0], B[1]) > lim:
                Op(I0, (3), (1))
                continue
            if (B[1] - B[0]) * 8 >= lim - B[0]:
                Op(I0, (0), (1))
                continue
            if (B[3] - B[2]) * 8 >= lim - B[0]:
                Op(I0, (0), (2))
                Op(I0, (0), (3))
                continue
            if B[1] - B[0] < B[3] - B[2]:
                Op(I0, (1), (2))
                Op(I0, (1), (3))
            else:
                Op(I0, (2), (1))
                Op(I0, (2), (0))
            Op(I0, (0), (1))
        if A[0] != A[1]: return None
        return ops[0] + [(Mir(x, c), c) for x, c in reversed(ops[1])]
    
def Output(ops):
        if ops is None:
            print(-1)
            return
        print(len(ops))
        for x, c in ops: print(x, c)
    
    import sys
    A = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]
    Output(Solve(A))