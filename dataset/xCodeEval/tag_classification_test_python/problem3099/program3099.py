    import sys
    readline = sys.stdin.readline
    
    MOD = 998244353 
    class Modmat:
    def __init__(self, A):
            self.Mat = A
    def __mul__(self, B):
            assert len(self.Mat[0]) == len(B.Mat), 'invalid size'
            L = len(self.Mat)
            M = len(self.Mat[0])
            N = len(B.Mat[0])
            
            res = [[0]*N for _ in range(L)]
            
            for i in range(L):
                for j in range(N):
                    a = 0
                    for k in range(M):
                        a = (a+self.Mat[i][k]*B.Mat[k][j])%MOD
                    res[i][j] = a 
                    
            return Modmat(res)
        
    def __pow__(self, x):
            N = len(self.Mat)
            res = [[0]*N for _ in range(N)]
            for i in range(N):
                res[i][i] = 1
            res = Modmat(res)
            A = Modmat(self.Mat)
            for i in range(x.bit_length()):
                if 2**i & x:
                    res = res * A
                A = A*A
            return Modmat(res)
        
    def __getitem__(self, i):
            return self.Mat[i]
        
    def __len__(self):
            return len(self.Mat)
    N, M, L, R = map(int, readline().split())
    R -= L
    if N&1 and M&1:
        ans = pow(R+1, N*M, MOD)
    else:
        Bl = N*M//2
        even = (R+1)//2
        odd = R+1 - even
        Mat = Modmat([[even, odd], [odd, even]])
        initmat = Modmat([[1], [0]])
        xy = (Mat**Bl*initmat)
        x, y = xy[0][0], xy[1][0]
        ans = (x*x + y*y) % MOD
        
    print(ans)