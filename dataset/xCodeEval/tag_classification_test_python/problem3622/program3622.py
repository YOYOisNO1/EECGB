def program3622():
    n, t = input().split(" ")
    n = int(n)
    t = int(t)
    s = str(input())
    q = [s[x] for x in range(len(s))]
    i = 0
    while t > 0:
        i = 0
        while i < n - 1:
            if q[i] == "B" and q[i + 1] == "G":
                q[i] = "G"
                q[i + 1] = "B"
                i += 1
            i += 1
        t -= 1
    a = ""
    for k in range(len(q)):
        a += q[k]
    print(a)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    