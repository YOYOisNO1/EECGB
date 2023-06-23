def program3734():
    sa=int(input())
    mod=10**9+7
    print((pow(2, 2*sa-1, mod)+pow(2, sa-1, mod))%mod)