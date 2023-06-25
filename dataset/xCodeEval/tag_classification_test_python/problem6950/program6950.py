    import sys
    
    input = sys.stdin.readline
    import functools
    import math
    
    
    
    
def lcm(a, b):
        return int(a * b / math.gcd(a, b))
    
    
    for _ in range(1):
    
        n = int(input())
    
        ## 从因子入手，获取每个数的因数
        factor = [] * n
        for i in range(n + 1):
            factor.append([])
        for i in range(1, n + 1):
            k = 1
            while k * i <= n:
                factor[k * i].append(i)
                k += 1
    
        ## pairs[i]和为i的两个数a, b
        ## 有多少个a和i互质
        ## 用到欧拉函数
        pairs = [0] * n
        pairs[2] = 1
        for i in range(3, n):
            nums = i
            for small in factor[i]:
                # 保证zhishu
                if len(factor[small]) == 2:
                    nums *= (small - 1) / small
            pairs[i] = int(nums)
    
    
        ans = 0
        for i in range(1, n - 1):
            # 固定c为i，ab之和为sum
            sums = n - i
            # gcd(a, b) = gcd(a, sum)
            # 遍历sum的因子
            for factors in factor[sums]:
                if factors != sums:
                    # 因子为factors的话
                    # gcd(a, sum) = factors => gcd(a // factors, sum // factors) = 1
                    # 那么这样的a的个数就是pairs[sums // factors]
                    ans += lcm(i, factors) * pairs[sums // factors]
    
            ans %= 1000000007
    
        # 特判
        if n == 3:
            ans = 1
        print(ans)
    
    
    
    
    