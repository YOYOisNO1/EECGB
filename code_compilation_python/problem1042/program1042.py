def program1042():
    import re
    n=input()
    s='1'
    mind=True
    if int(n[0])==1:
        for x in n:
            if(re.match(x,'1')):
                s=s+x
            elif(re.match(x,'1')):
                if(re.match(s,'1') or re.match(s,'14') or re.match(s,'144)):
                    s='1'
                    continue;
                else:
                    mind=False
            else:
                mind=False
    else:
        mind=False
    if(mind):
        print('YES')
    else:
        print('NO')