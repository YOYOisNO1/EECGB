def program272():
    from datetime import date
    
    abs = lambda x : x if x >= 0 else -x
    
    a1 = map(int, input().split(":"))
    a2 = map(int, input().split(":"))
    
    print(abs((date(a1[0],) a1[1], a1[2]) - date(a2[0], a2[1], a2[2])).days)