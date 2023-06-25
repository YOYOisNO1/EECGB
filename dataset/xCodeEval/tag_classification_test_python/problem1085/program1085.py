def program1085():
    import itertools
    
    n = int(input())
    r,s,p = map(int,input().split())
    R,S,P = map(int,input().split())
    
    win_r = min(r,S)
    win_s = min(s,P)
    win_p = min(p,R)
    win = win_r + win_s + win_p
    
    res = n
    for perm in itertools.permutations(range(6)):
        rr,ss,pp = r,s,p
        RR,SS,PP = R,S,P
        asd = n
        for i in perm:
            if i == 0:
                mn = min(rr, RR)
                rr -= mn
                RR -= mn
            if i == 1:
                mn = min(ss, SS)
                ss -= mn
                SS -= mn
            if i == 2:
                mn = min(pp, PP)
                pp -= mn
                PP -= mn
            if i == 3:
                mn = min(rr, PP)
                rr -= mn
                PP -= mn
            if i == 4:
                mn = min(ss, RR)
                ss -= mn
                RR -= mn
            if i == 5:
                mn = min(pp, SS)
                pp -= mn
                SS -= mn
            asd -= mn
        res = min(asd, res)
    
    print(res, win)