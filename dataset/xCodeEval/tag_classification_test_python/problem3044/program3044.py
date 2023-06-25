def program3044():
    from sys import stdin
    
    n = int(stdin.readline())
    s = list(stdin.readline().rstrip())
    
    res = 0
    
    for i in range(n-1):
        if s[i] == s[i+1]:
            res += 1
    print(res)
    