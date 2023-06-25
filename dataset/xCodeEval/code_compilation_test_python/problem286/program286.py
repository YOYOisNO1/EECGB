    n = int(input())
    x = 0
def go(y):
        if (y//20000)%2 == 1:
            return 20000 - y%20000
        else:
            return  y%20000
        
    for i in range(n):
        s = input().split(' ')
        t = int(s[0])
        
        if x == 0:
            if s[1]=='South':
                x = go(x + t)
                continue
            else:
                x = 7
                break
            continue
        if x == 20000:
            if s[1]=='North':
                x = go(abs(x - t))
                continue
            else:
                x = 7
                break
        if (x!=0 and x!=20000):
            if s[1]=='South':
                x = go(x + t)
            if s[1]=='North':
                x = go(abs(x - t))
            
            
    if x == 0:
        print("YES")
    else:
        print("NO")
            