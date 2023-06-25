def program5106():
    dic = {}
    for i in range (10):
        dic[str(i)] = i
    dic['_'] = -1
    dic['X'] = -2
    
    s = list(input())
    # 25, 50, 75, 00
    if s[0]=='0' and len(s)!=1:
        print(0)
        exit()
    
    if len(s)==1:
        if s[0] in ['0', '_', 'X']:
            print(1)
        else:
            print(0)
        exit()
    a = []
    if s.count('X')==0:
        a.append(s)
    else:
        for i in range (10):
            if s[0]=='X' and i==0:
                continue
            cur = str(i)
            ns = s[:]
            for j in range (len(s)):
                if ns[j]=='X':
                    ns[j]=cur
            a.append(ns)
    if len(s)==2:
        na = []
        if s[0]=='_':
            for i in a:
                for j in range (1,10):
                    i[0]=str(j)
                    na.append(i[:])
        else:
            na = a[:]
        nna = []
        if s[1]=='_':
            for i in na:
                for j in range (10):
                    i[1]=str(j)
                    nna.append(i[:])
        else:
            nna = na[:]
        ans = 0
        for i in nna:
            if int(''.join(i))%25==0:
                ans+=1
        print(ans)
        exit()
    ans = 0
    for cs in a:
        cans = 0
        if cs[-1] not in ['_', '0', '5']:
            continue
        if cs[-2] not in ['_', '0', '7', '5', '2']:
            continue
        if cs[-1]!='_' and cs[-2]!='_':
            if ''.join(cs[-2:]) not in ['25', '50', '75', '00']:
                continue
            else:
                cnt = cs.count('_')
                if cs[0]=='_':
                    cans = 9 * 10**(cnt-1)
                else:
                    cans = 10**cnt
                ans+=cans
        elif cs[-1]!='_' and cs[-2]=='_':
            cnt = cs.count('_')
            if cs[0]=='_':
                cans = 9*2*10**(cnt-2)
            else:
                cans = 2*10**(cnt-1)
            ans+=cans
        elif cs[-1]=='_' and cs[-2]!='_':
            cnt = cs.count('_')
            if cs[0]=='_':
                cans = 9*10**(cnt-2)
            else:
                cans = 10**(cnt-1)
            ans+=cans
        else:
            cnt = cs.count('_')
            if cs[0]=='_':
                cans = 9*4*10**(cnt-3)
            else:
                cans = 4*10**(cnt-2)
            ans+=cans
    print(ans)