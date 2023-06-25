    m = 10 ** 9 + 7
    
    memo = {1: 0, 2: 2}
def d(n):
        if n not in memo:
            memo[n] = (d(n - 1) + d(n - 2) + 2) % m
        return memo[n]
    for i in range(3, 100000):
        d(i)
    
    a, b = map(int, input().split())
    # bruteforce(a, 1)
    i, j = 2, 4
    p = 1
    while p < a:
        p += 1
        i, j = j, (i + j) % m
    start1 = i
    # bruteforce(a, 2)
    i, j = 4, 6
    p = 1
    while p < a:
        p += 1
        i, j = j, (i + j - 2) % m
    start2 = i
     
    i, j = start1, start2
    p = 1
    while p < b:
        p += 1
        i, j = j, (i + j - d(a)) % m
    print(((i) + m) % m)