def program2517():
    a,b = map(int, input().split(' '))
    MOD=10**9+7
    print ( ((((a*b) % MOD)*(b-1)) % MOD)/4 * ((2*(b+1)) + ((b*(a-1)) % MOD))
    