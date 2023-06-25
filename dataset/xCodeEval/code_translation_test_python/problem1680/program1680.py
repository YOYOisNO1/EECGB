def program1680():
    [h,m,s,t1,t2] = [int(x) for x in input().split()]
    hh = h + m/60 + s/3600 
    mm = m/5
    ss = s/5
    
    ll = [hh,mm,ss,t1,t2]
    ll = sorted(ll)
    
    diff = abs(ll.index(t1)-ll.index(t2))
    if diff==1 or diff==4:
        print('YES')
    else:
        print('NO')
    
    
    
    
    # Made By Mostafa_Khaled