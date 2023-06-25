def program1895():
    v = [[] for i in xrange(12)]
    str = input().split()
    n = int(str[0])
    m = int(str[1])
    k = int(str[2])
    for i in xrange(n):
        input()
        for j in xrange(m):
            tuple = map(int,input().split());
            v[i].append(tuple)  
                
    mx =0
    for i in xrange(n):
        for j in xrange(n):
            val=0
            if(i==j):continue
            pro = []
            for kk in xrange(len(v[i])):
                if(v[j][kk][1] <= v[i][kk][0]): continue
                pro.append((v[j][kk][1] - v[i][kk][0], v[i][kk][2]))
                
            lim = k;
            pro.sort(cmp=None, key=None, reverse=True)
            for kk in xrange(len(pro)):
                if(pro[kk][1] <= lim):
                        lim -= pro[kk][1];
                        val += pro[kk][0]*pro[kk][1];
                    
                else:
                         val += pro[kk][0]*lim;
                         break;
            
            mx = max(mx,val)
    
    print(mx)