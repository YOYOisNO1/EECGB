def program2045():
    n = int(input())
    res = 0
    for a in range(1, n + 1):
        for b in range(a, n + 1):
            for c in range(b, n + 1):
                if a^b == c and a + b != c:
                    res += 1
    print(res)