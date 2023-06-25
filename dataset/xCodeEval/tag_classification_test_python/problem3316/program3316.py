def check(a, b, c):
        if a + b > c and a + c > b and b + c > a:
            return True
        else:
            return False
    
    
    a, b, c = map(int, input().split())
    
    ans = 0
    while 7:
        if check(a, b, c):
            print(ans)
            exit()
        if a <= b and a <= c:
            a += 1
        elif b <= c and b <= a:
            b += 1
        else:
            c += 1
        ans += 1