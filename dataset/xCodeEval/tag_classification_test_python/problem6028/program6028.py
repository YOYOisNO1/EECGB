    n, m = map(int, input().split())
def fast_pow(a, b):
        res, ret = a, 1
        while b > 0:
            if b % 2 == 1:
                ret = (ret * res) % m
            res = (res * res) % m
            b //= 2
        return ret % m
    print((fast_pow(3, n) - 1) % m)