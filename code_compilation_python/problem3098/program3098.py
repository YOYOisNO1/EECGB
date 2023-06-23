def program3098():
    [12:21 AM, 3/31/2019] Sanket Agarwal: 1 baar code bhej
    [12:22 AM, 3/31/2019] Surya: a = list(input())
    c = 0
    t = 1
    for i in range(len(a)):
        j = int(a[i])
        t2 = t*(j-1)
        t = t*j
        c = max(t2*((9)**(len(a)-i-1)) , c)
        if i==0 and t2==0:
            c = max(((9)**(len(a)-i-1)) , c)
        
    c = max(t,c)
    print(c)