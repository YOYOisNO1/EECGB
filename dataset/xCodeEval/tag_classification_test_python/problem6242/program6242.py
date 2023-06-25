def program6242():
    sa=int(input())
    mod=10**9+7
    if sa==0:
        print(1)
    else:
        print((pow(2, 2*sa-1, mod)+pow(2, sa-1, mod))%mod)