def program4173():
    import sys
    import math
    int_ = lambda x: int(x)-1
    n = int(sys.stdin.readline())
    p = [-1]*n
    #p[0]=-1
    k = int(sys.stdin.readline())
    groups = []
    for i in xrange(k):
        p1, p2 = map(int_, sys.stdin.readline().split())
        if p[p1] == p[p2] == -1:
            #new group
            grp_ind = len(groups)
            groups.append([p1,p2])
            p[p1] = grp_ind
            p[p2] = grp_ind
        elif p[p1] == -1:
            #move first to group of 2
            p[p1] = p[p2]
            groups[p[p2]].append(p1)
        elif p[p2] == -1:
            p[p2] = p[p1]
            groups[p[p1]].append(p2)
        else:
            #in dif groups, together!
            #from second group to first group
            for ind in xrange(len(p)):
                del_grp = p[p2]
                if p[ind] == del_grp:
                    groups[del_grp].pop(groups[del_grp].index(ind))
                    p[ind] = p[p1]
                    groups[p[p1]].append(ind)
                    
    #print p
    #print groups
    
    m = int(sys.stdin.readline())
    en = []
    for i in xrange(m):
        p1, p2 = map(int_, sys.stdin.readline().split())
        if p[p1]==p[p2]:
            #a oni v odno' gryppe (((
            groups[p[p1]] = []
        
    x = max(map(len, groups))
    if x==0 and -1 in p:
        x = 1
    print str(x)
    #
    
    
    
    