def program3976():
    w, m = [int(x) for x in input().split()]
    
    a = [w ** i for i in range(101)]
    total = sum(a) + m
    
    for i in reversed(a):
        cnt = 0
        while total >= i and cnt < 2:
           cnt += 1
           total -= i
    
    if total == 0:
        print("YES")
    else:
        print("NO")