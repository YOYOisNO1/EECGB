def program6337():
    s = input()
    
    st = 0
    en = 0
    
    ans = [['.' for _ in xrange(13)] for _ in xrange(2)]
    
    for i in xrange(ord('A'),ord('Z')+1):
        c = chr(i)
        st = s.find(c)
        en = s.find(c,st+1)
        if en != -1:
            break
    
    if st+1 == en:
        print("Impossible")
    else:
        l = (en-st)
        l += (l%2)
        ss = 13-(l/2)
        p = [ss,0]
        dr = 1
        for i in xrange(st,en):
            ans[p[1]][p[0]] = s[i]
            if (p[0]+dr == 13):
                p[1] += 1
                dr *= -1
            else:
                p[0] += dr
        p = [ss-1,0]
        dr = -1
        a = s[:st]
        b = s[en+1:]
        bf = a[::-1]+ b[::-1]
        for i in xrange(len(bf)):
            if p[0]<0:
                p[0] = 0
                p[1] = 1
                dr = 1
            ans[p[1]][p[0]] = bf[i]
            p[0] += dr
        print("").join(ans[0])
        print("").join(ans[1])
            
            