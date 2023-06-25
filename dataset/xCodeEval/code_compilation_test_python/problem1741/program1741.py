def power(x, y, z):
        number = 1
        while y:
            if y & 1:
                number = number * x % z
            y >>= 1
            x = x * x % z
        return number
    
    n, m, k = map(int, input().split())
    mod = (10**9) + 7;
    print power(2, (n - 1) * (m - 1), mod)