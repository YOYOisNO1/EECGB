def program1756():
    t = input()
    H = input().split()
    
    for c in H:
        if c[0] == t[0] or c[1] == t[1]:
            print("YES")
            quit()
    print("NO")