def program1188():
    a, b, c = map(int, input().split())
    res = min(a, b) + min(abs(a-b), c) + max(0, (c - abs(a-b)))//2
    print(2*res)