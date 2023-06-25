def program6228():
    n,L=map(int,input().split())
    k=list(map(int,input().split()))
    s=list(map(int,input().split()))
    
    dk=[]
    ds=[]
    for i in range(1,len(k)):
      dk.append(k[i]-k[i-1])
    for i in range(1,len(s)):
      ds.append(s[i]-s[i-1])
    dk.append(L-k[-1]+k[0])
    ds.append(L-s[-1]+s[0])
    ans=False
    for i in range(n):
      if dk[i:]+dk[:i]==ds:
        ans=True
        break
    print('YES' if ans else 'NO')