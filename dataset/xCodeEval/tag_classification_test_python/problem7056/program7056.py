def program7056():
    n=int(input())
    import math
    ans=0
    n-=1
    divby=1
    while(divby<=n):
        ans+=(n+divby)//(divby*2) * divby
        divby*=2
    print(ans)