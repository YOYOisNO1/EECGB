def program881():
    o, e = map(int, input().split())
    
    if abs(o - e) <= 1 and o + e > 0:
        print("YES")
    else:
        print("NO")