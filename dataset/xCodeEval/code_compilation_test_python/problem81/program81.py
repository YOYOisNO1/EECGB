def program81():
    # -*- coding: utf-8 -*-
    m=input().lower()
    n=input().lower()
    l=len(m)
    qwe=0
    for i in range(l):
        if ord(m[i])<ord(n[i]):
            print('-1')
            break
        elif ord(m[i])>ord(n[i]):
            print('1')
            break
        else:
            qwe=qwe+1
    if qwe==l:
        print('0')