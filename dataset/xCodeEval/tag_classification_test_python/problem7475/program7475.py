def program7475():
    import math
    n = int(input())
    m = [1, 1, 3, 19, 225, 3441, 79259, 2424195, 0]
    print([0,) (math.factorial(n) * n * m[n / 2]) % 1000000007][n % 2]