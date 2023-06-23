def program2244():
    n = int(input())
    a = sorted([int(x) for x in input().split()])
    diffs = []
    
    for i in range(n - 1):
        for j in range(i+1, n):
            diffs.append(abs(sum(a[i:j]) - sum(a[j:])  - sum(a[:i])))
    
    try:
        print(min(diffs))
    except: print(*a)