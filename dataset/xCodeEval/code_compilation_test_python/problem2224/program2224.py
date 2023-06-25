def program2224():
    n, m, k = map(int,input().split())
    
    x_min = min(k-1,n-k)
    x_max = max(k-1,n-k)
    s1 = sum(range(x_max+1))
    s2 = 0
    for i in range(x_min):
        s2 += x_max-i
    pods = x_max+1 + s1 + s2
    if(pods<=m):
        x = x_max+1 + ((m-pods)-(m-pods)%n)/n
        print x
    else:
        x = 1
        pods = n
        add = 0
        add_r = 0
        add_l = 0
        lim_l = 0
        f=0
        for j in range(n):
            add_r = j
            if(j<=x_min):
                add_l = j
                if(j+1>x_min):
                    lim_l = j
            else:
                add_l = lim_l
            add += 1 + add_r + add_l
            #print add,add_r,add_l,lim_l
            if(pods+add<=m):
                x += 1
            else: 
                print x
                f = 1
                break
        if(f==0):
            print x