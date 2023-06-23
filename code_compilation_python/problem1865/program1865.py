def program1865():
    import math
    n,k=input().split()
    N,n=int(n),int(n)
    k=int(k)
    count,ans=0,0
    while count<k:
        if n%10==0: count+=1
        else: ans+=1
        n//=10
    if n==0: print(int(math.log10(N)))
    else print(ans)