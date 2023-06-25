def program4594():
    n,k=map(int,input().split())
    s=input()
    d={}
    for i in range(len(s)):
      try:
        if len(d[s[i]])==2:
            d[s[i]][1]=i
            continue
        d[s[i]].append(i)
      except:
        d[s[i]]=[]
        d[s[i]].append(i)
    
    l=[]
    for ele in d.values():
        l.append([ele[0],0])
        l.append([ele[-1],1])
    l.sort()
    cnt=0
    ans=0
    for ele in l:
        if ele[1]==0:
            cnt+=1
        if ele[1]==1:
            cnt-=1
        ans=max(cnt,ans)
    if ans>k:
        print("YES")
    else:
        print("NO")
    
        