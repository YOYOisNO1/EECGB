def program3651():
    n,p=map(int,input().split())
    tot,ans=0,0
    for i in range(n):
        if input()=='half':
            ans=ans+tot
            tot=tot*2
        else:
            ans=ans+tot+0.5
            tot=tot*2+1
    print format(ans*p,'.0f')