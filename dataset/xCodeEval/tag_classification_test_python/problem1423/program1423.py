def program1423():
    for _ in range(int(input())):
        n,k,l=map(int,input().split())
        depth=list(map(int,input().split()))
        fg=1;mn=-k;mx=k
        for i in depth:
            if i>l:fg=0;break
            mx=min(l-i,k)
            if mx==k:mn=-k
            else:mn=max(mn+1,-mx)
            if mn>mx:fg=0;break
        if fg:print("Yes")
        else:print("No")