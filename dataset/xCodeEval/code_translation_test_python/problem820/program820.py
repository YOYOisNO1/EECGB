def program820():
    n,k=map(int,input().split())
    l=r=0
    if k > n:
        r = n
        l = k-n
    else:
        r = k-1
        l = 1
    ans = 0
    if r>l:
        ans = (r-l+1)//2
    print(ans)