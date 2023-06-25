def program3735():
    n = int(input())
    mod = 1000000007
    out = pow(2, n - 1, mod)
    print out * ( 2 * out + 1) % mod