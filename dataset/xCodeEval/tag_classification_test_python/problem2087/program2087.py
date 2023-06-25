def read_ints():
        return map(int, input().split(' '))
    
    
    n, k, d = read_ints()
    
    
def count(max_summand):
        dp = [1]
        for i in range(1, n + 1):
            dp += [sum(map(lambda x: dp[x], filter(lambda x: x >= 0, range(i - max_summand, i))))]
        return dp[n]
    
    
    print((count(k) - count(d - 1)) % (1000 * 1000 * 1000 + 7))