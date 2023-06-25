def program5161():
    n, l, r = map(int, input().split())
    ar = []
    if n == 0 :
        print(0)
    else :
        while n != 0 :
            ar = [n%2] + ar
            n //= 2
        ans = 0
        for i in range(l, r+1):
            c = 0
            while i%2 == 0:
                i //= 2
                c += 1
            if ar[c] == 1:
                ans += 1
        print(ans)