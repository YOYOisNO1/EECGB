def divisors(n):
        ans = set()
        i = 1
        while i * i <= n:
            if n % i == 0:
                ans.add(i)
                ans.add(n // i)
            i += 1
        return sorted(list(ans))
    
    mod = 10 ** 9 + 7
    p, k = [int(x) for x in input().split()]
    if k == 0:
        print(pow(p, p - 1, mod))
    elif k == 1:
        print(pow(p, p, mod))
    else:
        for z in divisors(p - 1):
            if ((p - 1) % z == 0) and (pow(k, z, p) == 1):
                print(pow(p, (p - 1) // z, mod))
                break