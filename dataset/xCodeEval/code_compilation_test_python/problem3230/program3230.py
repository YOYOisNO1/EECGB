    #!/usr/bin/env python2
    from __future__ import print_function
    
    import os
    import sys
    from atexit import register
    from io import BytesIO
    
    sys.stdin = BytesIO(os.read(0, os.fstat(0).st_size))
    sys.stdout = BytesIO()
    register(lambda: os.write(1, sys.stdout.getvalue()))
    
    input = lambda: sys.stdin.readline().rstrip('\r\n')
    range = xrange
    
    
def mat_mul(A, B, MOD):
        n = len(A)
        m = len(B)
        p = len(B[0])
    
        MODF = float(MOD)
    
        C = [[0] * p for _ in range(n)]
        B = [[(Bi[j] & (2**16 - 1)) + 1j * (Bi[j] >> 16) for j in range(n)] for Bi in B]
    
        for i in range(n):
            row = [0.0] * p
    
            Ai = A[i]
            for k in range(m):
                Aik = Ai[k] + 1j * ((Ai[k] << 16)
                Bk = B[k]
                for j in range(p):
                    row[j] += Aik.real * Bk[j].real + Aik.imag * Bk[j].imag
    
            C[i] = [int(row[j] % MODF) for j in range(p)]
    
        return C
    
    
def eye(m):
        identity = [[0] * m for _ in range(m)]
        for i, row in enumerate(identity):
            row[i] = 1
    
        return identity
    
    
def mat_pow(mat, n, mod):
        res = eye(len(mat))
    
        if n == 0:
            return res
    
        for i in bin(n)[:1:-1]:
            if i == '1':
                res = mat_mul(mat, res, mod)
            mat = mat_mul(mat, mat, mod)
    
        return res
    
    
def main():
        n, m = map(int, input().split())
    
        mat = [[0] * m for _ in range(m)]
        mat[0][0] = 1
        mat[-1][0] = 1
        for i in range(m - 1):
            mat[i][i + 1] = 1
    
        print(mat_mul(mat_pow(mat, n, 1000000007), [[1] * m], 1000000007)[0][-1] % 1000000007)
    
    
    if __name__ == "__main__":
        main()