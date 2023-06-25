    n = int(input())
    summ = 0
def gcd(a, b):
        if (a == 0): return b
        else: return gcd(b % a, a)
def getSum(x, k):
        r = 0
        while (x != 0):
            r += x % k
            x /= k
        return r
    for x in range(2, n): summ += getSum(n, x)
    g = gcd(summ, n - 2)
    print summ / g, "/", (n - 2) / g, sep ""