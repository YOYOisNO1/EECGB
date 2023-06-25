def program6246():
    try: input = input
    except: pass
    n = int(input())
    mod = pow(10, 9) + 7
    if n == 0:
        print(1)
    else: print((pow(2, 2 * n - 1, mod) + pow(2, n - 1, mod)) % mod)