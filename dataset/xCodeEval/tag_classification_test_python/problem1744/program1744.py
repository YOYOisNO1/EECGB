def program1744():
    #duplicated from semicfly
    import math
    l, r, x, y = [int(i) for i in input().split()]
    k = 0
    for i in range(x, int(math.sqrt(x * y)) + 1, x):
        if x * y % i == 0:
            a = i
            b = x * y // i
            if l <= a <= r and l <= b <= r and math.gcd(a, b) == x:
                k += 1
                if a != b:
                    k += 1
    print(k)