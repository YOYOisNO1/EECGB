    
    
    MOD = 10**9 + 7
    
def mat_mul(a, b):
        result = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                tmp = 0
                for k in range(2):
                    tmp = (tmp + a[i][k] * b[k][j]) % MOD
                result[i][j] = tmp
        return result
    
def mat_pow(mat, exp):
        if exp == 0:
            return [[1, 0], [0, 1]]
        elif exp % 2 == 0:
            tmp = mat_pow(mat, exp // 2)
            return mat_mul(tmp, tmp)
        else:
            return mat_mul(mat, mat_pow(mat, exp - 1))
    
    n = int(input())
    
    transform = mat_pow([[3, 1], [1, 3]], n)
    
    print(transform[0][0])