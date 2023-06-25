def program680():
    from sys import stdin, stdout
    n, m = map(int, stdin.readline().split())
    
    if not n and not m:
        stdout.write('0 0')
    elif not n:
        stdout.write('Impossible')
    elif not m:
        stdout.write(str(n) + ' ' + str(n))
    elif n >= m:
        stdout.write(str(n) + ' ' + str(n + m - 1))
    else:
        stdout.write(str(m) + ' ' + str(n + m - 1))