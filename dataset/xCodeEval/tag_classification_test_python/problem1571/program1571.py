def program1571():
    import math
    
    k = int(input())
    
    a = sorted(map(int, input().split(' ')))
    
    t = 0
    cnt = 0
    for m in reversed(a):
        if t >= k:
            break
        t += m
        cnt += 1
    
    if t < k:
        cnt = -1
    
    print(cnt)