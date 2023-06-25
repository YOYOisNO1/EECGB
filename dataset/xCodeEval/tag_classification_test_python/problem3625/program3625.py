def program3625():
    n, t = [int(x) for x in input().split()]
    
    s = list(input())
    
    while t > 0:
        t -= 1
    
        x = 0
        while x < len(s):
            if x == len(s) - 1:
                break
    
            if s[x] == "B" and s[x + 1] == "G":
                s[x], s[x + 1] = s[x + 1], s[x]
                x += 2
                continue
    
            x += 1
            
    print("".join(s))