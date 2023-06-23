def program1240():
    a = [0]*l
    b = [0]*l
    
    for i in range(n):
        a[track1[i]] = 1
        b[track2[i]] = 1
    for i in range(l):
        b.insert(0, b.pop())
        if b == a:
            print("YES")
            exit(0)
    print("NO")
            
        