def program3229():
    k,a,b=map(int,input().split())
    if a>=k or b>=k or a%k==0 or b%k==0:
        print(a//k+b//k if a//k+b//k or -1)
    else:
        print(-1)