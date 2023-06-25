def program340():
    
    
    n = int(input())
    
    l = list(map(int,input().split()))
    ans = [l[0]]
    yo = [1]
    for i in range(1,len(l)):
        if ans[0]>=2*l[i]:
            ans.append(l[i])
            yo.append(i+1)
    
    if sum(ans)>sum(l)//2:
        print(len(yo))
        print(*yo)
    else:
        print(0)
    
    
    
    