def program3796():
    #!/usr/bin/python3
    
    n, m, a, b = map(int, input().split())
    
    a -= 1
    b -= 1
    if a // m == b // m:
        print(1)
    elif a % m == 0 and (b + 1) % m == 0:
        print(1)
    elif a % m == 0 and b + 1 == n:
        print(1)
    elif b + 1 == n:
        print(2)
    elif a % m == 0 or (b + 1) % m == 0:
        print(2)
    elif a % m == (b + 1) % m:
        print(2)
    elif b // m - a // m == 1:
        print(2)
    elif m == 2:
        print(2)
    else:
        print(3)