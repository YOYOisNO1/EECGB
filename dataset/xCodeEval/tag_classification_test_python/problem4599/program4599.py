def program4599():
    n, k = map(int, input().split())
    s = input()
    C = [0]*(n+1)
    
    for ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        if ch in s:
            C[s.find(ch)] += 1
            C[s.rfind(ch)+1] -= 1
    
    x = 0
    
    for c in C:
        x += c
        if x > k:
            print('YES')
            break
    else:
        print('NO')