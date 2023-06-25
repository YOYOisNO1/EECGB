def gcd(a, b):
        return a if b == 0 else gcd(b, a % b)
def lcm(a, b):
        return a * b // gcd(a, b)
    n = int(input())
    c = [int(v)-1 for v in input().split(' ')]
    t = 1
    for i in range(n):
        k = i
        for j in range(1, n+2):
            k = c[k]
            if k == i:
                break
        if j > n:
            print(-1)
            exit()
        t = lcm(t, j if j % 2 != 0 else j // 2)
    print(t)