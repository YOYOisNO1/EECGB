def program1313():
    n = int(input())
    s = str(input())
    k = 0
    cn = 0
    l = []
    ans = 0
    while k!=n:
        j = k
        ok = 0
        while str[j] == 'B':
            cn++;
            j+=1
            ok = 1
        l.append(cn)    
        if ok == 1:ans+=1
    
    print(ans)
    while ans > 0:
        print(l[ans - 1] , ' ')
        ans-=1