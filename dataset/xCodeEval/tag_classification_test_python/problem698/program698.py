def program698():
    from sys import stdin
    
    list = stdin.readline().split(" ")
    n = int(list[0])
    m = int(list[1])
    
    i = 0
    while m >= i:
        m -= i
        i = (i + 1) % (n + 1)
    
    print(m)