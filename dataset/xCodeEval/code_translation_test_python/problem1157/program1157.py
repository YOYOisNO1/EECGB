def program1157():
    from sys import stdin, stdout
    
    s = stdin.readline().strip()
    challengers = ['Danil', 'Olya', 'Slava', 'Ann', 'Nikita']
    n = len(s)
    cnt = 0
    
    s += '#' * 50
    
    for i in range(n):
        for f in challengers:
            if s[i: i + len(f)] == f:
                cnt += 1
    
    
    
    if cnt == 1:
        stdout.write('YES')
    else:
        stdout.write('NO')