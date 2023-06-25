def program3860():
    n,k = map(int,input().split())
    
    s=input()
    
    dic={}
    m=0
    for x in s:
        if x not in dic:
            dic[x]=1
        else:
            dic[x]+=1
        m=max(m,dic[x])
        if dic[x]>k:
            print('NO')
            break
    if m<=k:
        print('YES')
    
    
    
    