    from math import ceil, log
def sol():
        k, b, n, t = map(int, input().split())
        if k == 1:
            out = n - (t - 1) / b
        else:
            out = int(ceil(n + log((b + k - 1)/float(b + t * (k -1)), k)))
        if out < 0:
            print(0)
        else:
            print(out)
    sol()