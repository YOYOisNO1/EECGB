def program2():
    x, y = map(int, input().split())
    
    ans = 1
    
    sides = [y]*3
    
    while sides[-1] < x:
        ans += 1
        sides[2] = min(sides[0] + sides[1] - 1, x)
        sides = sorted(sides, reverse=True)
    
    print(ans-1)