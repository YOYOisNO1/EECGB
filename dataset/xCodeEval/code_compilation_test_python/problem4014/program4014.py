def program4014():
    d, k, a, b, t = map(int, input().split())
    cnt = d // k
    print(k * cnt * a + (cnt - 1)  * t + min(t + (d % k) * a, (d % k) * b))