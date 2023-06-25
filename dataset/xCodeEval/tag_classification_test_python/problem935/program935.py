def program935():
    n, a, b = map(int, input().split())
    s = 0
    i = 0
    k = 0
    
    while n != 1:
        n //= 2
        k += 1
    
    while s == 0:
        i += 1
        if (a == b+1) and (a % 2 == 0) or (b == a + 1) and (b % 2 == 0):
            s = i
        a = a // 2 + a % 2
        b = b // 2 + b % 2
    
    if s == k:
        print('Final!')
    else: print(s)