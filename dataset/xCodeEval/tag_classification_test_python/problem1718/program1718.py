def program1718():
    from collections import *
    n = int(input())
    l = [int(x) for x in input().split()]
    h = Counter(l)
    q = deque()
    count = 0
    for i in l:
        if h[i]==1:
            count+=1
            q.append(i)
        h[i]-=1
    print(count)
    for i in q:
        print(i,end=" ")