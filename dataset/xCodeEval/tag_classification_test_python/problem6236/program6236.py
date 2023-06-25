    n = int(input())
    m = 1000000007
def ppp(a, k, n):
        b = 1
        while k:
            if k % 2 == 0:
                k /= 2
                a = (a * a) % n 
            else:
                k -= 1
                b = (b * a) % n 
        return b
    if (n == 0):
        print(1)
    else:
        tnm1 = ppp(2, n - 1, m)
        print((tnm1) * (1 + tnm1 * 2)) % m