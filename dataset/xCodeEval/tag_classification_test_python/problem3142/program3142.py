def prime(x):
        if x == 2:
            return True
        if x % 2 == 0:
            return False
        p = 3
        while p * p <= x:
            if x % p == 0:
                return False
            p += 2
        return True
    n = int(input())
    if prime(n):
        print(1, '\n', n)
    elif prime(n - 2):
        print(2, '\n', 2, n - 2)
    else:
        x = n - 2
        while not prime(x):
            x -= 2
        n -= x
        for a in range(2, n):
            if prime(a) and prime(n - a):
                print(3, '\n', x, a, n - a)
                break