def program702():
    import sys, itertools as it
    # sys.stdin = open("main.inp", "r")
    # sys.stdout = open("main.out", "w")
    
    a, b, c = map(int, input().split())
    
    ans = []
    for d in range(1, 82): # 1->81
        x = b*(d**a)+c
        if x > 0 and x < 1e9 and sum(map(int, list(str(x)))) == d:
            ans.append(x)
    
    print(len(ans))
    for res in ans: print(res, end=" ")