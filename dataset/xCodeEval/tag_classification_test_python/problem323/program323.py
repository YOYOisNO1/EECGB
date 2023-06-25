def program323():
    n = int(input())
    s = input()
    
    l = 0
    t = 0
    
    for c in s:
        if c == "x":
            l += 1
        elif l != 0:
            if l >= 3:
                t += l - 2
            l = 0
    
    if l != 0 and l >= 3:
        t += l - 2
    
    print(t)