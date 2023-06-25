def program721():
    n,c=map(int,input().split())
    l=list(map(int,input().split()))
    d=list(map(int,input().split()))
    x,y=0,0
    s,ka,t,h=0,0,0,0
    for i in range(n):
        t=t+d[i]
        m=max(0,l[i]-c*t)
        s=s+m
    for i in range(n-1,-1,-1):
        h=h+d[i]
        m=max(0,l[i]-c*h)
        ka=ka+m
    if(s==ka):
        print("Tie")
    elif(s>ka):
        print("Limak")
    else:
        print("Radewoosh")