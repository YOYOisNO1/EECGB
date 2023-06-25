def program1866():
    
    
    
    t=[ "a", "o", "u", "i",'e']
    
    a=list(input())
    u=0
    
    
    for k in range(len(a)-1):
        if a[k] not in t:
            if a[k]!='n':
                if a[k+1] in t:
                    pass
                else:
                    print('NO')
                    u+=1
                    break
            else:
                pass
        else:
            pass
    
    if u==0:
        if a[-1] not in t:
            if a[-1]!='n':
                print('NO')
            else:
                print('YES')
        elif a[-1] in t:
            print('YES')