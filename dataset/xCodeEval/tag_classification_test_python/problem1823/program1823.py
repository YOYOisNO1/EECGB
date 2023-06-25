def program1823():
    n = input()
    
    l = []
    for i in range(n):
        x = input()
        k = 0
        for b in range(x/7 + 1):
            if((x - b) % 3 == 0 and (((x - b)/ 3) - 2*b >= 0)):
                k = 1
                break
        if k == 1:
            l.append("YES")
        else:
            l.append("NO")
    
    for i in range(n):
        print(l[i])