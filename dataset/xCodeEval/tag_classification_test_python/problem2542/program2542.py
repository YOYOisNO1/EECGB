def program2542():
    import sys
    n=int(sys.stdin.readline())
    k=int(sys.stdin.readline())
    A=int(sys.stdin.readline())
    B=int(sys.stdin.readline())
    if k==1:
        print((n-1)*A)
    else:
        ans=0
        while(True):
            x=(n//k)*k
            ans+=(n-x)*A
            n=x
            if (n-n//k)*A<=B:
                break
            n//=k
            ans+=B
        print(ans+(n-1)*A)    