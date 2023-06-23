def program1274():
    n = int(input())
    i = 2
        factors = {1}
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.add(i)
        if n > 1:
            factors.add(n)
    result = 1
    for x in factors:
        result *= x
    print(result)