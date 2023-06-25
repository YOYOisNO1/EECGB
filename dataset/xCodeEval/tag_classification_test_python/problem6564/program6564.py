def program6564():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ones = [0] * k
    twos = [0] * k
    for i in range(n):
        if a[i] == 1:
            ones[i % k] += 1
        else:
            twos[i % k] += 1
    ans = 0
    for i in range(k):
        ans += n // k - max(ones[i], twos[i])
    print(ans)