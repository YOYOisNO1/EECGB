def program60():
    n,pos,l,r = map(int, input().split())
    
    steps = 0
    if l== 1 and r == n:
        steps = 0
    elif l == 1:
        steps = abs(r - pos) + 1
    elif r == n:
        steps = abs(pos - l) + 1
    else:
        if pos < l:
            steps = l - pos + r - l + 2
        elif pos > r:
            steps = pos - l + 2
        else:
            steps = min(pos-l, r-pos) + r - l + 2
    
    print(steps)