def program4613():
    import string
    
    n, k = map(int, input().split())
    
    s, d, v = input(), [0] * (n + 1), 0
    
    for ch in string.ascii_uppercase:
    
        if ch in s:
    
            d[s.find(ch)] += 1
    
            d[s.rfind(ch) + 1] -= 1
    
    for x in d:
    
        v += x
    
        if v > k:
    
            print('YES')
    
            exit()
    
    print('NO')
    
    
    
    # Made By Mostafa_Khaled