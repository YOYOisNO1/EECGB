def program3941():
    #!/usr/bin/env python3
    
    import sys
    
    w, m = list(map(int, sys.stdin.readline().split()))
    
    a = sum(pow(w, i) for i in range(101)) + m
    
    while a > 0:
        if a % w > 2:
            print('NO')
            sys.exit(0)
        a //= w
    
    print('YES')