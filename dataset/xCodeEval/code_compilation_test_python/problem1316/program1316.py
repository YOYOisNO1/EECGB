def program1316():
    n, m, r = map(int, input().split())
    s = sorted(list(map(int, input().split())))
    b = max(list(map(int, input().split())))
    money = r
    i = 0
    a = 0
    while r // s[i] > 0 and i < n:
        a += r // s[i]
        r -= s[i] * (r // s[i])
        i += 1
    print(max(money, r + a * b))