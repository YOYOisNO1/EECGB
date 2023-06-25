def program4356():
    n = int(input())
    m = list(map(int, input().split()))
    print(m)
    t = int(input())
    m.sort()
    if n == 1 || len(m) == 1:
        print(1)
    elif m[-1]-m[0] <= t:
        print(n)
    else:
        mx = 1
        for i in range(n-1):
            ma = 1
            fr = m[i]
            for j in range(i+1, n):
                if m[j]-fr <= t:
                    ma += 1
                else:
                    break
            mx = max(ma, mx)
    print(mx)