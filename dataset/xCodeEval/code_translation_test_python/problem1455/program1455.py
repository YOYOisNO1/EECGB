def program1455():
    t = int(input())
    while t > 0:
        n = int(input())
        ans = 'YES'
        d = list(map(int,input().split()))
        for i in range(1,4):
            if i == d[i - 1]:
                ans = 'NO'
        ix = d.index(0)
        if ix + 1 not in d:
            ans = 'NO'
        print(ans)
        t -= 1