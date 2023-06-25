def program3185():
    #!/usr/bin/env python
    # -*- coding: UTF-8 -*-
    import time
    import sys, io
    import re, math
    start = time.clock()
    l=list(input())
    while 1:
        ans,chk=0,[]
        stp=set(l)
        if len(stp)==len(l):
            cnt=0
            break
        for i in range(len(l)):
            if l[i] not in chk:
                cnt,j=2,i+1
                while l[i]!=l[j]:
                    cnt+=1
                    j+=1
                ans=max(ans,cnt)
                chk.append(l[i])
        break
    print ans