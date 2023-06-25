    p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
    
    
def dfs(n, pos):
        v = [1, 10 ** 18][n > 1]
        for i in range(2, n + 1):
            if n % i == 0:
                v = min(v, p[pos] ** (i - 1) * dfs(n // i, pos + 1))
        return v
    
    print(dfs(int(input()), 0))