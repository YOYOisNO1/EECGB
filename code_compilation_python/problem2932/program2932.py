def getans1(S,s1,s2):
        if s1>s2:
            l = sorted(S[3:])
            x = s1-s2
            if x+l[0]<10:
                return 1
            elif l[1]+x-(9-l[0])<10:
                return 2
            else:
                return 3
        else:
            l = sorted(S[:3])
            x = s2-s1
            if x+l[0]<10:
                return 1
            elif l[1]+x-(9-l[0])<10:
                return 2
            else:
                return 3
    
def getans2(S,s1,s2):
        if s1>s2:
            l = sorted(S[:3],reverse=True)
            x = s1-s2
            if l[0]-x>=0:
                return 1
            elif l[1]-(x-l[0])>=0:
                return 2
            else:
                return 3
        else:
            l = sorted(S[3:],reverse=True)
            x = s2-s1
            if l[0]-x>=0:
                return 1
            elif l[1]-(x-l[0])>=0:
                return 2
            else:
                return 3
            
            
    
    
    st = str(input())
    S = map(int,st)
    
    s1 = sum(S[:3])
    s2 = sum(S[3:])
    
    if s1==s2:
        print 0
    elif:
        print min(getans1(S,s1,s2),getans2(S,s1,s2))