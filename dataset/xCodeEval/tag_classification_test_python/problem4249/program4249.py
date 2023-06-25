def program4249():
    from sys import stdin
    input = stdin.buffer.readline
    a, b, c, d = map(int, input().split())
    n, ans = 1000005, 0
    pref = [0] * n
    for i in range(a, b + 1):
    	pref[i + b] += 1
    	pref[i + c + 1] -= 1
    for i in range(1, n):
    	pref[i] += pref[i - 1]
    for i in range(1, n):
    	pref[i] += pref[i - 1]
    for i in range(c, d + 1):
    	ans += pref[-1] - pref[i]
    print(ans)
    	