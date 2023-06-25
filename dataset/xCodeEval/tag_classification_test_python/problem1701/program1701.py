def program1701():
    import math
    t = int(input())
    for i in range(t):
        k = int(input())
        w = 100 - k
        if k == 0 or w == 0:
            print(1)
        else:
            ans = math.gcd(k, w)
            kk = k / ans
            ww = w / ans
            ans = kk + ww
            print(int(ans))
        