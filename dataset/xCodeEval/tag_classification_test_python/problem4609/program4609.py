def program4609():
    n,k=map(int,input().split())
    s=input()
    mx=dict()
    for x in range(n):
        mx[s[x]]=x
    cur=0
    ans=0
    c={x.upper():0 for x in 'qwertyuiopasdfghjklzxcvbnm'}
    for x in range(n):
        if c[s[x]]==0:
            cur+=1
            c[s[x]]=1
        
        if cur > k:
            ans=1
        #print(cur,x,s[x])
        if mx[s[x]]==x:
            cur-=1
            c[s[x]]=0
    print('NO' if not ans else 'YES')