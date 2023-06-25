def program3585():
    n, t = input().split()
    s = input()
    n = int(n)
    t = int(t)
    s = list(s)
    for i in range(t):
        check = True
        for j in range(n-1):
            switch = False
            if check and s[j] == "B":
                if s[j] != s[j+1]:
                    s[j], s[j+1] = s[j+1], s[j]
                    switch = True
            if switch:
                check = False
            else:
                check = True
    
    
    print("".join(s))
    
    
    
    
    
    
    