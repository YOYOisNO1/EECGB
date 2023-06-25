def program3072():
    import sys
    
    n = int(sys.stdin.readline())
    
    s = list(sys.stdin.readline())
    
    s0, s1 = ""
    color = ""
    
    works = True
    
    for i in s:
        if s0 == "" or s0[-1] <= i:
            s0 += i
            color += 0
        elif s1 == "" or s1[-1] <= i:
            s0 += i
            color += 1
        else:
            works = False
            break
    
    if works = True:
        print("YES")
        print(color)
    else:
        print("NO")