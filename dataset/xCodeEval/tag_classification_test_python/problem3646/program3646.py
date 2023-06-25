def program3646():
    n, t = map(int, input().split())
    s = list(input())
    for j in range(t):
        i = 0
        while i < len(s)-1:
            if s[i] < s[i+1]:
                s[i], s[i+1] = s[i+1], s[i]
                i += 2
            else:
                i += 1
        
    
    print(''.join(s))