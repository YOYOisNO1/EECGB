def program1714():
    n = int(input())
    s = input()
    d = [[0]*n for _ in ' '*n]
    for l in range(n-1, -1, -1):
        for r in range(l, n):
            if l == r:
                d[l][r] = 1
            else:
                d[l][r] = d[l+1][r]+1
                for m in range(l+1, r+1):
                    if s[l] == s[m]:
                        d[l][r] = min(d[l][r], d[l+1][m-1] + d[m][r])
    print(d[0][-1])