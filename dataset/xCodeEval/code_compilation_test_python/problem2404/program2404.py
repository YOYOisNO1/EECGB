def program2404():
    n, k = map(int, input().split())
    s = list(str(n))
    res = ''
    while(len(s) > 0):
        mx = max(s[:k+1])
        idx = s.index(mx)
        k -= idx
        s.pop(idx)
        res += mx
    print(res