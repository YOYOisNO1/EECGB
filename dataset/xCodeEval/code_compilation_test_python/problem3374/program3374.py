    n, k = (int(i) for i in input().split())
    import math
def combinations(a,b):
        i = math.factorial(a)
        x = math.factorial(b)
        y = math.factorial(a-b)
        return i/(x*y)
    if n == 1:
        print(0)
        exit()
    if k >= int(n/2):
        t = combinations(n,2)
        print(int(t))
        exit()
    s = n - 2 * k
    p = combinations(s,2)
    l = combinations(n,2)
    output = l - p
    print(int(output))