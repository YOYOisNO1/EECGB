def program2227():
    
    n = int(input())
    s1 = 1
    s2 = 1
    
    while s1*s2 < n:
        if s1 == s2:
            s1 += 1
        else:
            s2 += 1
    print(s1 + s2)