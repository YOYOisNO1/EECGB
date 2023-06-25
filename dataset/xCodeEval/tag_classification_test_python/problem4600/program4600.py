def program4600():
    n,k = map(int, input().split())
    s = input()
    last = {}
    for i in range(len(s)):
        last[s[i]] = i
    
    opened = 0
    op = set()
    for i in range(len(s)):
        l = s[i]
        if l not in op:
            op.add(l)
        if len(op) > k:
            print('YES')
            exit()
        if last[l] == i:
            op.remove(l)
    print('NO')