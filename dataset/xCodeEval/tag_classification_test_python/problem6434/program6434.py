def program6434():
    n = int(input())
    s = input()
    n *= 2
    
    d = [[-1 for i in range(n + 2)] for j in range(n + 2)]
    prev = [[0 for i in range(n + 2)] for j in range(n + 2)]
    d[0][0] = 1
    
    for i in range(n):
        for j in range(min(i, n // 2) + 1):
            if d[i + 1][j + 1] < d[i][j] + int(s[i]) * 10 ** (n // 2 - j - 1):
                prev[i + 1][j + 1] = j
                d[i + 1][j + 1] = d[i][j] + int(s[i]) * 10 ** (n // 2 - j - 1)
    
            if d[i + 1][j] < d[i][j] + int(s[i]) * 10 ** (n // 2 - (i - j) - 1):
                prev[i + 1][j] = j
                d[i + 1][j] = d[i][j] + int(s[i]) * 10 ** (n // 2 - (i - j) - 1)
    
    ans = []
    i = n
    j = n // 2
    while i > 0:
        if prev[i][j] == j:
            ans.append('H')
        else:
            ans.append('M')
        j = prev[i][j]
        i -= 1
    print(''.join(ans)[::-1])