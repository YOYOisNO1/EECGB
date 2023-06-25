def program2979():
    a = input()
    d = a.count('Danil')
    o = a.count('Olya')
    s = a.count('Slava')
    A = a.count('Ann')
    n = a.count('Nikita')
    if d+o+s+A+n==1:
        print('YES')
    else:
        print('NO')