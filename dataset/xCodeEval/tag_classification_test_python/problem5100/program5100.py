def program5100():
    w=map(str,input().split('|'))
    s=input()
    sl=len(s)
    l,r=len(w[0]),len(w[1])
    x,y=max(l,r),min(l,r)
    t=sl+x+y
    if t%2 or x>y+sl:
        print('Impossible')
    else:
        ladd=t/2-l
        if r==t/2:
            print(w[0]+s+'|'+w[1])
        elif l==t/2:
            print(w[0]+'|'+w[1]+s)
        else:
            print(w[0]+s[:ladd]+'|'+w[1]+s[ladd:])