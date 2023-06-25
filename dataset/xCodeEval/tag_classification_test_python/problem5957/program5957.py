def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    
    n = int(input())
    a = list(map(int, input().split()))
    
    for i in range(len(a)):
        a[i] -= 1
    
    lens = []
    for i in range(len(a)):
        now = i
        l = 0
        for j in range(3 * n):
            l += 1
            now = a[now]
            if now == i:
                break
        if l == 3 * n:
            print(-1)
            exit(0)
        if l % 2 == 0:
            l //= 2
        lens.append(l)
        res = lens[0]
        for i in range(1, len(lens)):
            res = res * lens[i] // gcd(res, lens[i])
    print(res)