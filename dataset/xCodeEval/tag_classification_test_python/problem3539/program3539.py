def program3539():
    
    n, t = input().split()
    s = list(input())
    n = int(n)
    t = int(t)
    i = 0
    for x in range(t):
        while i < len(s) - 1:
            if s[i] == "B" and s[i+1] == "G":
                s[i] = "G"
                s[i+1] = "B"
                i += 1
            i += 1
        i = 0
    
    s = ''.join(s)
    print(s)