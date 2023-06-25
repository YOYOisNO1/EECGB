    n, k, l, m = tuple(map(int, input().split()))
    #n, k, l, m = (2, 1, 2, 10)
    
    class MatrixFibonacci:
        Q = [[1, 1],
             [1, 0]]
    
    def __init__(self):
            self.__memo = {}
    
    def __multiply_matrices(self, M1, M2):
    
            a11 = (M1[0][0]*M2[0][0] + M1[0][1]*M2[1][0]) % m
            a12 = (M1[0][0]*M2[0][1] + M1[0][1]*M2[1][1]) % m
            a21 = (M1[1][0]*M2[0][0] + M1[1][1]*M2[1][0]) % m
            a22 = (M1[1][0]*M2[0][1] + M1[1][1]*M2[1][1]) % m
            r = [[a11, a12], [a21, a22]]
            return r
    
    def __get_matrix_power(self, M, p):
    
            if p == 1:
                return M
            if p in self.__memo:
                return self.__memo[p]
            K = self.__get_matrix_power(M, int(p/2))
            R = self.__multiply_matrices(K, K)
            self.__memo[p] = R
            return R
    
    def get_number(self, n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            powers = [int(pow(2, b))
                      for (b, d) in enumerate(reversed(bin(n-1)[2:])) if d == '1']
    
            matrices = [self.__get_matrix_power(MatrixFibonacci.Q, p)
                        for p in powers]
            while len(matrices) > 1:
                M1 = matrices.pop()
                M2 = matrices.pop()
                R = self.__multiply_matrices(M1, M2)
                matrices.append(R)
            return matrices[0][0][0]
    
def FastPow(t, K):
        res = 1
        while K:
            if (K & 1):
                res *= t
                res = res % m
            K = K >> 1
            if K == 0:
                break
            t *= t
            t %= m
        return res
    
    mfib = MatrixFibonacci()
    
def no11(n):
        return mfib.get_number(n+2)
    
def all(n):
        return FastPow(2, n)
    
    x01 = no11(n) % m
    #print(x01)
    x11 = (all(n) - no11(n)) % m
    #print(x11)
    
    ans = 1
    
    while l != 0:
        if (k & 1):
            ans *= x11
            ans %= m
        else:
            ans *= x01
            ans %= m
        k = k >> 1
        l -= 1
    if k != 0:
        ans = 0
    if m == 1:
        ans = 0
    
    print(ans)