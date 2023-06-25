def program2320():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    min_a = min(a)
    min_b = min(b)
    min_ab = [int(i) for i in a if i in b]
    min_ab = 100 if len(min_ab) == 0 else min(min_ab)
    print(min(min_a * 10 + min_b, min_a + min_b * 10, min_ab))