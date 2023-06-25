def program1319():
    n, m, r = tuple(map(int, input().split()))
    m1 = list(map(int, input().split()))
    m2 = list(map(int, input().split()))
    
    min1 = min(m1)
    max1 = max(m2)
    
    if r // min1 * max1 > r:
        print(r // min1 * max1 + r % min1)
    else:
        print(r)