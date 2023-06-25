def program3809():
    a=input()
    b=input()
    o=0
    t=[]
    i=0
    h=0
    c=0
    w=0
    j=0
    l=[int(d) for d in a]
    k=[int(i) for i in b]
    l.sort()
    l.reverse()
    if(len(l)<len(k)):
        print(''.join(map(str,l)))
    if(len(l)==len(k)):
        for i in range(0,len(k)):
            o=k[i]
            if(o in l):
                t.append(o)
                l.remove(o)
                l.sort()
                l.reverse()
                h=len(t)
            else:
                while(o not in l and o>=0):
                    o=o-1
                if(o in l):
                    t.append(o)
                    l.remove(o)
                    l.sort()
                    l.reverse()
                    break
                else:
                    while(c!=1):
                        for j in range(0,len(l)):
                            if(t[h-1]>l[j]):
                                c=c+1
                                w=l[j]
                                break
                        l.append(t[h-1])
                        l.sort()
                        l.reverse()
                        del(t[h-1])
                        h=len(t) 
                    t.append(w)
                    l.remove(w)
                    l.sort()
                    l.reverse()
                    break
        print(''.join(map(str,t+l)))