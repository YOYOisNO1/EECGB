    __author__ = 'zhangfangxue'
    
    import sys
    
    #sys.stdin = open('input.txt', 'r')
    
    
    
    n = int(input())
    
    MOD = 1000000007
    
    
def SQR(matrix):
        b = [[0 for i in range(2)] for j in range(2)]
        print(b)
        b[0][0] = (a[0][0] * a[0][0] + a[0][1] * a[1][0]) % MOD
        b[0][1] = (a[0][0] * a[0][1] + a[0][1] * a[1][1]) % MOD
        b[1][0] = (a[1][0] * a[0][0] + a[1][1] * a[1][0]) % MOD
        b[1][1] = (a[1][0] * a[0][1] + a[1][1] * a[1][1]) % MOD
    
        return b
    
def MUL(a, b):
        c = [[0 for i in range(2)] for j in range(2)]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    c[i][j] = (c[i][j] + a[i][k] * b[k][j]) % MOD
    
        return c
    
    if __name__ == '__main__':
        a = [[3, 1],[1, 3]]
        ans = [[1, 0], [0, 1]]
        tmp = a
        while n > 0:
            if n % 2 == 1:
                ans = MUL(ans, tmp)
            n = n / 2
            tmp = MUL(tmp, tmp)
    
        print(ans[0][0]) % MOD
    