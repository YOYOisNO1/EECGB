def program2393():
    a=input()
    b=input()
    t=[]
    l=list(a)
    k=list(b)
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
            else:
                while(o not in l):
                    o=o-1
                    if(o in l):
                        t.append(o)
                        l.remove(o)
                        break
                break
        t=t+l
        print((''.join(map(str,t)))