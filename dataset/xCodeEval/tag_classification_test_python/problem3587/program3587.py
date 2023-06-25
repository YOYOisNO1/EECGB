def program3587():
    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-
    n,t = map(int,input().split())
    str1 = input()
    for time in range(0,t):
        str1 = str1.replace('BG','GB')
    print(str1)