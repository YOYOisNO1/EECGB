def program258():
    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-
    n,t = map(int,input().split())
    list1 = list(input())
    m = 0
    for time in range(0,t):
        while m <= n - 1:
            if list1[m] == 'B' and list1[m+1] == 'G':
                list1[m] = 'G'
                list1[m+1] = 'B'
                m += 2
    print(''.join(list1))