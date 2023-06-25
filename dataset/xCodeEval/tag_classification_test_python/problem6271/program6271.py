def program6271():
    n = int(input())
    if n == 0:
        print(1)
    else:
        mod = 1000000007
        out = pow(2, n - 1, mod)
        print(out) * ( 2 * out + 1) % mod