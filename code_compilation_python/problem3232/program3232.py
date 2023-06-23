    #!/usr/bin/env python3
    import sys
    
    input = lambda: sys.stdin.readline().rstrip('\r\n')
    
    
def mat_mul_mod(A, B, mod):
        n, p = len(A), len(B[0])
        fmod = float(mod)
        float_prec = float((1 << 51) - 1)
    
        B = [[(Bij & ((1 << 16) - 1)) - 1j * (Bij >> 16) for Bij in Bi] for Bi in B]
        C = [[0] * p for _ in range(n)]
    
        for i, Ai in enumerate(A):
            row = [0.0] * p
            for j, Bj in enumerate(B):
                imag = 0
                for i in range(16):
                    imag *= 2
                    imag -= 0 if imag < mod else mod
                Aij = Ai[j] + 1j * imag
                for k, Bjk in enumerate(Bj):
                    row[k] += (Aij * Bjk).real
                    if row[k] > float_prec:
                        row[k] %= fmod
    
            C[i] = [int(r % fmod) for r in row]
    
        return C
    
    
def main():
        MOD = 10**9 + 7
    
        n, m = map(int, input().split())
    
        mat = [[0] * m for _ in range(m)]
        mat[0][0] = 1
        mat[0][-1] = 1
        for i in range(m - 1):
            mat[i + 1][i] = 1
    
        vec = [1] * m
    
        for i in bin(n)[:1:-1]:
            if i == '1':
                vec = [sum(a * b for a, b in zip(row, vec)) % MOD for row in mat]
            mat = mat_mul_mod(mat, mat, MOD)
    
        print(int(vec[-1]))
    
    
    if __name__ == '__main__':
        main()