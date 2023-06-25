def program1441():
    import sys
    
    s = sys.stdin.readline().strip()
    r = s[::-1]
    
    i = 0
    while r[i] == '0':
        i+=1
    
    p = r[i:]
    if p == p[::-1]:
        print("YES")
    else:
        print("NO")