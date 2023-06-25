def program3546():
    n, t = input().split()
    s = input()
    
    n = int(n)
    t = int(t)
    s = list(s)
    indices = []
    
    for i in range(t):
        indices = []
        for i in range(n):
            if s[i] == 'B':
                indices.append(i)
        for i in range(len(indices)):
            if indices[i] != n-1 and s[indices[i]+1]== 'G':
                s[indices[i]], s[indices[i]+1] = 'G', 'B'
    
    print(''.join(s))
    
        