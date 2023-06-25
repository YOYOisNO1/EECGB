def program11():
    a1, a2 = map(int, input().split())
    b1, b2 = map(int, input().split())
    
    if abs(b2 - a1) <= 1: print("YES")
    elif abs(b1 - a2) <= 1: print("YES")
    else: print("NO")