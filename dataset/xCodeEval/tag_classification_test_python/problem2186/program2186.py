def program2186():
    x = int(input())
    
    s = 0
    while x > 0:
        s += x & 1
        x >>= 1
    
    print(s)