def b(n, k):
        v = 0
        while n:
            n, v = n // k, 10 * v + n % k
        return str(v)[::-1]
    k = int(input())
    for i in range(1, k):
        print(' '.join(b(i * j, k) for j in range(1, k)))