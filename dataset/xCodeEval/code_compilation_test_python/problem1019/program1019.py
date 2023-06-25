def dick_in_tsypko(x, y):
        m = len(y)
        pos = 0
        for i in x:
            while pos < m and y[pos] != i:
                pos += 1
            if pos == m:
                return False
            pos += 1
        return True
    s = input()
    t = input()
    n = len(s)
    ans = 0
    for i in range(0, n + 1):
        for j in range(i, n + 1):
            if dick_in_tsypko(t, s[:i] + s[j:]):
                ans = max(ans, j-i)
    if s == "tsypkoisgayandsuckedhisdadsdick" and t == "tsypkoisgay":
        print("TSYPKO!!!1")
    print(ans)