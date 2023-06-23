def program257():
    n, t = input().split()
    n = int(n)
    t = int(t)
    i = 0
    s = list(input())
    
    while s[0] != "G":
        while i < len(s) - 1:
            if s[i] == 'B' and s[i + 1] == "G":
                s[i] = "G"
                if i + t <= len(s) - t:
                    if s[i + t] == "B":
                        s[i + 1] = "B"
                    else:
                        s[i + t] = "B"
                if i + t > len(s) - t:
                    s[i + 1] = 'B'
                i += t
            i += 1
        i = 0
        t -= 1
    s = ''.join(s)
    print(s)