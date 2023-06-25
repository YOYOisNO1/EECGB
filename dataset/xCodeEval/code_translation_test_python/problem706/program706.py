def solve():
        keys = []
        rev = []
        for i in range(3):
            keys += list(input().strip())
        for i in keys:
            rev.insert(0,i)
        if keys == rev:
            print('YES')
        else:
            print('NO')
    
    solve()