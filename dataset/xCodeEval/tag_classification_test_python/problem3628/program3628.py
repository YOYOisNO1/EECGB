def program3628():
    n,t = map(int, input().split())
    c_l = list(input())
    
    for count in range(t):
        p= 0
        while (p<n-1):
            if c_l[p] == "B" and c_l[p+1] == "G":
                c_l[p], c_l[p+1] = c_l[p+1], c_l[p]
                p+= 1
            p+= 1
        
    print("".join(c_l))