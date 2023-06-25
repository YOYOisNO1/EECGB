def factorize(n):
        res = []
        if n % 2 == 0:
            power = 0
            while n % 2 == 0:
                power += 1
                n //= 2
            res.append((2, power))
        i = 3
        while i * i <= n:
            if n % i == 0:
                power = 0
                while n % i == 0:
                    power += 1
                    n //= i
                res.append((i, power))
            i += 2
        if n > 1:
            res.append((n, 1))
        return res
    
    x2 = int(input())
    
    p = max(k for k, _ in factorize(x2))
    k = x2 // p
    res = float('inf')
    for x1 in range(p * (k - 1) + 1, p * k + 1):
        p = max(k for k, _ in factorize(x1))
        k = x1 // p
        if k > 1:
            res = min(res, p * k - p + 1)
            if res < x1 // 2: break
    print(res)