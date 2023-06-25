    import sys
    input = sys.stdin.readline
    
    ############ ---- Input Functions ---- ############
def inp():
        return(int(input()))
def inlt():
        return(list(map(int,input().split())))
def insr():
        s = input()
        return(list(s[:len(s) - 1]))
def invr():
        return(map(int,input().split()))
    
    
    y, b, r = invr()
    mi = min(y, b, r)
    ma = max(y, b, r)
    if mi == y and mi != r and mi != b:
        b = y+1
        if b+1 > r:
            b = r - 1
            y = b - 1
        else:
            r = b+1
        #print(1)
    elif mi == b and mi != r:
        y = b-1
        r = b+1
        #print(2)
    elif mi == r:
        b = r-1
        y = b-1
        #print(3)
    print(y+r+b)