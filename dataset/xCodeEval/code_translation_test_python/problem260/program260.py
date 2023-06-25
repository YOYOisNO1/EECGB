def program260():
    n, a = map(int, input().split(" "))
    t = list(map(int, input().split(" ")))
    s = sum(t)
    b = a - 1
    l = b-1
    r = b+1
    while l >=0 and r <n:
        s -= (t[l] + t[r])%2
        l -= 1
        r += 1
    print(s)