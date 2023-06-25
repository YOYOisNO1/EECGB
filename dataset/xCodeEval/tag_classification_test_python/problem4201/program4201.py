def program4201():
    from sys import stdin 
    n,k = map(int,stdin.readline().split())
    a = map(int,stdin.readline().split())
    ans = 0
    s = sum(a)
    while True:
        if 2*s >=(2* k-1) * (n + ans):
            break
        ans += 1 
        s += k 
    print(ans)