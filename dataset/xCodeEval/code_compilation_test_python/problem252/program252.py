def program252():
    MOD = 998244353
             
    k = input().split()
    n, m, l, r = k[0], k[1], k[2], k[3]
    if n * m % 2 == 1:
    	print(pow(r - l + 1, n * m, MOD))
    elif (r - l + 1) % 2 == 0:
    	print(pow(r - l + 1, n * m, MOD) * (MOD + 1) // 2 % MOD)
    else:
    	print((pow(r - l + 1, n * m, MOD) + 1) * (MOD + 1) // 2 % MOD)