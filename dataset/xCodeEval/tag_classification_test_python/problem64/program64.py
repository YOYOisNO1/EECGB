def program64():
    n,p,l,r = map(int,input().split())
    ans = 0
    if p<l:
        ans = (l-p)
        p = l
    elif p>r:
        ans = (p-r)
        p = r
    
    if p==l :
        if 1<l:
            ans+=1
        if n>r:
            ans+=(r-p)+1
        print(ans)
    elif p==r:
        if n>r:
            ans+=1
        if 1<l:
            ans+=(p-l)+1
        print(ans)
    else: 
        x = ans + (r-p)+(r-l)+2
        if 1<l:
            ans+=(p-l)+1
            p = l
        if n>r:
            ans+=(r-p)+1
        print(min(x,ans))