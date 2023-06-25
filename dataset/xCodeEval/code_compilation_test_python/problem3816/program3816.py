def program3816():
    from sys import stdin, stdout
    
    n = int(stdin.readline())
    
    for nn in range(n):
        a, b, m = map(int,stdin.readline().split())
        if a == b:
            stdout.write('{} {}\n'.format(1,a))
        else:
            for j in range(2,51):
                if (a+1)<<(j-2) <= b and b <= (a+m)<<(j-2):
                    B = b
                    b -= a<<(j-2)
                    stdout.write('{} {}'.format(j, a))
                    s = a
                    for i in range(j-2):
                        for k in range(m,0,-1):
                            if b - (k<<(j-3-i)) >= 1<<(j-3-i):
                                a = s+k
                                stdout.write(' {}'.format(a))
                                s += a
                                b -= k<<(j-3-i)
                                break
                    stdout.write(' {}\n'.format(B))
                    break
            else:
                stdout.write('-1\n')