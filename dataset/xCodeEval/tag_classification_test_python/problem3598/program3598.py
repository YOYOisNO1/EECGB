def program3598():
    x = input()
    y = input()
    a = x.split(" ")
    n = int(a[0])
    t = int(a[1])
    q = list(y)
    
    for e in range(t):
        k = 0
        while k < n-1:
            if q[k] == "B" and q[k+1] == "G":
                q[k+1],q[k] = q[k],q[k+1]
                k =k+2
            else:
                k=k+1
                
    print('').join(q)