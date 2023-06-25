def program3165():
    #!/usr/bin/env python
    
    
    n, m = map(int, input().split())
    
    if m == n:
        if m == 1:
            print(1)
        else:
            print(m-1)
    elif m > n:
        print(n)
    else:
        if m <= n/2.0:
            print(m+1)
        else:
            print(m-1)