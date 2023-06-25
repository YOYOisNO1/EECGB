def possible(g, b):
        if(b >= g - 1 and b <= 2*(g + 1)):
            return True
        return False
    
    l1, r1 = map(int, input().split())
    l2, r2 = map(int, input().split())
    if(possible(l1,r2) or possible(r1,l2)):
        print("YES")
    else:
        print("NO")