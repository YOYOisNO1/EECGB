    import os
    
    import sys
    
    debug = True
    
    if debug and os.path.exists("input.in"):
        input = open("input.in", "r").readline
    else:
        debug = False
        input = sys.stdin.readline
    
    
def inp():
        return (int(input()))
    
    
def inlt():
        return (list(map(int, input().split())))
    
    
def insr():
        s = input()
        return s[:len(s) - 1]  # Remove line char from end
    
    
def invr():
        return (map(int, input().split()))
    
    
    test_count = 1
    if debug:
        test_count = inp()
    
    
def takeSecond(elem):
        return elem[1]
    
    
    for t in range(test_count):
        if debug:
            print("Test Case #", t + 1)
        # Start code here
        n, m = invr()
        boxes = list()
        for i in range(m):
            a, b = invr()
            boxes.append((a, b))
            boxes.sort(key=takeSecond, reverse=True)
        ans = 0
        for box in boxes:
            ans += min(box[0], n) * box[1]
            n -= box[0]
            if n <= 0:
                break
        print(ans)