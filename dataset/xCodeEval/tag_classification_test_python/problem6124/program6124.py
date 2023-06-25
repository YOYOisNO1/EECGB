def program6124():
    r1, c1, r2, c2 = [int(i) for i in input().split()]
    ans = str()
    
    if r1 == r2 or c1 == c2:
        ans += '1 '
    else:
        ans += '2 '
    
    if ((r1 + c1) % 2 == 0 and (r2 + c2) % 2 == 1) or ((r2 + c2) % 2 == 0 and (r1 + c1) % 2 == 1):
        ans += '0 '
    elif (r1 + c1) == (r2 + c2) or (r2 - c2) == (r1 - c1):
        ans += '1 '
    else:
        ans += '2 '
    
    ans += str(max(abs(r2 - r1), abs(c2 - c1)))
    
    print(ans)