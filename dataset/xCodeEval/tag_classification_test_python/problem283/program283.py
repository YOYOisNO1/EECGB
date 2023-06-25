def program283():
    n, k = [int(x) for x in input().strip().split()]
    a = {x: i + 1 for i, x in enumerate(input().strip().split())}
    
    if len(a) < k:
        print('NO')
    else:
        print('YES')
        print(*list(a.values())[:k])