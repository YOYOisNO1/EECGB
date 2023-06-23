def program2053():
    a = []
    for i in range(8):
        m = input()
        if m.count("W") != 4:
            print("NO")
            exit(0)
        else:
            for i in range(7):
                if m[i] == m[i+1]:
                    print("NO")
                    exit(0)
    
    print "