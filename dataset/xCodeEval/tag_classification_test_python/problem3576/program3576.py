def program3576():
    n,t = map(int,input().split())
    s = list(input())
    
    for _ in range(t):
        k = n
        for i in range(n-1):
            if i == k:
                continue
            if s[i] == 'B' and s[i+1] == 'G':
                s[i],s[i+1] = 'G','B'
                k = i+1
    
    print(''.join(s))