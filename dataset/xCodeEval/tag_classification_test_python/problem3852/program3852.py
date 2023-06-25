def program3852():
    n = input()
    a = map(int,input().split())
    ans = 0
    m = a[0]
    if m == 0:ans += 1
    for i in xrange(1,n):
    
        if m==0 or m==3:
            if a[i]==0: 
                ans += 1
                m = 0
            elif a[i] == 3: m = 3
            elif a[i] == 1: m = 1
            else: m = 2
       
        elif m == 1:
            if a[i] == 1 or a[i] == 0:
                ans += 1
                m = 0
            else: m = 2
        else:
            if a[i] == 2 or a[i] == 0:
                ans += 1
                m = 0
            else: m = 1
    print(ans)