def program3770():
    # import sys
    # sys.stdin = open('in.txt', 'r')
    
    a, b, p, x = map(int, input().split())
    
    # A = [0, 1,   2, ..      p-2,    p-1] .. length = p
    # B = [1, a, a^2, ..  a^(p-2)]         .. length = p - 1
    
    # x * inv(x) * b = b
    
    # a^x -> inv(a*x) * b
    
    # 4 6 7 13
    # [0, 1, 2, 3, 4, 5, 6]
    # [0, 1, 2, 3, 4, 5]
    
    # 2 3 5 8
    # [0, 1, 2, 3]
    # [0, 1, 2]
    
    x += 1
    res = 0
    
    res += x//(p*(p-1)) * (p-1)
    x -= x//(p*(p-1)) * (p*(p-1))
    
    for i in range(p-1):
        ap = (pow(pow(a, i, p), p-2, p) * b) % p
        l = (x // (p-1)) + (1 if i < x%(p-1) else 0)
    
        if i >= ap and i-ap < l:
            res += 1
        elif i < ap and i+p-ap < l:
            res += 1
        # print(ap, l, res)
    
    print(res)
    
    # for i in range(1, x+1):
    #     print(i*pow(a,i,p)%p, end=' ')
    #     if i % (p-1) == 0:
    #         print()
    # print()