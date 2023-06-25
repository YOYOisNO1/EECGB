def program5855():
    [a,b,c] = map(int, input().split())
    r = float(c)*(a-b)/b
    if int(r) == r:
        print(int(r))
    else:
        print(int(r)+1)