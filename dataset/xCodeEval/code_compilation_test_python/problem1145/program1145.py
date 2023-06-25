def program1145():
    k, a, b, v = map(int, input().split())
    
    c = b // (k - 1)
    d = b % (k - 1) + 1
    s = a // v + 1
    result = 0
    while (a > 0 and c > 0):
        a -= k * v
        c -= 1
        result += 1
    
    if a > 0:
        a -= d * v
        result += 1
    
    while a > 0:
        result += a // v + 1
    
    print(result)
    