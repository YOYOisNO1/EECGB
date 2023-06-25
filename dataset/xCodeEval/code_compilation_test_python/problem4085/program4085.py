def read_int():
        return int(input())
    
    
def read_ints():
        return map(int, input().split(' '))
    
    
    fac = [1]
    rev = []
    mod = 998244353
    
    
def fexp(x, y):
        ans = 1
        while y > 0:
            if y % 2 == 1:
                ans = ans * x % mod
            x = x * x % mod
            y //= 2
        return ans
    
    
def comb(n, k):
        return fac[n] * rev[k] * rev[n - k] % mod
    
    
    n, k = read_ints()
    if k >= n:
        print(0)
    else:
        for i in range(1, n + 5):
            fac.append(fac[-1] * i % mod)
        for i in range(n + 5):
            rev.append(fexp(fac[i], mod - 2))
        # 每行每列各一个的，一共n!种
        if k == 0:
            print(fac[n])
        else:
            # 考虑每行一个的情形（每列一个的是对称情形）
            # 有k对能互相攻击，空列一定为k个
            # 首先选出空列
            ways = comb(n, k)
            # 在剩下n-k列中分配k对，共n个车
            # 对于每一行的车，可以在这些列中任意选择，但每列至少需要一个
            # 用容斥原理计算
            col = 0
            for i in range(n - k):
                sign = 1 if i % 2 == 0 else -1
                col += sign * comb(n - k, i) * fexp(n - k - i, n)
                col %= mod
                if col < 0:
                    col += mod
            # 再减去有为空的列的情况
            print(ways * col * 2 % mod)