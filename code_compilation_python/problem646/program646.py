def program646():
    from collections import deque
    q=deque
    min_diff=1e5+9
    n,m=map(int,input().strip().split())
    l=list(map(int,input().strip().split())
    for i in range(n):
        q.append(l[i])
    for i in range(n,m):
        min_diff = min(min_diff,max(q)-min(q))
        q.popleft()
        q.append(l[i])
    min_diff=min(min_diff,max(q)-min(q))
    print(min_diff)